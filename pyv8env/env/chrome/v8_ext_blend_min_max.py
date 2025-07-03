from .flags import *


@construct_000000
class EXTBlendMinMax:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    MIN_EXT = 32775
    MAX_EXT = 32776
