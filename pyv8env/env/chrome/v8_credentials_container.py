from .flags import *


@construct_100001
class CredentialsContainer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("create", "fn_create", 0, 0, 1, 0, 1, 0, 0),
        ("get", "fn_get", 0, 0, 1, 0, 1, 0, 0),
        ("preventSilentAccess", "fn_preventSilentAccess", 0, 0, 1, 0, 1, 0, 0),
        ("store", "fn_store", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_create(self, *args):
        logger.debug(f'patch -> v8_credentials_container.py -> CredentialsContainer.create{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_credentials_container.py -> CredentialsContainer.get{tuple(args)} -> method')

    def fn_preventSilentAccess(self, *args):
        logger.debug(f'patch -> v8_credentials_container.py -> CredentialsContainer.preventSilentAccess{tuple(args)} -> method')

    def fn_store(self, *args):
        logger.debug(f'patch -> v8_credentials_container.py -> CredentialsContainer.store{tuple(args)} -> method')
