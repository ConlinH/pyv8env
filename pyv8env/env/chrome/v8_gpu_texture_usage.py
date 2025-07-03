from .flags import *


@construct_100001
class GPUTextureUsage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COPY_SRC = 1
    COPY_DST = 2
    TEXTURE_BINDING = 4
    STORAGE_BINDING = 8
    RENDER_ATTACHMENT = 16
