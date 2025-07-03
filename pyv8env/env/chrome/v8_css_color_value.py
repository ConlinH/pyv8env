from .flags import *


@construct_100001
class CSSColorValue:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toHSL", "fn_toHSL", 0, 0, 1, 0, 0, 0, 0),
        ("toHWB", "fn_toHWB", 0, 0, 1, 0, 0, 0, 0),
        ("toRGB", "fn_toRGB", 0, 0, 1, 0, 0, 0, 0),
        ("parse", "fn_parse", 1, 0, 2, 0, 1, 1, 0),

    )

    def fn_toHSL(self, *args):
        logger.debug(f'patch -> v8_css_color_value.py -> CSSColorValue.toHSL{tuple(args)} -> method')

    def fn_toHWB(self, *args):
        logger.debug(f'patch -> v8_css_color_value.py -> CSSColorValue.toHWB{tuple(args)} -> method')

    def fn_toRGB(self, *args):
        logger.debug(f'patch -> v8_css_color_value.py -> CSSColorValue.toRGB{tuple(args)} -> method')

    @classmethod
    def fn_parse(cls, *args):
        logger.debug(f'patch -> v8_css_color_value.py -> CSSColorValue.parse{tuple(args)} -> method')
