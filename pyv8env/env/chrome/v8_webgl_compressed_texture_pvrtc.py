from .flags import *


@construct_000000
class WebGLCompressedTexturePVRTC:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 35840
    COMPRESSED_RGB_PVRTC_2BPPV1_IMG = 35841
    COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 35842
    COMPRESSED_RGBA_PVRTC_2BPPV1_IMG = 35843
