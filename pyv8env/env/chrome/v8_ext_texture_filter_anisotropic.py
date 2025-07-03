from .flags import *


@construct_000000
class EXTTextureFilterAnisotropic:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    TEXTURE_MAX_ANISOTROPY_EXT = 34046
    MAX_TEXTURE_MAX_ANISOTROPY_EXT = 34047
