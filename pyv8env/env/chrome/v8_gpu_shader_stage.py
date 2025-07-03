from .flags import *


@construct_100001
class GPUShaderStage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    VERTEX = 1
    FRAGMENT = 2
    COMPUTE = 4
