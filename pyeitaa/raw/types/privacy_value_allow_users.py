from io import BytesIO

from pyeitaa.raw.core.primitives import Int, Long, Vector
from pyeitaa.raw.core import TLObject
from typing import List, Any, Self


class PrivacyValueAllowUsers(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.PrivacyRule`.

    Details:
        - Layer: ``135``
        - ID: ``-0x476fa04e``

    Parameters:
        users: List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["users"]

    ID = -0x476fa04e
    QUALNAME = "types.PrivacyValueAllowUsers"

    def __init__(self, *, users: List[int]) -> None:
        self.users = users  # Vector<long>

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        # No flags
        
        users = TLObject.read(data, Long)
        
        return PrivacyValueAllowUsers(users=users)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        # No flags
        
        data.write(Vector(self.users, Long))
        
        return data.getvalue()
