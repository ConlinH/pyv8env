from .flags import *


@construct_100001
class GPUBufferUsage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    MAP_READ = 1
    MAP_WRITE = 2
    COPY_SRC = 4
    COPY_DST = 8
    INDEX = 16
    VERTEX = 32
    UNIFORM = 64
    STORAGE = 128
    INDIRECT = 256
    QUERY_RESOLVE = 512
