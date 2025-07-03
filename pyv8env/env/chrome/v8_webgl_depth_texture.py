from .flags import *


@construct_000000
class WebGLDepthTexture:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    UNSIGNED_INT_24_8_WEBGL = 34042
