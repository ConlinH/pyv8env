from .flags import *


@construct_000000
class WebGLCompressedTextureETC1:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_RGB_ETC1_WEBGL = 36196
