from .flags import *
from .v8_svg_text_content_element import SVGTextContentElement


@construct_100001
class SVGTextPositioningElement(SVGTextContentElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGTextPositioningElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("dx", "get_dx", None, 0, 1, 0, 0, 0, 0, 1),
        ("dy", "get_dy", None, 0, 1, 0, 0, 0, 0, 1),
        ("rotate", "get_rotate", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_positioning_element.py -> SVGTextPositioningElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_positioning_element.py -> SVGTextPositioningElement.y -> get attr')

    def get_dx(self):
        val = self._attr.get('dx')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_positioning_element.py -> SVGTextPositioningElement.dx -> get attr')

    def get_dy(self):
        val = self._attr.get('dy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_positioning_element.py -> SVGTextPositioningElement.dy -> get attr')

    def get_rotate(self):
        val = self._attr.get('rotate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_positioning_element.py -> SVGTextPositioningElement.rotate -> get attr')
