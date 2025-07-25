from typing import Union
from pyeitaa import raw

VideoSize = Union[raw.types.VideoSize]


# noinspection PyRedeclaration
class VideoSize:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`VideoSize <pyeitaa.raw.types.VideoSize>`
    """

    QUALNAME = "pyeitaa.raw.base.VideoSize"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
