from .flags import *


@construct_000000
class OESShaderMultisampleInterpolation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    MIN_FRAGMENT_INTERPOLATION_OFFSET_OES = 36443
    MAX_FRAGMENT_INTERPOLATION_OFFSET_OES = 36444
    FRAGMENT_INTERPOLATION_OFFSET_BITS_OES = 36445
