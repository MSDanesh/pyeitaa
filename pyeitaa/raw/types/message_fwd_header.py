from io import BytesIO

from pyeitaa.raw.core.primitives import Int, String
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Optional, Any, Self


class MessageFwdHeader(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.MessageFwdHeader`.

    Details:
        - Layer: ``135``
        - ID: ``0x5f777dce``

    Parameters:
        date: ``int`` ``32-bit``
        imported (optional): ``bool``
        from_id (optional): :obj:`Peer <pyeitaa.raw.base.Peer>`
        from_name (optional): ``str``
        channel_post (optional): ``int`` ``32-bit``
        post_author (optional): ``str``
        saved_from_peer (optional): :obj:`Peer <pyeitaa.raw.base.Peer>`
        saved_from_msg_id (optional): ``int`` ``32-bit``
        psa_type (optional): ``str``
    """

    __slots__: List[str] = ["date", "imported", "from_id", "from_name", "channel_post", "post_author", "saved_from_peer", "saved_from_msg_id", "psa_type"]

    ID = 0x5f777dce
    QUALNAME = "types.MessageFwdHeader"

    def __init__(self, *, date: int, imported: Optional[bool] = None, from_id: "raw.base.Peer" = None, from_name: Optional[str] = None, channel_post: Optional[int] = None, post_author: Optional[str] = None, saved_from_peer: "raw.base.Peer" = None, saved_from_msg_id: Optional[int] = None, psa_type: Optional[str] = None) -> None:
        self.date = date  # int
        self.imported = imported  # flags.7?true
        self.from_id = from_id  # flags.0?Peer
        self.from_name = from_name  # flags.5?string
        self.channel_post = channel_post  # flags.2?int
        self.post_author = post_author  # flags.3?string
        self.saved_from_peer = saved_from_peer  # flags.4?Peer
        self.saved_from_msg_id = saved_from_msg_id  # flags.4?int
        self.psa_type = psa_type  # flags.6?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        flags = Int.read(data)
        
        imported = True if flags & (1 << 7) else False
        from_id = TLObject.read(data) if flags & (1 << 0) else None
        
        from_name = String.read(data) if flags & (1 << 5) else None
        date = Int.read(data)
        
        channel_post = Int.read(data) if flags & (1 << 2) else None
        post_author = String.read(data) if flags & (1 << 3) else None
        saved_from_peer = TLObject.read(data) if flags & (1 << 4) else None
        
        saved_from_msg_id = Int.read(data) if flags & (1 << 4) else None
        psa_type = String.read(data) if flags & (1 << 6) else None
        return MessageFwdHeader(date=date, imported=imported, from_id=from_id, from_name=from_name, channel_post=channel_post, post_author=post_author, saved_from_peer=saved_from_peer, saved_from_msg_id=saved_from_msg_id, psa_type=psa_type)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        flags = 0
        flags |= (1 << 7) if self.imported else 0
        flags |= (1 << 0) if self.from_id is not None else 0
        flags |= (1 << 5) if self.from_name is not None else 0
        flags |= (1 << 2) if self.channel_post is not None else 0
        flags |= (1 << 3) if self.post_author is not None else 0
        flags |= (1 << 4) if self.saved_from_peer is not None else 0
        flags |= (1 << 4) if self.saved_from_msg_id is not None else 0
        flags |= (1 << 6) if self.psa_type is not None else 0
        data.write(Int(flags))
        
        if self.from_id is not None:
            data.write(self.from_id.write())
        
        if self.from_name is not None:
            data.write(String(self.from_name))
        
        data.write(Int(self.date))
        
        if self.channel_post is not None:
            data.write(Int(self.channel_post))
        
        if self.post_author is not None:
            data.write(String(self.post_author))
        
        if self.saved_from_peer is not None:
            data.write(self.saved_from_peer.write())
        
        if self.saved_from_msg_id is not None:
            data.write(Int(self.saved_from_msg_id))
        
        if self.psa_type is not None:
            data.write(String(self.psa_type))
        
        return data.getvalue()
