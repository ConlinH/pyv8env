from .flags import *


@construct_100001
class NavigationPreloadManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("disable", "fn_disable", 0, 0, 1, 0, 1, 0, 0),
        ("enable", "fn_enable", 0, 0, 1, 0, 1, 0, 0),
        ("getState", "fn_getState", 0, 0, 1, 0, 1, 0, 0),
        ("setHeaderValue", "fn_setHeaderValue", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_disable(self, *args):
        logger.debug(f'patch -> v8_navigation_preload_manager.py -> NavigationPreloadManager.disable{tuple(args)} -> method')

    def fn_enable(self, *args):
        logger.debug(f'patch -> v8_navigation_preload_manager.py -> NavigationPreloadManager.enable{tuple(args)} -> method')

    def fn_getState(self, *args):
        logger.debug(f'patch -> v8_navigation_preload_manager.py -> NavigationPreloadManager.getState{tuple(args)} -> method')

    def fn_setHeaderValue(self, *args):
        logger.debug(f'patch -> v8_navigation_preload_manager.py -> NavigationPreloadManager.setHeaderValue{tuple(args)} -> method')
