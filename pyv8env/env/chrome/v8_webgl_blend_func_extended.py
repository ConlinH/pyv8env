from .flags import *


@construct_000000
class WebGLBlendFuncExtended:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    SRC1_COLOR_WEBGL = 35065
    SRC1_ALPHA_WEBGL = 34185
    ONE_MINUS_SRC1_COLOR_WEBGL = 35066
    ONE_MINUS_SRC1_ALPHA_WEBGL = 35067
    MAX_DUAL_SOURCE_DRAW_BUFFERS_WEBGL = 35068
