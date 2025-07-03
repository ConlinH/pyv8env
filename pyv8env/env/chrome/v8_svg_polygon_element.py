from .flags import *
from .v8_svg_geometry_element import SVGGeometryElement


@construct_100001
class SVGPolygonElement(SVGGeometryElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGPolygonElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("points", "get_points", None, 0, 1, 0, 0, 0, 0, 1),
        ("animatedPoints", "get_animatedPoints", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_points(self):
        val = self._attr.get('points')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_polygon_element.py -> SVGPolygonElement.points -> get attr')

    def get_animatedPoints(self):
        val = self._attr.get('animatedPoints')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_polygon_element.py -> SVGPolygonElement.animatedPoints -> get attr')
