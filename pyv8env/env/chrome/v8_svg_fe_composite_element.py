from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFECompositeElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFECompositeElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("in2", "get_in2", None, 0, 1, 0, 0, 0, 0, 1),
        ("in1", "get_in1", None, 0, 1, 0, 0, 0, 0, 1),
        ("operator", "get_operator", None, 0, 1, 0, 0, 0, 0, 1),
        ("k1", "get_k1", None, 0, 1, 0, 0, 0, 0, 1),
        ("k2", "get_k2", None, 0, 1, 0, 0, 0, 0, 1),
        ("k3", "get_k3", None, 0, 1, 0, 0, 0, 0, 1),
        ("k4", "get_k4", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_in2(self):
        val = self._attr.get('in2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.in2 -> get attr')

    def get_in1(self):
        val = self._attr.get('in1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.in1 -> get attr')

    def get_operator(self):
        val = self._attr.get('operator')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.operator -> get attr')

    def get_k1(self):
        val = self._attr.get('k1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.k1 -> get attr')

    def get_k2(self):
        val = self._attr.get('k2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.k2 -> get attr')

    def get_k3(self):
        val = self._attr.get('k3')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.k3 -> get attr')

    def get_k4(self):
        val = self._attr.get('k4')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.k4 -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_composite_element.py -> SVGFECompositeElement.result -> get attr')
