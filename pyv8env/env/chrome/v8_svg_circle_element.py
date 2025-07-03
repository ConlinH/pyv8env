from .flags import *
from .v8_svg_geometry_element import SVGGeometryElement


@construct_100001
class SVGCircleElement(SVGGeometryElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGCircleElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("cx", "get_cx", None, 0, 1, 0, 0, 0, 0, 1),
        ("cy", "get_cy", None, 0, 1, 0, 0, 0, 0, 1),
        ("r", "get_r", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_cx(self):
        val = self._attr.get('cx')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_circle_element.py -> SVGCircleElement.cx -> get attr')

    def get_cy(self):
        val = self._attr.get('cy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_circle_element.py -> SVGCircleElement.cy -> get attr')

    def get_r(self):
        val = self._attr.get('r')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_circle_element.py -> SVGCircleElement.r -> get attr')
