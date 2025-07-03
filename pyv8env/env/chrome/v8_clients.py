from .flags import *


@construct_100001
class Clients:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("claim", "fn_claim", 0, 0, 1, 0, 1, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 1, 0, 0),
        ("matchAll", "fn_matchAll", 0, 0, 1, 0, 1, 0, 0),
        ("openWindow", "fn_openWindow", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_claim(self, *args):
        logger.debug(f'patch -> v8_clients.py -> Clients.claim{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_clients.py -> Clients.get{tuple(args)} -> method')

    def fn_matchAll(self, *args):
        logger.debug(f'patch -> v8_clients.py -> Clients.matchAll{tuple(args)} -> method')

    def fn_openWindow(self, *args):
        logger.debug(f'patch -> v8_clients.py -> Clients.openWindow{tuple(args)} -> method')
