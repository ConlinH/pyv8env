from .flags import *


@construct_100001
class Translation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("canTranslate", "fn_canTranslate", 1, 0, 1, 0, 1, 0, 0),
        ("createTranslator", "fn_createTranslator", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_canTranslate(self, *args):
        logger.debug(f'patch -> v8_translation.py -> Translation.canTranslate{tuple(args)} -> method')

    def fn_createTranslator(self, *args):
        logger.debug(f'patch -> v8_translation.py -> Translation.createTranslator{tuple(args)} -> method')
