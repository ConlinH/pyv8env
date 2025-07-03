from .flags import *


@construct_100001
class Keyboard:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getLayoutMap", "fn_getLayoutMap", 0, 0, 1, 0, 1, 0, 0),
        ("lock", "fn_lock", 0, 0, 1, 0, 1, 0, 0),
        ("unlock", "fn_unlock", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_getLayoutMap(self, *args):
        logger.debug(f'patch -> v8_keyboard.py -> Keyboard.getLayoutMap{tuple(args)} -> method')

    def fn_lock(self, *args):
        logger.debug(f'patch -> v8_keyboard.py -> Keyboard.lock{tuple(args)} -> method')

    def fn_unlock(self, *args):
        logger.debug(f'patch -> v8_keyboard.py -> Keyboard.unlock{tuple(args)} -> method')
