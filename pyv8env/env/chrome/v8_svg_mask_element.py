from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGMaskElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGMaskElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("maskUnits", "get_maskUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("maskContentUnits", "get_maskContentUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("requiredExtensions", "get_requiredExtensions", None, 0, 1, 0, 0, 0, 0, 1),
        ("systemLanguage", "get_systemLanguage", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_maskUnits(self):
        val = self._attr.get('maskUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.maskUnits -> get attr')

    def get_maskContentUnits(self):
        val = self._attr.get('maskContentUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.maskContentUnits -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.height -> get attr')

    def get_requiredExtensions(self):
        val = self._attr.get('requiredExtensions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.requiredExtensions -> get attr')

    def get_systemLanguage(self):
        val = self._attr.get('systemLanguage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_mask_element.py -> SVGMaskElement.systemLanguage -> get attr')
