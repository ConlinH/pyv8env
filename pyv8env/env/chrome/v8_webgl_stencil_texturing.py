from .flags import *


@construct_000000
class WebGLStencilTexturing:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    DEPTH_STENCIL_TEXTURE_MODE_WEBGL = 37098
    STENCIL_INDEX_WEBGL = 6401
