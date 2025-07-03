from .flags import *
from .v8_css_color_value import CSSColorValue


@construct_113001
class CSSRGB(CSSColorValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSRGB, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("r", "get_r", "set_r", 0, 1, 0, 0, 0, 0, 1),
        ("g", "get_g", "set_g", 0, 1, 0, 0, 0, 0, 1),
        ("b", "get_b", "set_b", 0, 1, 0, 0, 0, 0, 1),
        ("alpha", "get_alpha", "set_alpha", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_r(self):
        val = self._attr.get('r')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rgb.py -> CSSRGB.r -> get attr')

    def set_r(self, val):
        self._attr['r'] = val

    def get_g(self):
        val = self._attr.get('g')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rgb.py -> CSSRGB.g -> get attr')

    def set_g(self, val):
        self._attr['g'] = val

    def get_b(self):
        val = self._attr.get('b')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rgb.py -> CSSRGB.b -> get attr')

    def set_b(self, val):
        self._attr['b'] = val

    def get_alpha(self):
        val = self._attr.get('alpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rgb.py -> CSSRGB.alpha -> get attr')

    def set_alpha(self, val):
        self._attr['alpha'] = val
