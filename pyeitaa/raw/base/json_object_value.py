from typing import Union
from pyeitaa import raw

JSONObjectValue = Union[raw.types.JsonObjectValue]


# noinspection PyRedeclaration
class JSONObjectValue:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`JsonObjectValue <pyeitaa.raw.types.JsonObjectValue>`
    """

    QUALNAME = "pyeitaa.raw.base.JSONObjectValue"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
