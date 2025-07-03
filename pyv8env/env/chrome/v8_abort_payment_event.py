from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_112001
class AbortPaymentEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AbortPaymentEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("respondWith", "fn_respondWith", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abort_payment_event.py -> AbortPaymentEvent.isTrusted -> get attr')

    def fn_respondWith(self, *args):
        logger.debug(f'patch -> v8_abort_payment_event.py -> AbortPaymentEvent.respondWith{tuple(args)} -> method')
