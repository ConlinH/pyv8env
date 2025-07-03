from .flags import *


@construct_100001
class PushSubscriptionOptions:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("userVisibleOnly", "get_userVisibleOnly", None, 0, 1, 0, 0, 0, 0, 1),
        ("applicationServerKey", "get_applicationServerKey", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_userVisibleOnly(self):
        val = self._attr.get('userVisibleOnly')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription_options.py -> PushSubscriptionOptions.userVisibleOnly -> get attr')

    def get_applicationServerKey(self):
        val = self._attr.get('applicationServerKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription_options.py -> PushSubscriptionOptions.applicationServerKey -> get attr')
