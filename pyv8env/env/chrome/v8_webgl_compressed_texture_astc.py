from .flags import *


@construct_000000
class WebGLCompressedTextureASTC:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPRESSED_RGBA_ASTC_4x4_KHR = 37808
    COMPRESSED_RGBA_ASTC_5x4_KHR = 37809
    COMPRESSED_RGBA_ASTC_5x5_KHR = 37810
    COMPRESSED_RGBA_ASTC_6x5_KHR = 37811
    COMPRESSED_RGBA_ASTC_6x6_KHR = 37812
    COMPRESSED_RGBA_ASTC_8x5_KHR = 37813
    COMPRESSED_RGBA_ASTC_8x6_KHR = 37814
    COMPRESSED_RGBA_ASTC_8x8_KHR = 37815
    COMPRESSED_RGBA_ASTC_10x5_KHR = 37816
    COMPRESSED_RGBA_ASTC_10x6_KHR = 37817
    COMPRESSED_RGBA_ASTC_10x8_KHR = 37818
    COMPRESSED_RGBA_ASTC_10x10_KHR = 37819
    COMPRESSED_RGBA_ASTC_12x10_KHR = 37820
    COMPRESSED_RGBA_ASTC_12x12_KHR = 37821
    COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR = 37840
    COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR = 37841
    COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR = 37842
    COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR = 37843
    COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR = 37844
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR = 37845
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR = 37846
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR = 37847
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR = 37848
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR = 37849
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR = 37850
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR = 37851
    COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR = 37852
    COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR = 37853

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getSupportedProfiles", "fn_getSupportedProfiles", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_getSupportedProfiles(self, *args):
        logger.debug(f'patch -> v8_webgl_compressed_texture_astc.py -> WebGLCompressedTextureASTC.getSupportedProfiles{tuple(args)} -> method')
