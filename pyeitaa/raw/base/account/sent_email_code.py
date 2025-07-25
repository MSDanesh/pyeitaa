from typing import Union
from pyeitaa import raw

SentEmailCode = Union[raw.types.account.SentEmailCode]


# noinspection PyRedeclaration
class SentEmailCode:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`account.SentEmailCode <pyeitaa.raw.types.account.SentEmailCode>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.SendVerifyEmailCode <pyeitaa.raw.functions.account.SendVerifyEmailCode>`
    """

    QUALNAME = "pyeitaa.raw.base.account.SentEmailCode"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
