from io import BytesIO

from pyeitaa.raw.core.primitives import Int
from pyeitaa.raw.core import TLObject
from pyeitaa import raw
from typing import List, Optional, Any, Self


class BotInlineMessageMediaGeo(TLObject):
    """This object is a constructor of the base type :obj:`~pyeitaa.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``135``
        - ID: ``0x51846fd``

    Parameters:
        geo: :obj:`GeoPoint <pyeitaa.raw.base.GeoPoint>`
        heading (optional): ``int`` ``32-bit``
        period (optional): ``int`` ``32-bit``
        proximity_notification_radius (optional): ``int`` ``32-bit``
        reply_markup (optional): :obj:`ReplyMarkup <pyeitaa.raw.base.ReplyMarkup>`
    """

    __slots__: List[str] = ["geo", "heading", "period", "proximity_notification_radius", "reply_markup"]

    ID = 0x51846fd
    QUALNAME = "types.BotInlineMessageMediaGeo"

    def __init__(self, *, geo: "raw.base.GeoPoint", heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.geo = geo  # GeoPoint
        self.heading = heading  # flags.0?int
        self.period = period  # flags.1?int
        self.proximity_notification_radius = proximity_notification_radius  # flags.3?int
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Self:
        flags = Int.read(data)
        
        geo = TLObject.read(data)
        
        heading = Int.read(data) if flags & (1 << 0) else None
        period = Int.read(data) if flags & (1 << 1) else None
        proximity_notification_radius = Int.read(data) if flags & (1 << 3) else None
        reply_markup = TLObject.read(data) if flags & (1 << 2) else None
        
        return BotInlineMessageMediaGeo(geo=geo, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius, reply_markup=reply_markup)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID))

        flags = 0
        flags |= (1 << 0) if self.heading is not None else 0
        flags |= (1 << 1) if self.period is not None else 0
        flags |= (1 << 3) if self.proximity_notification_radius is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        data.write(Int(flags))
        
        data.write(self.geo.write())
        
        if self.heading is not None:
            data.write(Int(self.heading))
        
        if self.period is not None:
            data.write(Int(self.period))
        
        if self.proximity_notification_radius is not None:
            data.write(Int(self.proximity_notification_radius))
        
        if self.reply_markup is not None:
            data.write(self.reply_markup.write())
        
        return data.getvalue()
