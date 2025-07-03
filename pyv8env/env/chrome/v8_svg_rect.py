from .flags import *


@construct_100001
class SVGRect:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", "set_x", 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", "set_y", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_rect.py -> SVGRect.x -> get attr')

    def set_x(self, val):
        self._attr['x'] = val

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_rect.py -> SVGRect.y -> get attr')

    def set_y(self, val):
        self._attr['y'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_rect.py -> SVGRect.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_rect.py -> SVGRect.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val
