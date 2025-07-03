from .flags import *


@construct_000001
class LockScreenData:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("deleteData", "fn_deleteData", 1, 0, 1, 0, 1, 0, 0),
        ("getData", "fn_getData", 1, 0, 1, 0, 1, 0, 0),
        ("getKeys", "fn_getKeys", 0, 0, 1, 0, 1, 0, 0),
        ("setData", "fn_setData", 2, 0, 1, 0, 1, 0, 0),

    )

    def fn_deleteData(self, *args):
        logger.debug(f'patch -> v8_lock_screen_data.py -> LockScreenData.deleteData{tuple(args)} -> method')

    def fn_getData(self, *args):
        logger.debug(f'patch -> v8_lock_screen_data.py -> LockScreenData.getData{tuple(args)} -> method')

    def fn_getKeys(self, *args):
        logger.debug(f'patch -> v8_lock_screen_data.py -> LockScreenData.getKeys{tuple(args)} -> method')

    def fn_setData(self, *args):
        logger.debug(f'patch -> v8_lock_screen_data.py -> LockScreenData.setData{tuple(args)} -> method')
