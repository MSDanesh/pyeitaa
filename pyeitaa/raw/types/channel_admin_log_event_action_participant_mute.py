from io import BytesIO

from pyeitaa.raw.core.primitives import Int
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Any, Self


class ChannelAdminLogEventActionParticipantMute(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``135``
        - ID: ``-0x6dbdb2e``

    Parameters:
        participant: :obj:`GroupCallParticipant <pyeitaa.raw.base.GroupCallParticipant>`
    """

    __slots__: List[str] = ["participant"]

    ID = -0x6dbdb2e
    QUALNAME = "types.ChannelAdminLogEventActionParticipantMute"

    def __init__(self, *, participant: "raw.base.GroupCallParticipant") -> None:
        self.participant = participant  # GroupCallParticipant

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        # No flags
        
        participant = TLObject.read(data)
        
        return ChannelAdminLogEventActionParticipantMute(participant=participant)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        # No flags
        
        data.write(self.participant.write())
        
        return data.getvalue()
