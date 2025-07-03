from .flags import *


@construct_100001
class GPUHeapProperty:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    DEVICE_LOCAL = 1
    HOST_VISIBLE = 2
    HOST_COHERENT = 4
    HOST_UNCACHED = 8
    HOST_CACHED = 16
