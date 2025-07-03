from .flags import *


@construct_100001
class AI:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("canCreateGenericSession", "fn_canCreateGenericSession", 0, 0, 1, 0, 1, 0, 0),
        ("canCreateTextSession", "fn_canCreateTextSession", 0, 0, 1, 0, 1, 0, 0),
        ("createGenericSession", "fn_createGenericSession", 0, 0, 1, 0, 1, 0, 0),
        ("createTextSession", "fn_createTextSession", 0, 0, 1, 0, 1, 0, 0),
        ("defaultGenericSessionOptions", "fn_defaultGenericSessionOptions", 0, 0, 1, 0, 1, 0, 0),
        ("defaultTextSessionOptions", "fn_defaultTextSessionOptions", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_canCreateGenericSession(self, *args):
        logger.debug(f'patch -> v8_ai.py -> AI.canCreateGenericSession{tuple(args)} -> method')

    def fn_canCreateTextSession(self, *args):
        logger.debug(f'patch -> v8_ai.py -> AI.canCreateTextSession{tuple(args)} -> method')

    def fn_createGenericSession(self, *args):
        logger.debug(f'patch -> v8_ai.py -> AI.createGenericSession{tuple(args)} -> method')

    def fn_createTextSession(self, *args):
        logger.debug(f'patch -> v8_ai.py -> AI.createTextSession{tuple(args)} -> method')

    def fn_defaultGenericSessionOptions(self, *args):
        logger.debug(f'patch -> v8_ai.py -> AI.defaultGenericSessionOptions{tuple(args)} -> method')

    def fn_defaultTextSessionOptions(self, *args):
        logger.debug(f'patch -> v8_ai.py -> AI.defaultTextSessionOptions{tuple(args)} -> method')
