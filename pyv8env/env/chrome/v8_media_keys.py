from .flags import *


@construct_100001
class MediaKeys:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createSession", "fn_createSession", 0, 0, 1, 0, 0, 0, 0),
        ("setServerCertificate", "fn_setServerCertificate", 1, 0, 1, 0, 1, 0, 0),
        ("getStatusForPolicy", "fn_getStatusForPolicy", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_createSession(self, *args):
        logger.debug(f'patch -> v8_media_keys.py -> MediaKeys.createSession{tuple(args)} -> method')

    def fn_setServerCertificate(self, *args):
        logger.debug(f'patch -> v8_media_keys.py -> MediaKeys.setServerCertificate{tuple(args)} -> method')

    def fn_getStatusForPolicy(self, *args):
        logger.debug(f'patch -> v8_media_keys.py -> MediaKeys.getStatusForPolicy{tuple(args)} -> method')
