from .flags import *


@construct_000000
class WebGLCompressedTextureS3TC:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_RGB_S3TC_DXT1_EXT = 33776
    COMPRESSED_RGBA_S3TC_DXT1_EXT = 33777
    COMPRESSED_RGBA_S3TC_DXT3_EXT = 33778
    COMPRESSED_RGBA_S3TC_DXT5_EXT = 33779
