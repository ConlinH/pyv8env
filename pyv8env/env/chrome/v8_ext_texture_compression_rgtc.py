from .flags import *


@construct_000000
class EXTTextureCompressionRGTC:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_RED_RGTC1_EXT = 36283
    COMPRESSED_SIGNED_RED_RGTC1_EXT = 36284
    COMPRESSED_RED_GREEN_RGTC2_EXT = 36285
    COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT = 36286
