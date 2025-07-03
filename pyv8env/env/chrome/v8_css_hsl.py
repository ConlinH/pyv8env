from .flags import *
from .v8_css_color_value import CSSColorValue


@construct_113001
class CSSHSL(CSSColorValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSHSL, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("h", "get_h", "set_h", 0, 1, 0, 0, 0, 0, 1),
        ("s", "get_s", "set_s", 0, 1, 0, 0, 0, 0, 1),
        ("l", "get_l", "set_l", 0, 1, 0, 0, 0, 0, 1),
        ("alpha", "get_alpha", "set_alpha", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_h(self):
        val = self._attr.get('h')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hsl.py -> CSSHSL.h -> get attr')

    def set_h(self, val):
        self._attr['h'] = val

    def get_s(self):
        val = self._attr.get('s')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hsl.py -> CSSHSL.s -> get attr')

    def set_s(self, val):
        self._attr['s'] = val

    def get_l(self):
        val = self._attr.get('l')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hsl.py -> CSSHSL.l -> get attr')

    def set_l(self, val):
        self._attr['l'] = val

    def get_alpha(self):
        val = self._attr.get('alpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_hsl.py -> CSSHSL.alpha -> get attr')

    def set_alpha(self, val):
        self._attr['alpha'] = val
