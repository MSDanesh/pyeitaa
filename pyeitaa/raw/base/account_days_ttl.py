from typing import Union
from pyeitaa import raw

AccountDaysTTL = Union[raw.types.AccountDaysTTL]


# noinspection PyRedeclaration
class AccountDaysTTL:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`AccountDaysTTL <pyeitaa.raw.types.AccountDaysTTL>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetAccountTTL <pyeitaa.raw.functions.account.GetAccountTTL>`
    """

    QUALNAME = "pyeitaa.raw.base.AccountDaysTTL"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
