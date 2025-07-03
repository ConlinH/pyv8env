from .flags import *


@construct_100001
class IdentityProvider:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getUserInfo", "fn_getUserInfo", 1, 0, 2, 0, 1, 1, 0),
        ("close", "fn_close", 0, 0, 2, 0, 1, 1, 0),
        ("register", "fn_register", 1, 0, 2, 0, 1, 1, 0),
        ("unregister", "fn_unregister", 1, 0, 2, 0, 1, 1, 0),
        ("resolve", "fn_resolve", 1, 0, 2, 0, 1, 1, 0),

    )

    @classmethod
    def fn_getUserInfo(cls, *args):
        logger.debug(f'patch -> v8_identity_provider.py -> IdentityProvider.getUserInfo{tuple(args)} -> method')

    @classmethod
    def fn_close(cls, *args):
        logger.debug(f'patch -> v8_identity_provider.py -> IdentityProvider.close{tuple(args)} -> method')

    @classmethod
    def fn_register(cls, *args):
        logger.debug(f'patch -> v8_identity_provider.py -> IdentityProvider.register{tuple(args)} -> method')

    @classmethod
    def fn_unregister(cls, *args):
        logger.debug(f'patch -> v8_identity_provider.py -> IdentityProvider.unregister{tuple(args)} -> method')

    @classmethod
    def fn_resolve(cls, *args):
        logger.debug(f'patch -> v8_identity_provider.py -> IdentityProvider.resolve{tuple(args)} -> method')
