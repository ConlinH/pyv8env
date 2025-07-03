from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGGradientElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGGradientElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("gradientUnits", "get_gradientUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("gradientTransform", "get_gradientTransform", None, 0, 1, 0, 0, 0, 0, 1),
        ("spreadMethod", "get_spreadMethod", None, 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_gradientUnits(self):
        val = self._attr.get('gradientUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_gradient_element.py -> SVGGradientElement.gradientUnits -> get attr')

    def get_gradientTransform(self):
        val = self._attr.get('gradientTransform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_gradient_element.py -> SVGGradientElement.gradientTransform -> get attr')

    def get_spreadMethod(self):
        val = self._attr.get('spreadMethod')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_gradient_element.py -> SVGGradientElement.spreadMethod -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_gradient_element.py -> SVGGradientElement.href -> get attr')
