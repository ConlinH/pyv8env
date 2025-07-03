from .flags import *


@construct_000000
class WebGLCompressedTextureS3TCsRGB:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_SRGB_S3TC_DXT1_EXT = 35916
    COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT = 35917
    COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT = 35918
    COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT = 35919
