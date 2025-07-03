from .flags import *


@construct_000000
class EXTsRGB:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    SRGB_EXT = 35904
    SRGB_ALPHA_EXT = 35906
    SRGB8_ALPHA8_EXT = 35907
    FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT = 33296
