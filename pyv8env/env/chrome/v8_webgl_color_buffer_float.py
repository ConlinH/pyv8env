from .flags import *


@construct_000000
class WebGLColorBufferFloat:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    RGBA32F_EXT = 34836
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT = 33297
    UNSIGNED_NORMALIZED_EXT = 35863
