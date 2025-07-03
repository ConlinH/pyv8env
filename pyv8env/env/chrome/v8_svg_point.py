from .flags import *


@construct_100001
class SVGPoint:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", "set_x", 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", "set_y", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("matrixTransform", "fn_matrixTransform", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_point.py -> SVGPoint.x -> get attr')

    def set_x(self, val):
        self._attr['x'] = val

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_point.py -> SVGPoint.y -> get attr')

    def set_y(self, val):
        self._attr['y'] = val

    def fn_matrixTransform(self, *args):
        logger.debug(f'patch -> v8_svg_point.py -> SVGPoint.matrixTransform{tuple(args)} -> method')
