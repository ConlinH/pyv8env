from .flags import *


@construct_100001
class CSSStyleValue:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),
        ("parse", "fn_parse", 2, 0, 2, 0, 1, 1, 0),
        ("parseAll", "fn_parseAll", 2, 0, 2, 0, 1, 1, 0),

    )

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_css_style_value.py -> CSSStyleValue.toString{tuple(args)} -> method')

    @classmethod
    def fn_parse(cls, *args):
        logger.debug(f'patch -> v8_css_style_value.py -> CSSStyleValue.parse{tuple(args)} -> method')

    @classmethod
    def fn_parseAll(cls, *args):
        logger.debug(f'patch -> v8_css_style_value.py -> CSSStyleValue.parseAll{tuple(args)} -> method')
