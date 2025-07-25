from io import BytesIO

from pyeitaa.raw.core.primitives import Int
from pyeitaa.raw.core import TLObject
from typing import List, Any, Self


class ThemesNotModified(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.account.Themes`.

    Details:
        - Layer: ``135``
        - ID: ``-0xbe149de``

    **No parameters required.**

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetThemes <pyeitaa.raw.functions.account.GetThemes>`
    """

    __slots__: List[str] = []

    ID = -0xbe149de
    QUALNAME = "types.account.ThemesNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        # No flags
        
        return ThemesNotModified()

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        # No flags
        
        return data.getvalue()
