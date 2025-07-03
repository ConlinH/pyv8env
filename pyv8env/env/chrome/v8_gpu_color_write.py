from .flags import *


@construct_100001
class GPUColorWrite:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    RED = 1
    GREEN = 2
    BLUE = 4
    ALPHA = 8
    ALL = 15
