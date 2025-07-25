from io import BytesIO

from pyeitaa.raw.core.primitives import Int, String
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Optional, Any, Self


class UserFull(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.UserFull`.

    Details:
        - Layer: ``135``
        - ID: ``-0x296800fb``

    Parameters:
        user: :obj:`User <pyeitaa.raw.base.User>`
        settings: :obj:`PeerSettings <pyeitaa.raw.base.PeerSettings>`
        notify_settings: :obj:`PeerNotifySettings <pyeitaa.raw.base.PeerNotifySettings>`
        common_chats_count: ``int`` ``32-bit``
        blocked (optional): ``bool``
        phone_calls_available (optional): ``bool``
        phone_calls_private (optional): ``bool``
        can_pin_message (optional): ``bool``
        has_scheduled (optional): ``bool``
        video_calls_available (optional): ``bool``
        about (optional): ``str``
        profile_photo (optional): :obj:`Photo <pyeitaa.raw.base.Photo>`
        bot_info (optional): :obj:`BotInfo <pyeitaa.raw.base.BotInfo>`
        pinned_msg_id (optional): ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``
        ttl_period (optional): ``int`` ``32-bit``
        theme_emoticon (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`users.GetFullUser <pyeitaa.raw.functions.users.GetFullUser>`
    """

    __slots__: List[str] = ["user", "settings", "notify_settings", "common_chats_count", "blocked", "phone_calls_available", "phone_calls_private", "can_pin_message", "has_scheduled", "video_calls_available", "about", "profile_photo", "bot_info", "pinned_msg_id", "folder_id", "ttl_period", "theme_emoticon"]

    ID = -0x296800fb
    QUALNAME = "types.UserFull"

    def __init__(self, *, user: "raw.base.User", settings: "raw.base.PeerSettings", notify_settings: "raw.base.PeerNotifySettings", common_chats_count: int, blocked: Optional[bool] = None, phone_calls_available: Optional[bool] = None, phone_calls_private: Optional[bool] = None, can_pin_message: Optional[bool] = None, has_scheduled: Optional[bool] = None, video_calls_available: Optional[bool] = None, about: Optional[str] = None, profile_photo: "raw.base.Photo" = None, bot_info: "raw.base.BotInfo" = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None, theme_emoticon: Optional[str] = None) -> None:
        self.user = user  # User
        self.settings = settings  # PeerSettings
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.common_chats_count = common_chats_count  # int
        self.blocked = blocked  # flags.0?true
        self.phone_calls_available = phone_calls_available  # flags.4?true
        self.phone_calls_private = phone_calls_private  # flags.5?true
        self.can_pin_message = can_pin_message  # flags.7?true
        self.has_scheduled = has_scheduled  # flags.12?true
        self.video_calls_available = video_calls_available  # flags.13?true
        self.about = about  # flags.1?string
        self.profile_photo = profile_photo  # flags.2?Photo
        self.bot_info = bot_info  # flags.3?BotInfo
        self.pinned_msg_id = pinned_msg_id  # flags.6?int
        self.folder_id = folder_id  # flags.11?int
        self.ttl_period = ttl_period  # flags.14?int
        self.theme_emoticon = theme_emoticon  # flags.15?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        flags = Int.read(data)
        
        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        can_pin_message = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 12) else False
        video_calls_available = True if flags & (1 << 13) else False
        user = TLObject.read(data)
        
        about = String.read(data) if flags & (1 << 1) else None
        settings = TLObject.read(data)
        
        profile_photo = TLObject.read(data) if flags & (1 << 2) else None
        
        notify_settings = TLObject.read(data)
        
        bot_info = TLObject.read(data) if flags & (1 << 3) else None
        
        pinned_msg_id = Int.read(data) if flags & (1 << 6) else None
        common_chats_count = Int.read(data)
        
        folder_id = Int.read(data) if flags & (1 << 11) else None
        ttl_period = Int.read(data) if flags & (1 << 14) else None
        theme_emoticon = String.read(data) if flags & (1 << 15) else None
        return UserFull(user=user, settings=settings, notify_settings=notify_settings, common_chats_count=common_chats_count, blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, video_calls_available=video_calls_available, about=about, profile_photo=profile_photo, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, ttl_period=ttl_period, theme_emoticon=theme_emoticon)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 4) if self.phone_calls_available else 0
        flags |= (1 << 5) if self.phone_calls_private else 0
        flags |= (1 << 7) if self.can_pin_message else 0
        flags |= (1 << 12) if self.has_scheduled else 0
        flags |= (1 << 13) if self.video_calls_available else 0
        flags |= (1 << 1) if self.about is not None else 0
        flags |= (1 << 2) if self.profile_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 14) if self.ttl_period is not None else 0
        flags |= (1 << 15) if self.theme_emoticon is not None else 0
        data.write(Int(flags))
        
        data.write(self.user.write())
        
        if self.about is not None:
            data.write(String(self.about))
        
        data.write(self.settings.write())
        
        if self.profile_photo is not None:
            data.write(self.profile_photo.write())
        
        data.write(self.notify_settings.write())
        
        if self.bot_info is not None:
            data.write(self.bot_info.write())
        
        if self.pinned_msg_id is not None:
            data.write(Int(self.pinned_msg_id))
        
        data.write(Int(self.common_chats_count))
        
        if self.folder_id is not None:
            data.write(Int(self.folder_id))
        
        if self.ttl_period is not None:
            data.write(Int(self.ttl_period))
        
        if self.theme_emoticon is not None:
            data.write(String(self.theme_emoticon))
        
        return data.getvalue()
