from .flags import *


@construct_100001
class LockManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("query", "fn_query", 0, 0, 1, 0, 1, 0, 0),
        ("request", "fn_request", 2, 0, 1, 0, 1, 0, 0),

    )

    def fn_query(self, *args):
        logger.debug(f'patch -> v8_lock_manager.py -> LockManager.query{tuple(args)} -> method')

    def fn_request(self, *args):
        logger.debug(f'patch -> v8_lock_manager.py -> LockManager.request{tuple(args)} -> method')
