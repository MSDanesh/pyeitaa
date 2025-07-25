from typing import Union
from pyeitaa import raw

PollAnswerVoters = Union[raw.types.PollAnswerVoters]


# noinspection PyRedeclaration
class PollAnswerVoters:
    """This base type has 1 constructor available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`PollAnswerVoters <pyeitaa.raw.types.PollAnswerVoters>`
    """

    QUALNAME = "pyeitaa.raw.base.PollAnswerVoters"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. ")
