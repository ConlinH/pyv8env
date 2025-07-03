from .flags import *
from .v8_payment_request_update_event import PaymentRequestUpdateEvent


@construct_111001
class PaymentMethodChangeEvent(PaymentRequestUpdateEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PaymentMethodChangeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("methodName", "get_methodName", None, 0, 1, 0, 0, 0, 0, 1),
        ("methodDetails", "get_methodDetails", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_methodName(self):
        val = self._attr.get('methodName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_method_change_event.py -> PaymentMethodChangeEvent.methodName -> get attr')

    def get_methodDetails(self):
        val = self._attr.get('methodDetails')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_method_change_event.py -> PaymentMethodChangeEvent.methodDetails -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_method_change_event.py -> PaymentMethodChangeEvent.isTrusted -> get attr')
