from .flags import *


@construct_000000
class EXTTextureMirrorClampToEdge:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    MIRROR_CLAMP_TO_EDGE_EXT = 34627
