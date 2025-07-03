from .flags import *


@construct_000000
class EXTTextureNorm16:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    R16_EXT = 33322
    RG16_EXT = 33324
    RGB16_EXT = 32852
    RGBA16_EXT = 32859
    R16_SNORM_EXT = 36760
    RG16_SNORM_EXT = 36761
    RGB16_SNORM_EXT = 36762
    RGBA16_SNORM_EXT = 36763
