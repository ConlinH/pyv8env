from .flags import *


@construct_100001
class PushSubscription:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("endpoint", "get_endpoint", None, 0, 1, 0, 0, 0, 0, 1),
        ("expirationTime", "get_expirationTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("options", "get_options", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getKey", "fn_getKey", 1, 0, 1, 0, 0, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("unsubscribe", "fn_unsubscribe", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_endpoint(self):
        val = self._attr.get('endpoint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription.py -> PushSubscription.endpoint -> get attr')

    def get_expirationTime(self):
        val = self._attr.get('expirationTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription.py -> PushSubscription.expirationTime -> get attr')

    def get_options(self):
        val = self._attr.get('options')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription.py -> PushSubscription.options -> get attr')

    def fn_getKey(self, *args):
        logger.debug(f'patch -> v8_push_subscription.py -> PushSubscription.getKey{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_push_subscription.py -> PushSubscription.toJSON{tuple(args)} -> method')

    def fn_unsubscribe(self, *args):
        logger.debug(f'patch -> v8_push_subscription.py -> PushSubscription.unsubscribe{tuple(args)} -> method')
