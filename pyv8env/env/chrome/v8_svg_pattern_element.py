from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGPatternElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGPatternElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("patternUnits", "get_patternUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("patternContentUnits", "get_patternContentUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("patternTransform", "get_patternTransform", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewBox", "get_viewBox", None, 0, 1, 0, 0, 0, 0, 1),
        ("preserveAspectRatio", "get_preserveAspectRatio", None, 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),
        ("requiredExtensions", "get_requiredExtensions", None, 0, 1, 0, 0, 0, 0, 1),
        ("systemLanguage", "get_systemLanguage", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_patternUnits(self):
        val = self._attr.get('patternUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.patternUnits -> get attr')

    def get_patternContentUnits(self):
        val = self._attr.get('patternContentUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.patternContentUnits -> get attr')

    def get_patternTransform(self):
        val = self._attr.get('patternTransform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.patternTransform -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.height -> get attr')

    def get_viewBox(self):
        val = self._attr.get('viewBox')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.viewBox -> get attr')

    def get_preserveAspectRatio(self):
        val = self._attr.get('preserveAspectRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.preserveAspectRatio -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.href -> get attr')

    def get_requiredExtensions(self):
        val = self._attr.get('requiredExtensions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.requiredExtensions -> get attr')

    def get_systemLanguage(self):
        val = self._attr.get('systemLanguage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_pattern_element.py -> SVGPatternElement.systemLanguage -> get attr')
