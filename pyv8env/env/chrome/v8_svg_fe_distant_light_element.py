from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFEDistantLightElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFEDistantLightElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("azimuth", "get_azimuth", None, 0, 1, 0, 0, 0, 0, 1),
        ("elevation", "get_elevation", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_azimuth(self):
        val = self._attr.get('azimuth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_distant_light_element.py -> SVGFEDistantLightElement.azimuth -> get attr')

    def get_elevation(self):
        val = self._attr.get('elevation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_distant_light_element.py -> SVGFEDistantLightElement.elevation -> get attr')
