from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFESpotLightElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFESpotLightElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("z", "get_z", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointsAtX", "get_pointsAtX", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointsAtY", "get_pointsAtY", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointsAtZ", "get_pointsAtZ", None, 0, 1, 0, 0, 0, 0, 1),
        ("specularExponent", "get_specularExponent", None, 0, 1, 0, 0, 0, 0, 1),
        ("limitingConeAngle", "get_limitingConeAngle", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.y -> get attr')

    def get_z(self):
        val = self._attr.get('z')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.z -> get attr')

    def get_pointsAtX(self):
        val = self._attr.get('pointsAtX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.pointsAtX -> get attr')

    def get_pointsAtY(self):
        val = self._attr.get('pointsAtY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.pointsAtY -> get attr')

    def get_pointsAtZ(self):
        val = self._attr.get('pointsAtZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.pointsAtZ -> get attr')

    def get_specularExponent(self):
        val = self._attr.get('specularExponent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.specularExponent -> get attr')

    def get_limitingConeAngle(self):
        val = self._attr.get('limitingConeAngle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_spot_light_element.py -> SVGFESpotLightElement.limitingConeAngle -> get attr')
