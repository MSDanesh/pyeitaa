from typing import Union
from pyeitaa import raw

CdnPublicKey = Union[raw.types.CdnPublicKey]


# noinspection PyRedeclaration
class CdnPublicKey:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`CdnPublicKey <pyeitaa.raw.types.CdnPublicKey>`
    """

    QUALNAME = "pyeitaa.raw.base.CdnPublicKey"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
