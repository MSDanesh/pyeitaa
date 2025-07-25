from io import BytesIO

from pyeitaa.raw.core.primitives import Int, Long, String, Vector
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Optional, Any, Self


class User(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.User`.

    Details:
        - Layer: ``135``
        - ID: ``-0x132d9235``

    Parameters:
        flags2: :obj:`# <pyeitaa.raw.base.#>`
        eFlags: :obj:`# <pyeitaa.raw.base.#>`
        id: ``int`` ``64-bit``
        miniApp: ``bool``
        badge_name: ``str``
        badge_red_color: ``bool``
        miniAppGeo: ``bool``
        bot_active_users: ``int`` ``32-bit``
        is_self (optional): ``bool``
        contact (optional): ``bool``
        mutual_contact (optional): ``bool``
        deleted (optional): ``bool``
        bot (optional): ``bool``
        bot_chat_history (optional): ``bool``
        bot_nochats (optional): ``bool``
        verified (optional): ``bool``
        restricted (optional): ``bool``
        min (optional): ``bool``
        bot_inline_geo (optional): ``bool``
        support (optional): ``bool``
        scam (optional): ``bool``
        apply_min_photo (optional): ``bool``
        fake (optional): ``bool``
        access_hash (optional): ``int`` ``64-bit``
        first_name (optional): ``str``
        last_name (optional): ``str``
        username (optional): ``str``
        phone (optional): ``str``
        photo (optional): :obj:`UserProfilePhoto <pyeitaa.raw.base.UserProfilePhoto>`
        status (optional): :obj:`UserStatus <pyeitaa.raw.base.UserStatus>`
        bot_info_version (optional): ``int`` ``32-bit``
        restriction_reason (optional): List of :obj:`RestrictionReason <pyeitaa.raw.base.RestrictionReason>`
        bot_inline_placeholder (optional): ``str``
        lang_code (optional): ``str``

    See Also:
        This object can be returned by 4 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.UpdateProfile <pyeitaa.raw.functions.account.UpdateProfile>`
            - :obj:`account.UpdateUsername <pyeitaa.raw.functions.account.UpdateUsername>`
            - :obj:`account.ChangePhone <pyeitaa.raw.functions.account.ChangePhone>`
            - :obj:`users.GetUsers <pyeitaa.raw.functions.users.GetUsers>`
    """

    __slots__: List[str] = ["id", "miniApp", "badge_name", "badge_red_color", "miniAppGeo", "bot_active_users", "is_self", "contact", "mutual_contact", "deleted", "bot", "bot_chat_history", "bot_nochats", "verified", "restricted", "min", "bot_inline_geo", "support", "scam", "apply_min_photo", "fake", "access_hash", "first_name", "last_name", "username", "phone", "photo", "status", "bot_info_version", "restriction_reason", "bot_inline_placeholder", "lang_code"]

    ID = -0x132d9235
    QUALNAME = "types.User"

    def __init__(self, *, id: int, miniApp: Optional[bool], badge_name: Optional[str], badge_red_color: Optional[bool], miniAppGeo: Optional[bool], bot_active_users: Optional[int], is_self: Optional[bool] = None, contact: Optional[bool] = None, mutual_contact: Optional[bool] = None, deleted: Optional[bool] = None, bot: Optional[bool] = None, bot_chat_history: Optional[bool] = None, bot_nochats: Optional[bool] = None, verified: Optional[bool] = None, restricted: Optional[bool] = None, min: Optional[bool] = None, bot_inline_geo: Optional[bool] = None, support: Optional[bool] = None, scam: Optional[bool] = None, apply_min_photo: Optional[bool] = None, fake: Optional[bool] = None, access_hash: Optional[int] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, username: Optional[str] = None, phone: Optional[str] = None, photo: "raw.base.UserProfilePhoto" = None, status: "raw.base.UserStatus" = None, bot_info_version: Optional[int] = None, restriction_reason: Optional[List["raw.base.RestrictionReason"]] = None, bot_inline_placeholder: Optional[str] = None, lang_code: Optional[str] = None) -> None:
        self.id = id  # long
        self.miniApp = miniApp  # eFlags.0?true
        self.badge_name = badge_name  # eFlags.1?string
        self.badge_red_color = badge_red_color  # eFlags.2?true
        self.miniAppGeo = miniAppGeo  # eFlags.4?true
        self.bot_active_users = bot_active_users  # flags2.12?int
        self.is_self = is_self  # flags.10?true
        self.contact = contact  # flags.11?true
        self.mutual_contact = mutual_contact  # flags.12?true
        self.deleted = deleted  # flags.13?true
        self.bot = bot  # flags.14?true
        self.bot_chat_history = bot_chat_history  # flags.15?true
        self.bot_nochats = bot_nochats  # flags.16?true
        self.verified = verified  # flags.17?true
        self.restricted = restricted  # flags.18?true
        self.min = min  # flags.20?true
        self.bot_inline_geo = bot_inline_geo  # flags.21?true
        self.support = support  # flags.23?true
        self.scam = scam  # flags.24?true
        self.apply_min_photo = apply_min_photo  # flags.25?true
        self.fake = fake  # flags.26?true
        self.access_hash = access_hash  # flags.0?long
        self.first_name = first_name  # flags.1?string
        self.last_name = last_name  # flags.2?string
        self.username = username  # flags.3?string
        self.phone = phone  # flags.4?string
        self.photo = photo  # flags.5?UserProfilePhoto
        self.status = status  # flags.6?UserStatus
        self.bot_info_version = bot_info_version  # flags.14?int
        self.restriction_reason = restriction_reason  # flags.18?Vector<RestrictionReason>
        self.bot_inline_placeholder = bot_inline_placeholder  # flags.19?string
        self.lang_code = lang_code  # flags.22?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        flags = Int.read(data)
        flags2 = Int.read(data)
        eFlags = Int.read(data)
        
        is_self = True if flags & (1 << 10) else False
        contact = True if flags & (1 << 11) else False
        mutual_contact = True if flags & (1 << 12) else False
        deleted = True if flags & (1 << 13) else False
        bot = True if flags & (1 << 14) else False
        bot_chat_history = True if flags & (1 << 15) else False
        bot_nochats = True if flags & (1 << 16) else False
        verified = True if flags & (1 << 17) else False
        restricted = True if flags & (1 << 18) else False
        min = True if flags & (1 << 20) else False
        bot_inline_geo = True if flags & (1 << 21) else False
        support = True if flags & (1 << 23) else False
        scam = True if flags & (1 << 24) else False
        apply_min_photo = True if flags & (1 << 25) else False
        fake = True if flags & (1 << 26) else False
        id = Long.read(data)
        
        access_hash = Long.read(data) if flags & (1 << 0) else None
        first_name = String.read(data) if flags & (1 << 1) else None
        last_name = String.read(data) if flags & (1 << 2) else None
        username = String.read(data) if flags & (1 << 3) else None
        phone = String.read(data) if flags & (1 << 4) else None
        photo = TLObject.read(data) if flags & (1 << 5) else None
        
        status = TLObject.read(data) if flags & (1 << 6) else None
        
        bot_info_version = Int.read(data) if flags & (1 << 14) else None
        restriction_reason = TLObject.read(data) if flags & (1 << 18) else []
        
        bot_inline_placeholder = String.read(data) if flags & (1 << 19) else None
        lang_code = String.read(data) if flags & (1 << 22) else None
        miniApp = TLObject.read(data) if eFlags & (1 << 0) else None
        
        badge_name = TLObject.read(data) if eFlags & (1 << 1) else None
        
        badge_red_color = TLObject.read(data) if eFlags & (1 << 2) else None
        
        miniAppGeo = TLObject.read(data) if eFlags & (1 << 4) else None
        
        bot_active_users = TLObject.read(data) if flags2 & (1 << 12) else None
        
        return User(id=id, miniApp=miniApp, badge_name=badge_name, badge_red_color=badge_red_color, miniAppGeo=miniAppGeo, bot_active_users=bot_active_users, is_self=is_self, contact=contact, mutual_contact=mutual_contact, deleted=deleted, bot=bot, bot_chat_history=bot_chat_history, bot_nochats=bot_nochats, verified=verified, restricted=restricted, min=min, bot_inline_geo=bot_inline_geo, support=support, scam=scam, apply_min_photo=apply_min_photo, fake=fake, access_hash=access_hash, first_name=first_name, last_name=last_name, username=username, phone=phone, photo=photo, status=status, bot_info_version=bot_info_version, restriction_reason=restriction_reason, bot_inline_placeholder=bot_inline_placeholder, lang_code=lang_code)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        flags = 0
        flags |= (1 << 10) if self.is_self else 0
        flags |= (1 << 11) if self.contact else 0
        flags |= (1 << 12) if self.mutual_contact else 0
        flags |= (1 << 13) if self.deleted else 0
        flags |= (1 << 14) if self.bot else 0
        flags |= (1 << 15) if self.bot_chat_history else 0
        flags |= (1 << 16) if self.bot_nochats else 0
        flags |= (1 << 17) if self.verified else 0
        flags |= (1 << 18) if self.restricted else 0
        flags |= (1 << 20) if self.min else 0
        flags |= (1 << 21) if self.bot_inline_geo else 0
        flags |= (1 << 23) if self.support else 0
        flags |= (1 << 24) if self.scam else 0
        flags |= (1 << 25) if self.apply_min_photo else 0
        flags |= (1 << 26) if self.fake else 0
        flags |= (1 << 0) if self.access_hash is not None else 0
        flags |= (1 << 1) if self.first_name is not None else 0
        flags |= (1 << 2) if self.last_name is not None else 0
        flags |= (1 << 3) if self.username is not None else 0
        flags |= (1 << 4) if self.phone is not None else 0
        flags |= (1 << 5) if self.photo is not None else 0
        flags |= (1 << 6) if self.status is not None else 0
        flags |= (1 << 14) if self.bot_info_version is not None else 0
        flags |= (1 << 18) if self.restriction_reason is not None else 0
        flags |= (1 << 19) if self.bot_inline_placeholder is not None else 0
        flags |= (1 << 22) if self.lang_code is not None else 0
        data.write(Int(flags))
        
        data.write(self.flags2.write())
        
        data.write(self.eFlags.write())
        
        data.write(Long(self.id))
        
        if self.access_hash is not None:
            data.write(Long(self.access_hash))
        
        if self.first_name is not None:
            data.write(String(self.first_name))
        
        if self.last_name is not None:
            data.write(String(self.last_name))
        
        if self.username is not None:
            data.write(String(self.username))
        
        if self.phone is not None:
            data.write(String(self.phone))
        
        if self.photo is not None:
            data.write(self.photo.write())
        
        if self.status is not None:
            data.write(self.status.write())
        
        if self.bot_info_version is not None:
            data.write(Int(self.bot_info_version))
        
        if self.restriction_reason is not None:
            data.write(Vector(self.restriction_reason))
        
        if self.bot_inline_placeholder is not None:
            data.write(String(self.bot_inline_placeholder))
        
        if self.lang_code is not None:
            data.write(String(self.lang_code))
        
        data.write(self.miniApp.write())
        
        data.write(self.badge_name.write())
        
        data.write(self.badge_red_color.write())
        
        data.write(self.miniAppGeo.write())
        
        data.write(self.bot_active_users.write())
        
        return data.getvalue()
