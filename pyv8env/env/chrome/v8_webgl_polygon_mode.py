from .flags import *


@construct_000000
class WebGLPolygonMode:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    POLYGON_MODE_WEBGL = 2880
    POLYGON_OFFSET_LINE_WEBGL = 10754
    LINE_WEBGL = 6913
    FILL_WEBGL = 6914

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("polygonModeWEBGL", "fn_polygonModeWEBGL", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_polygonModeWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_polygon_mode.py -> WebGLPolygonMode.polygonModeWEBGL{tuple(args)} -> method')
