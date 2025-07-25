from typing import Union
from pyeitaa import raw

PollResults = Union[raw.types.PollResults]


# noinspection PyRedeclaration
class PollResults:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`PollResults <pyeitaa.raw.types.PollResults>`
    """

    QUALNAME = "pyeitaa.raw.base.PollResults"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
