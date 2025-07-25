from typing import Union
from pyeitaa import raw

CdnConfig = Union[raw.types.CdnConfig]


# noinspection PyRedeclaration
class CdnConfig:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`CdnConfig <pyeitaa.raw.types.CdnConfig>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`help.GetCdnConfig <pyeitaa.raw.functions.help.GetCdnConfig>`
    """

    QUALNAME = "pyeitaa.raw.base.CdnConfig"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
