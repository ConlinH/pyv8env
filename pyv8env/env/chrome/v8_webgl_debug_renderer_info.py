from .flags import *


@construct_000000
class WebGLDebugRendererInfo:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    UNMASKED_VENDOR_WEBGL = 37445
    UNMASKED_RENDERER_WEBGL = 37446
