from .flags import *


@construct_100001
class SyncManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getTags", "fn_getTags", 0, 0, 1, 0, 1, 0, 0),
        ("register", "fn_register", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_getTags(self, *args):
        logger.debug(f'patch -> v8_sync_manager.py -> SyncManager.getTags{tuple(args)} -> method')

    def fn_register(self, *args):
        logger.debug(f'patch -> v8_sync_manager.py -> SyncManager.register{tuple(args)} -> method')
