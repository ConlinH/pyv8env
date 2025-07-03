from .flags import *


@construct_000000
class EXTDepthClamp:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    DEPTH_CLAMP_EXT = 34383
