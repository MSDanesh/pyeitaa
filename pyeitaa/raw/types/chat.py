from io import BytesIO

from pyeitaa.raw.core.primitives import Int, Long, String
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Optional, Any, Self


class Chat(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.Chat`.

    Details:
        - Layer: ``135``
        - ID: ``0x41cbf256``

    Parameters:
        id: ``int`` ``64-bit``
        title: ``str``
        photo: :obj:`ChatPhoto <pyeitaa.raw.base.ChatPhoto>`
        participants_count: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
        creator (optional): ``bool``
        kicked (optional): ``bool``
        left (optional): ``bool``
        deactivated (optional): ``bool``
        call_active (optional): ``bool``
        call_not_empty (optional): ``bool``
        noforwards (optional): ``bool``
        migrated_to (optional): :obj:`InputChannel <pyeitaa.raw.base.InputChannel>`
        admin_rights (optional): :obj:`ChatAdminRights <pyeitaa.raw.base.ChatAdminRights>`
        default_banned_rights (optional): :obj:`ChatBannedRights <pyeitaa.raw.base.ChatBannedRights>`
    """

    __slots__: List[str] = ["id", "title", "photo", "participants_count", "date", "version", "creator", "kicked", "left", "deactivated", "call_active", "call_not_empty", "noforwards", "migrated_to", "admin_rights", "default_banned_rights"]

    ID = 0x41cbf256
    QUALNAME = "types.Chat"

    def __init__(self, *, id: int, title: str, photo: "raw.base.ChatPhoto", participants_count: int, date: int, version: int, creator: Optional[bool] = None, kicked: Optional[bool] = None, left: Optional[bool] = None, deactivated: Optional[bool] = None, call_active: Optional[bool] = None, call_not_empty: Optional[bool] = None, noforwards: Optional[bool] = None, migrated_to: "raw.base.InputChannel" = None, admin_rights: "raw.base.ChatAdminRights" = None, default_banned_rights: "raw.base.ChatBannedRights" = None) -> None:
        self.id = id  # long
        self.title = title  # string
        self.photo = photo  # ChatPhoto
        self.participants_count = participants_count  # int
        self.date = date  # int
        self.version = version  # int
        self.creator = creator  # flags.0?true
        self.kicked = kicked  # flags.1?true
        self.left = left  # flags.2?true
        self.deactivated = deactivated  # flags.5?true
        self.call_active = call_active  # flags.23?true
        self.call_not_empty = call_not_empty  # flags.24?true
        self.noforwards = noforwards  # flags.25?true
        self.migrated_to = migrated_to  # flags.6?InputChannel
        self.admin_rights = admin_rights  # flags.14?ChatAdminRights
        self.default_banned_rights = default_banned_rights  # flags.18?ChatBannedRights

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        flags = Int.read(data)
        
        creator = True if flags & (1 << 0) else False
        kicked = True if flags & (1 << 1) else False
        left = True if flags & (1 << 2) else False
        deactivated = True if flags & (1 << 5) else False
        call_active = True if flags & (1 << 23) else False
        call_not_empty = True if flags & (1 << 24) else False
        noforwards = True if flags & (1 << 25) else False
        id = Long.read(data)
        
        title = String.read(data)
        
        photo = TLObject.read(data)
        
        participants_count = Int.read(data)
        
        date = Int.read(data)
        
        version = Int.read(data)
        
        migrated_to = TLObject.read(data) if flags & (1 << 6) else None
        
        admin_rights = TLObject.read(data) if flags & (1 << 14) else None
        
        default_banned_rights = TLObject.read(data) if flags & (1 << 18) else None
        
        return Chat(id=id, title=title, photo=photo, participants_count=participants_count, date=date, version=version, creator=creator, kicked=kicked, left=left, deactivated=deactivated, call_active=call_active, call_not_empty=call_not_empty, noforwards=noforwards, migrated_to=migrated_to, admin_rights=admin_rights, default_banned_rights=default_banned_rights)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 1) if self.kicked else 0
        flags |= (1 << 2) if self.left else 0
        flags |= (1 << 5) if self.deactivated else 0
        flags |= (1 << 23) if self.call_active else 0
        flags |= (1 << 24) if self.call_not_empty else 0
        flags |= (1 << 25) if self.noforwards else 0
        flags |= (1 << 6) if self.migrated_to is not None else 0
        flags |= (1 << 14) if self.admin_rights is not None else 0
        flags |= (1 << 18) if self.default_banned_rights is not None else 0
        data.write(Int(flags))
        
        data.write(Long(self.id))
        
        data.write(String(self.title))
        
        data.write(self.photo.write())
        
        data.write(Int(self.participants_count))
        
        data.write(Int(self.date))
        
        data.write(Int(self.version))
        
        if self.migrated_to is not None:
            data.write(self.migrated_to.write())
        
        if self.admin_rights is not None:
            data.write(self.admin_rights.write())
        
        if self.default_banned_rights is not None:
            data.write(self.default_banned_rights.write())
        
        return data.getvalue()
