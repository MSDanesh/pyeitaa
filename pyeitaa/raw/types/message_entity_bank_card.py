from io import BytesIO

from pyeitaa.raw.core.primitives import Int
from pyeitaa.raw.core import TLObject
from typing import List, Any, Self


class MessageEntityBankCard(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.MessageEntity`.

    Details:
        - Layer: ``135``
        - ID: ``0x761e6af4``

    Parameters:
        offset: ``int`` ``32-bit``
        length: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["offset", "length"]

    ID = 0x761e6af4
    QUALNAME = "types.MessageEntityBankCard"

    def __init__(self, *, offset: int, length: int) -> None:
        self.offset = offset  # int
        self.length = length  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        # No flags
        
        offset = Int.read(data)
        
        length = Int.read(data)
        
        return MessageEntityBankCard(offset=offset, length=length)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        # No flags
        
        data.write(Int(self.offset))
        
        data.write(Int(self.length))
        
        return data.getvalue()
