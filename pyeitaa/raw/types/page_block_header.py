from io import BytesIO

from pyeitaa.raw.core.primitives import Int
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Any, Self


class PageBlockHeader(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.PageBlock`.

    Details:
        - Layer: ``135``
        - ID: ``-0x402f9b14``

    Parameters:
        text: :obj:`RichText <pyeitaa.raw.base.RichText>`
    """

    __slots__: List[str] = ["text"]

    ID = -0x402f9b14
    QUALNAME = "types.PageBlockHeader"

    def __init__(self, *, text: "raw.base.RichText") -> None:
        self.text = text  # RichText

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        # No flags
        
        text = TLObject.read(data)
        
        return PageBlockHeader(text=text)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        # No flags
        
        data.write(self.text.write())
        
        return data.getvalue()
