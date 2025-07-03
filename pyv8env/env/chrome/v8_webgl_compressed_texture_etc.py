from .flags import *


@construct_000000
class WebGLCompressedTextureETC:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_R11_EAC = 37488
    COMPRESSED_SIGNED_R11_EAC = 37489
    COMPRESSED_RG11_EAC = 37490
    COMPRESSED_SIGNED_RG11_EAC = 37491
    COMPRESSED_RGB8_ETC2 = 37492
    COMPRESSED_SRGB8_ETC2 = 37493
    COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 37494
    COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 37495
    COMPRESSED_RGBA8_ETC2_EAC = 37496
    COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 37497
