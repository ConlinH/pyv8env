from .flags import *
from .v8_svg_graphics_element import SVGGraphicsElement


@construct_100001
class SVGGeometryElement(SVGGraphicsElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGGeometryElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("pathLength", "get_pathLength", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPointAtLength", "fn_getPointAtLength", 1, 0, 1, 0, 0, 0, 0),
        ("getTotalLength", "fn_getTotalLength", 0, 0, 1, 0, 0, 0, 0),
        ("isPointInFill", "fn_isPointInFill", 1, 0, 1, 0, 0, 0, 0),
        ("isPointInStroke", "fn_isPointInStroke", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_pathLength(self):
        val = self._attr.get('pathLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_geometry_element.py -> SVGGeometryElement.pathLength -> get attr')

    def fn_getPointAtLength(self, *args):
        logger.debug(f'patch -> v8_svg_geometry_element.py -> SVGGeometryElement.getPointAtLength{tuple(args)} -> method')

    def fn_getTotalLength(self, *args):
        logger.debug(f'patch -> v8_svg_geometry_element.py -> SVGGeometryElement.getTotalLength{tuple(args)} -> method')

    def fn_isPointInFill(self, *args):
        logger.debug(f'patch -> v8_svg_geometry_element.py -> SVGGeometryElement.isPointInFill{tuple(args)} -> method')

    def fn_isPointInStroke(self, *args):
        logger.debug(f'patch -> v8_svg_geometry_element.py -> SVGGeometryElement.isPointInStroke{tuple(args)} -> method')
