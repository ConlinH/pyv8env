from .flags import *
from .v8_css_style_value import CSSStyleValue


@construct_100001
class CSSNumericValue(CSSStyleValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSNumericValue, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 0, 0, 1, 0, 0, 0, 0),
        ("div", "fn_div", 0, 0, 1, 0, 0, 0, 0),
        ("equals", "fn_equals", 0, 0, 1, 0, 0, 0, 0),
        ("max", "fn_max", 0, 0, 1, 0, 0, 0, 0),
        ("min", "fn_min", 0, 0, 1, 0, 0, 0, 0),
        ("mul", "fn_mul", 0, 0, 1, 0, 0, 0, 0),
        ("sub", "fn_sub", 0, 0, 1, 0, 0, 0, 0),
        ("to", "fn_to", 1, 0, 1, 0, 0, 0, 0),
        ("toSum", "fn_toSum", 0, 0, 1, 0, 0, 0, 0),
        ("type", "fn_type", 0, 0, 1, 0, 0, 0, 0),
        ("parse", "fn_parse", 1, 0, 2, 0, 1, 1, 0),

    )

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.add{tuple(args)} -> method')

    def fn_div(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.div{tuple(args)} -> method')

    def fn_equals(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.equals{tuple(args)} -> method')

    def fn_max(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.max{tuple(args)} -> method')

    def fn_min(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.min{tuple(args)} -> method')

    def fn_mul(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.mul{tuple(args)} -> method')

    def fn_sub(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.sub{tuple(args)} -> method')

    def fn_to(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.to{tuple(args)} -> method')

    def fn_toSum(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.toSum{tuple(args)} -> method')

    def fn_type(self, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.type{tuple(args)} -> method')

    @classmethod
    def fn_parse(cls, *args):
        logger.debug(f'patch -> v8_css_numeric_value.py -> CSSNumericValue.parse{tuple(args)} -> method')
