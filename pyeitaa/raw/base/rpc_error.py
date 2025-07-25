from typing import Union
from pyeitaa import raw

RpcError = Union[raw.types.RpcError, raw.types.RpcError]


# noinspection PyRedeclaration
class RpcError:
    """This base type has 2 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`RpcError <pyeitaa.raw.types.RpcError>`
            - :obj:`RpcError <pyeitaa.raw.types.RpcError>`
    """

    QUALNAME = "pyeitaa.raw.base.RpcError"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
