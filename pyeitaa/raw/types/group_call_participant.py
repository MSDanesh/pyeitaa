from io import BytesIO

from pyeitaa.raw.core.primitives import Int, Long, String
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Optional, Any, Self


class GroupCallParticipant(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.GroupCallParticipant`.

    Details:
        - Layer: ``135``
        - ID: ``-0x1459c902``

    Parameters:
        peer: :obj:`Peer <pyeitaa.raw.base.Peer>`
        date: ``int`` ``32-bit``
        source: ``int`` ``32-bit``
        muted (optional): ``bool``
        left (optional): ``bool``
        can_self_unmute (optional): ``bool``
        just_joined (optional): ``bool``
        versioned (optional): ``bool``
        min (optional): ``bool``
        muted_by_you (optional): ``bool``
        volume_by_admin (optional): ``bool``
        is_self (optional): ``bool``
        video_joined (optional): ``bool``
        active_date (optional): ``int`` ``32-bit``
        volume (optional): ``int`` ``32-bit``
        about (optional): ``str``
        raise_hand_rating (optional): ``int`` ``64-bit``
        video (optional): :obj:`GroupCallParticipantVideo <pyeitaa.raw.base.GroupCallParticipantVideo>`
        presentation (optional): :obj:`GroupCallParticipantVideo <pyeitaa.raw.base.GroupCallParticipantVideo>`
    """

    __slots__: List[str] = ["peer", "date", "source", "muted", "left", "can_self_unmute", "just_joined", "versioned", "min", "muted_by_you", "volume_by_admin", "is_self", "video_joined", "active_date", "volume", "about", "raise_hand_rating", "video", "presentation"]

    ID = -0x1459c902
    QUALNAME = "types.GroupCallParticipant"

    def __init__(self, *, peer: "raw.base.Peer", date: int, source: int, muted: Optional[bool] = None, left: Optional[bool] = None, can_self_unmute: Optional[bool] = None, just_joined: Optional[bool] = None, versioned: Optional[bool] = None, min: Optional[bool] = None, muted_by_you: Optional[bool] = None, volume_by_admin: Optional[bool] = None, is_self: Optional[bool] = None, video_joined: Optional[bool] = None, active_date: Optional[int] = None, volume: Optional[int] = None, about: Optional[str] = None, raise_hand_rating: Optional[int] = None, video: "raw.base.GroupCallParticipantVideo" = None, presentation: "raw.base.GroupCallParticipantVideo" = None) -> None:
        self.peer = peer  # Peer
        self.date = date  # int
        self.source = source  # int
        self.muted = muted  # flags.0?true
        self.left = left  # flags.1?true
        self.can_self_unmute = can_self_unmute  # flags.2?true
        self.just_joined = just_joined  # flags.4?true
        self.versioned = versioned  # flags.5?true
        self.min = min  # flags.8?true
        self.muted_by_you = muted_by_you  # flags.9?true
        self.volume_by_admin = volume_by_admin  # flags.10?true
        self.is_self = is_self  # flags.12?true
        self.video_joined = video_joined  # flags.15?true
        self.active_date = active_date  # flags.3?int
        self.volume = volume  # flags.7?int
        self.about = about  # flags.11?string
        self.raise_hand_rating = raise_hand_rating  # flags.13?long
        self.video = video  # flags.6?GroupCallParticipantVideo
        self.presentation = presentation  # flags.14?GroupCallParticipantVideo

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        flags = Int.read(data)
        
        muted = True if flags & (1 << 0) else False
        left = True if flags & (1 << 1) else False
        can_self_unmute = True if flags & (1 << 2) else False
        just_joined = True if flags & (1 << 4) else False
        versioned = True if flags & (1 << 5) else False
        min = True if flags & (1 << 8) else False
        muted_by_you = True if flags & (1 << 9) else False
        volume_by_admin = True if flags & (1 << 10) else False
        is_self = True if flags & (1 << 12) else False
        video_joined = True if flags & (1 << 15) else False
        peer = TLObject.read(data)
        
        date = Int.read(data)
        
        active_date = Int.read(data) if flags & (1 << 3) else None
        source = Int.read(data)
        
        volume = Int.read(data) if flags & (1 << 7) else None
        about = String.read(data) if flags & (1 << 11) else None
        raise_hand_rating = Long.read(data) if flags & (1 << 13) else None
        video = TLObject.read(data) if flags & (1 << 6) else None
        
        presentation = TLObject.read(data) if flags & (1 << 14) else None
        
        return GroupCallParticipant(peer=peer, date=date, source=source, muted=muted, left=left, can_self_unmute=can_self_unmute, just_joined=just_joined, versioned=versioned, min=min, muted_by_you=muted_by_you, volume_by_admin=volume_by_admin, is_self=is_self, video_joined=video_joined, active_date=active_date, volume=volume, about=about, raise_hand_rating=raise_hand_rating, video=video, presentation=presentation)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 1) if self.left else 0
        flags |= (1 << 2) if self.can_self_unmute else 0
        flags |= (1 << 4) if self.just_joined else 0
        flags |= (1 << 5) if self.versioned else 0
        flags |= (1 << 8) if self.min else 0
        flags |= (1 << 9) if self.muted_by_you else 0
        flags |= (1 << 10) if self.volume_by_admin else 0
        flags |= (1 << 12) if self.is_self else 0
        flags |= (1 << 15) if self.video_joined else 0
        flags |= (1 << 3) if self.active_date is not None else 0
        flags |= (1 << 7) if self.volume is not None else 0
        flags |= (1 << 11) if self.about is not None else 0
        flags |= (1 << 13) if self.raise_hand_rating is not None else 0
        flags |= (1 << 6) if self.video is not None else 0
        flags |= (1 << 14) if self.presentation is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(Int(self.date))
        
        if self.active_date is not None:
            data.write(Int(self.active_date))
        
        data.write(Int(self.source))
        
        if self.volume is not None:
            data.write(Int(self.volume))
        
        if self.about is not None:
            data.write(String(self.about))
        
        if self.raise_hand_rating is not None:
            data.write(Long(self.raise_hand_rating))
        
        if self.video is not None:
            data.write(self.video.write())
        
        if self.presentation is not None:
            data.write(self.presentation.write())
        
        return data.getvalue()
