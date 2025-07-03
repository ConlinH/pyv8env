from .flags import *


@construct_100001
class LanguageTranslator:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("translate", "fn_translate", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_translate(self, *args):
        logger.debug(f'patch -> v8_language_translator.py -> LanguageTranslator.translate{tuple(args)} -> method')
