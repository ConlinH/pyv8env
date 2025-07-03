from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFEBlendElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFEBlendElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("in1", "get_in1", None, 0, 1, 0, 0, 0, 0, 1),
        ("in2", "get_in2", None, 0, 1, 0, 0, 0, 0, 1),
        ("mode", "get_mode", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_in1(self):
        val = self._attr.get('in1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.in1 -> get attr')

    def get_in2(self):
        val = self._attr.get('in2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.in2 -> get attr')

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.mode -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_blend_element.py -> SVGFEBlendElement.result -> get attr')
