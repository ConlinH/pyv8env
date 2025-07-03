from .flags import *


@construct_100001
class PushManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("supportedContentEncodings", "get_supportedContentEncodings", None, 0, 2, 0, 1, 1, 1, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getSubscription", "fn_getSubscription", 0, 0, 1, 0, 1, 0, 0),
        ("permissionState", "fn_permissionState", 0, 0, 1, 0, 1, 0, 0),
        ("subscribe", "fn_subscribe", 0, 0, 1, 0, 1, 0, 0),

    )

    @classmethod
    def get_supportedContentEncodings(cls):
        logger.debug(f'patch -> v8_push_manager.py -> PushManager.supportedContentEncodings -> get attr')

    def fn_getSubscription(self, *args):
        logger.debug(f'patch -> v8_push_manager.py -> PushManager.getSubscription{tuple(args)} -> method')

    def fn_permissionState(self, *args):
        logger.debug(f'patch -> v8_push_manager.py -> PushManager.permissionState{tuple(args)} -> method')

    def fn_subscribe(self, *args):
        logger.debug(f'patch -> v8_push_manager.py -> PushManager.subscribe{tuple(args)} -> method')
