from .flags import *
from .v8_svg_gradient_element import SVGGradientElement


@construct_100001
class SVGRadialGradientElement(SVGGradientElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGRadialGradientElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("cx", "get_cx", None, 0, 1, 0, 0, 0, 0, 1),
        ("cy", "get_cy", None, 0, 1, 0, 0, 0, 0, 1),
        ("r", "get_r", None, 0, 1, 0, 0, 0, 0, 1),
        ("fx", "get_fx", None, 0, 1, 0, 0, 0, 0, 1),
        ("fy", "get_fy", None, 0, 1, 0, 0, 0, 0, 1),
        ("fr", "get_fr", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_cx(self):
        val = self._attr.get('cx')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_radial_gradient_element.py -> SVGRadialGradientElement.cx -> get attr')

    def get_cy(self):
        val = self._attr.get('cy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_radial_gradient_element.py -> SVGRadialGradientElement.cy -> get attr')

    def get_r(self):
        val = self._attr.get('r')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_radial_gradient_element.py -> SVGRadialGradientElement.r -> get attr')

    def get_fx(self):
        val = self._attr.get('fx')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_radial_gradient_element.py -> SVGRadialGradientElement.fx -> get attr')

    def get_fy(self):
        val = self._attr.get('fy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_radial_gradient_element.py -> SVGRadialGradientElement.fy -> get attr')

    def get_fr(self):
        val = self._attr.get('fr')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_radial_gradient_element.py -> SVGRadialGradientElement.fr -> get attr')
