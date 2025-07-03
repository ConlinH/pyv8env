from .flags import *


@construct_000000
class EXTTextureCompressionBPTC:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_RGBA_BPTC_UNORM_EXT = 36492
    COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT = 36493
    COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT = 36494
    COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT = 36495
