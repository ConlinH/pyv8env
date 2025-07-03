from .flags import *


@construct_100001
class PeriodicSyncManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getTags", "fn_getTags", 0, 0, 1, 0, 1, 0, 0),
        ("register", "fn_register", 1, 0, 1, 0, 1, 0, 0),
        ("unregister", "fn_unregister", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_getTags(self, *args):
        logger.debug(f'patch -> v8_periodic_sync_manager.py -> PeriodicSyncManager.getTags{tuple(args)} -> method')

    def fn_register(self, *args):
        logger.debug(f'patch -> v8_periodic_sync_manager.py -> PeriodicSyncManager.register{tuple(args)} -> method')

    def fn_unregister(self, *args):
        logger.debug(f'patch -> v8_periodic_sync_manager.py -> PeriodicSyncManager.unregister{tuple(args)} -> method')
