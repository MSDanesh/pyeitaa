from typing import Union
from pyeitaa import raw

StatsPercentValue = Union[raw.types.StatsPercentValue]


# noinspection PyRedeclaration
class StatsPercentValue:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`StatsPercentValue <pyeitaa.raw.types.StatsPercentValue>`
    """

    QUALNAME = "pyeitaa.raw.base.StatsPercentValue"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
