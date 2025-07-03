from .flags import *
from .v8_css_numeric_value import CSSNumericValue


@construct_100001
class CSSMathValue(CSSNumericValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSMathValue, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("operator", "get_operator", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_operator(self):
        val = self._attr.get('operator')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_math_value.py -> CSSMathValue.operator -> get attr')
