from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_111001
class PushSubscriptionChangeEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PushSubscriptionChangeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("newSubscription", "get_newSubscription", None, 0, 1, 0, 0, 0, 0, 1),
        ("oldSubscription", "get_oldSubscription", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_newSubscription(self):
        val = self._attr.get('newSubscription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription_change_event.py -> PushSubscriptionChangeEvent.newSubscription -> get attr')

    def get_oldSubscription(self):
        val = self._attr.get('oldSubscription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription_change_event.py -> PushSubscriptionChangeEvent.oldSubscription -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_subscription_change_event.py -> PushSubscriptionChangeEvent.isTrusted -> get attr')
