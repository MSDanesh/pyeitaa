from io import BytesIO
from json import dumps
from typing import cast, List, Any, Union, Dict

from ..all import objects


class TLObject:
    __slots__: List[str] = []

    QUALNAME = "Base"

    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> Any:
        return cast(TLObject, objects[int.from_bytes(data.read(4), "little", signed=True)]).read(data, *args)

    def write(self, *args: Any) -> bytes:
        pass

    @staticmethod
    def default(obj: "TLObject") -> Union[str, Dict[str, str]]:
        if isinstance(obj, bytes):
            return repr(obj)

        return {
            "_": obj.QUALNAME,
            **{
                attr: getattr(obj, attr)
                for attr in obj.__slots__
                if getattr(obj, attr) is not None
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=TLObject.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "pyeitaa.raw.{}({})".format(
            self.QUALNAME,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in self.__slots__
                if getattr(self, attr) is not None
            )
        )

    def __eq__(self, other: Any) -> bool:
        for attr in self.__slots__:
            try:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __len__(self) -> int:
        return len(self.write())

    def __getitem__(self, item: Any) -> Any:
        return getattr(self, item)

    def __setitem__(self, key: Any, value: Any) -> Any:
        setattr(self, key, value)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        pass
