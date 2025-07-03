from .flags import *


@construct_000000
class EXTPolygonOffsetClamp:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    POLYGON_OFFSET_CLAMP_EXT = 36379

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("polygonOffsetClampEXT", "fn_polygonOffsetClampEXT", 3, 0, 1, 0, 0, 0, 0),

    )

    def fn_polygonOffsetClampEXT(self, *args):
        logger.debug(f'patch -> v8_ext_polygon_offset_clamp.py -> EXTPolygonOffsetClamp.polygonOffsetClampEXT{tuple(args)} -> method')
