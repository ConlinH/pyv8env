from .flags import *
from .v8_abstract_range import AbstractRange


@construct_111001
class StaticRange(AbstractRange):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(StaticRange, self).__init__(*args, **kw)
