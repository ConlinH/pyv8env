from .flags import *


@construct_100001
class Permissions:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("query", "fn_query", 1, 0, 1, 0, 1, 0, 0),
        ("request", "fn_request", 1, 0, 1, 0, 1, 0, 0),
        ("requestAll", "fn_requestAll", 1, 0, 1, 0, 1, 0, 0),
        ("revoke", "fn_revoke", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_query(self, *args):
        logger.debug(f'patch -> v8_permissions.py -> Permissions.query{tuple(args)} -> method')

    def fn_request(self, *args):
        logger.debug(f'patch -> v8_permissions.py -> Permissions.request{tuple(args)} -> method')

    def fn_requestAll(self, *args):
        logger.debug(f'patch -> v8_permissions.py -> Permissions.requestAll{tuple(args)} -> method')

    def fn_revoke(self, *args):
        logger.debug(f'patch -> v8_permissions.py -> Permissions.revoke{tuple(args)} -> method')
