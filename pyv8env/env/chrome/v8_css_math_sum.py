from .flags import *
from .v8_css_math_value import CSSMathValue


@construct_110001
class CSSMathSum(CSSMathValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSMathSum, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("values", "get_values", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_values(self):
        val = self._attr.get('values')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_math_sum.py -> CSSMathSum.values -> get attr')
