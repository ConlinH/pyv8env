from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_112001
class PaymentRequestEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PaymentRequestEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("topOrigin", "get_topOrigin", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentRequestOrigin", "get_paymentRequestOrigin", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentRequestId", "get_paymentRequestId", None, 0, 1, 0, 0, 0, 0, 1),
        ("methodData", "get_methodData", None, 0, 1, 0, 0, 0, 0, 1),
        ("total", "get_total", None, 0, 1, 0, 0, 0, 0, 1),
        ("modifiers", "get_modifiers", None, 0, 1, 0, 0, 0, 0, 1),
        ("instrumentKey", "get_instrumentKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentOptions", "get_paymentOptions", None, 0, 1, 0, 0, 0, 0, 1),
        ("shippingOptions", "get_shippingOptions", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("changePaymentMethod", "fn_changePaymentMethod", 1, 0, 1, 0, 1, 0, 0),
        ("changeShippingAddress", "fn_changeShippingAddress", 1, 0, 1, 0, 1, 0, 0),
        ("changeShippingOption", "fn_changeShippingOption", 1, 0, 1, 0, 1, 0, 0),
        ("openWindow", "fn_openWindow", 1, 0, 1, 0, 1, 0, 0),
        ("respondWith", "fn_respondWith", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_topOrigin(self):
        val = self._attr.get('topOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.topOrigin -> get attr')

    def get_paymentRequestOrigin(self):
        val = self._attr.get('paymentRequestOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.paymentRequestOrigin -> get attr')

    def get_paymentRequestId(self):
        val = self._attr.get('paymentRequestId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.paymentRequestId -> get attr')

    def get_methodData(self):
        val = self._attr.get('methodData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.methodData -> get attr')

    def get_total(self):
        val = self._attr.get('total')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.total -> get attr')

    def get_modifiers(self):
        val = self._attr.get('modifiers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.modifiers -> get attr')

    def get_instrumentKey(self):
        val = self._attr.get('instrumentKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.instrumentKey -> get attr')

    def get_paymentOptions(self):
        val = self._attr.get('paymentOptions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.paymentOptions -> get attr')

    def get_shippingOptions(self):
        val = self._attr.get('shippingOptions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.shippingOptions -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.isTrusted -> get attr')

    def fn_changePaymentMethod(self, *args):
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.changePaymentMethod{tuple(args)} -> method')

    def fn_changeShippingAddress(self, *args):
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.changeShippingAddress{tuple(args)} -> method')

    def fn_changeShippingOption(self, *args):
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.changeShippingOption{tuple(args)} -> method')

    def fn_openWindow(self, *args):
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.openWindow{tuple(args)} -> method')

    def fn_respondWith(self, *args):
        logger.debug(f'patch -> v8_payment_request_event.py -> PaymentRequestEvent.respondWith{tuple(args)} -> method')
