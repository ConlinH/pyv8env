from .flags import *
from .v8_css_color_value import CSSColorValue


@construct_113001
class CSSHWB(CSSColorValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSHWB, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("h", "get_h", "set_h", 0, 1, 0, 0, 0, 0, 1),
        ("w", "get_w", "set_w", 0, 1, 0, 0, 0, 0, 1),
        ("b", "get_b", "set_b", 0, 1, 0, 0, 0, 0, 1),
        ("alpha", "get_alpha", "set_alpha", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_h(self):
        val = self._attr.get('h')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hwb.py -> CSSHWB.h -> get attr')

    def set_h(self, val):
        self._attr['h'] = val

    def get_w(self):
        val = self._attr.get('w')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hwb.py -> CSSHWB.w -> get attr')

    def set_w(self, val):
        self._attr['w'] = val

    def get_b(self):
        val = self._attr.get('b')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hwb.py -> CSSHWB.b -> get attr')

    def set_b(self, val):
        self._attr['b'] = val

    def get_alpha(self):
        val = self._attr.get('alpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hwb.py -> CSSHWB.alpha -> get attr')

    def set_alpha(self, val):
        self._attr['alpha'] = val
