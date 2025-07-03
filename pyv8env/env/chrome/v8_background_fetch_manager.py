from .flags import *


@construct_100001
class BackgroundFetchManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("fetch", "fn_fetch", 2, 0, 1, 0, 1, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 1, 0, 0),
        ("getIds", "fn_getIds", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_fetch(self, *args):
        logger.debug(f'patch -> v8_background_fetch_manager.py -> BackgroundFetchManager.fetch{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_background_fetch_manager.py -> BackgroundFetchManager.get{tuple(args)} -> method')

    def fn_getIds(self, *args):
        logger.debug(f'patch -> v8_background_fetch_manager.py -> BackgroundFetchManager.getIds{tuple(args)} -> method')
