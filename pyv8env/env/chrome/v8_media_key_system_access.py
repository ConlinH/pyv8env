from .flags import *


@construct_100001
class MediaKeySystemAccess:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("keySystem", "get_keySystem", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createMediaKeys", "fn_createMediaKeys", 0, 0, 1, 0, 1, 0, 0),
        ("getConfiguration", "fn_getConfiguration", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_keySystem(self):
        val = self._attr.get('keySystem')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_key_system_access.py -> MediaKeySystemAccess.keySystem -> get attr')

    def fn_createMediaKeys(self, *args):
        logger.debug(f'patch -> v8_media_key_system_access.py -> MediaKeySystemAccess.createMediaKeys{tuple(args)} -> method')

    def fn_getConfiguration(self, *args):
        logger.debug(f'patch -> v8_media_key_system_access.py -> MediaKeySystemAccess.getConfiguration{tuple(args)} -> method')
