from .flags import *
from .v8_svg_gradient_element import SVGGradientElement


@construct_100001
class SVGLinearGradientElement(SVGGradientElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGLinearGradientElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x1", "get_x1", None, 0, 1, 0, 0, 0, 0, 1),
        ("y1", "get_y1", None, 0, 1, 0, 0, 0, 0, 1),
        ("x2", "get_x2", None, 0, 1, 0, 0, 0, 0, 1),
        ("y2", "get_y2", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_x1(self):
        val = self._attr.get('x1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_linear_gradient_element.py -> SVGLinearGradientElement.x1 -> get attr')

    def get_y1(self):
        val = self._attr.get('y1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_linear_gradient_element.py -> SVGLinearGradientElement.y1 -> get attr')

    def get_x2(self):
        val = self._attr.get('x2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_linear_gradient_element.py -> SVGLinearGradientElement.x2 -> get attr')

    def get_y2(self):
        val = self._attr.get('y2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_linear_gradient_element.py -> SVGLinearGradientElement.y2 -> get attr')
