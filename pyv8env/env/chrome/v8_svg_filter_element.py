from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFilterElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFilterElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("filterUnits", "get_filterUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("primitiveUnits", "get_primitiveUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_filterUnits(self):
        val = self._attr.get('filterUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_filter_element.py -> SVGFilterElement.filterUnits -> get attr')

    def get_primitiveUnits(self):
        val = self._attr.get('primitiveUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_filter_element.py -> SVGFilterElement.primitiveUnits -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_filter_element.py -> SVGFilterElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_filter_element.py -> SVGFilterElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_filter_element.py -> SVGFilterElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_filter_element.py -> SVGFilterElement.height -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_filter_element.py -> SVGFilterElement.href -> get attr')
