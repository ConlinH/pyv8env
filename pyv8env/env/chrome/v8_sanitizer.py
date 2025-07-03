from .flags import *


@construct_110001
class Sanitizer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getConfiguration", "fn_getConfiguration", 0, 0, 1, 0, 0, 0, 0),
        ("sanitize", "fn_sanitize", 1, 0, 1, 0, 0, 0, 0),
        ("sanitizeFor", "fn_sanitizeFor", 2, 0, 1, 0, 0, 0, 0),
        ("getDefaultConfiguration", "fn_getDefaultConfiguration", 0, 0, 2, 0, 1, 1, 0),

    )

    def fn_getConfiguration(self, *args):
        logger.debug(f'patch -> v8_sanitizer.py -> Sanitizer.getConfiguration{tuple(args)} -> method')

    def fn_sanitize(self, *args):
        logger.debug(f'patch -> v8_sanitizer.py -> Sanitizer.sanitize{tuple(args)} -> method')

    def fn_sanitizeFor(self, *args):
        logger.debug(f'patch -> v8_sanitizer.py -> Sanitizer.sanitizeFor{tuple(args)} -> method')

    @classmethod
    def fn_getDefaultConfiguration(cls, *args):
        logger.debug(f'patch -> v8_sanitizer.py -> Sanitizer.getDefaultConfiguration{tuple(args)} -> method')
