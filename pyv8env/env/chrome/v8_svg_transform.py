from .flags import *


@construct_100001
class SVGTransform:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    SVG_TRANSFORM_UNKNOWN = 0
    SVG_TRANSFORM_MATRIX = 1
    SVG_TRANSFORM_TRANSLATE = 2
    SVG_TRANSFORM_SCALE = 3
    SVG_TRANSFORM_ROTATE = 4
    SVG_TRANSFORM_SKEWX = 5
    SVG_TRANSFORM_SKEWY = 6

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("matrix", "get_matrix", None, 0, 1, 0, 0, 0, 0, 1),
        ("angle", "get_angle", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setMatrix", "fn_setMatrix", 1, 0, 1, 0, 0, 0, 0),
        ("setRotate", "fn_setRotate", 3, 0, 1, 0, 0, 0, 0),
        ("setScale", "fn_setScale", 2, 0, 1, 0, 0, 0, 0),
        ("setSkewX", "fn_setSkewX", 1, 0, 1, 0, 0, 0, 0),
        ("setSkewY", "fn_setSkewY", 1, 0, 1, 0, 0, 0, 0),
        ("setTranslate", "fn_setTranslate", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.type -> get attr')

    def get_matrix(self):
        val = self._attr.get('matrix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.matrix -> get attr')

    def get_angle(self):
        val = self._attr.get('angle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.angle -> get attr')

    def fn_setMatrix(self, *args):
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.setMatrix{tuple(args)} -> method')

    def fn_setRotate(self, *args):
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.setRotate{tuple(args)} -> method')

    def fn_setScale(self, *args):
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.setScale{tuple(args)} -> method')

    def fn_setSkewX(self, *args):
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.setSkewX{tuple(args)} -> method')

    def fn_setSkewY(self, *args):
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.setSkewY{tuple(args)} -> method')

    def fn_setTranslate(self, *args):
        logger.debug(f'patch -> v8_svg_transform.py -> SVGTransform.setTranslate{tuple(args)} -> method')
