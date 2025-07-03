from .flags import *
from .v8_css_math_value import CSSMathValue


@construct_113001
class CSSMathClamp(CSSMathValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSMathClamp, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("lower", "get_lower", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", None, 0, 1, 0, 0, 0, 0, 1),
        ("upper", "get_upper", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_lower(self):
        val = self._attr.get('lower')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_math_clamp.py -> CSSMathClamp.lower -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_math_clamp.py -> CSSMathClamp.value -> get attr')

    def get_upper(self):
        val = self._attr.get('upper')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_math_clamp.py -> CSSMathClamp.upper -> get attr')
