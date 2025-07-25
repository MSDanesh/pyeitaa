from io import BytesIO

from pyeitaa.raw.core.primitives import Int
from pyeitaa.raw.core import TLObject
from typing import List, Any, Self


class GetState(TLObject):
    """Eitaa API method.

    Details:
        - Layer: ``135``
        - ID: ``-0x122b77d6``

    **No parameters required.**

    Returns:
        :obj:`updates.State <pyeitaa.raw.base.updates.State>`
    """

    __slots__: List[str] = []

    ID = -0x122b77d6
    QUALNAME = "functions.updates.GetState"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        # No flags
        
        return GetState()

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        # No flags
        
        return data.getvalue()
