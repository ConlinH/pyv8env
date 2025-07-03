from .flags import *


@construct_000000
class WebGLClipCullDistance:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    MAX_CLIP_DISTANCES_WEBGL = 3378
    MAX_CULL_DISTANCES_WEBGL = 33529
    MAX_COMBINED_CLIP_AND_CULL_DISTANCES_WEBGL = 33530
    CLIP_DISTANCE0_WEBGL = 12288
    CLIP_DISTANCE1_WEBGL = 12289
    CLIP_DISTANCE2_WEBGL = 12290
    CLIP_DISTANCE3_WEBGL = 12291
    CLIP_DISTANCE4_WEBGL = 12292
    CLIP_DISTANCE5_WEBGL = 12293
    CLIP_DISTANCE6_WEBGL = 12294
    CLIP_DISTANCE7_WEBGL = 12295
