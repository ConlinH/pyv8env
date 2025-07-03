from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class PaymentResponse(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PaymentResponse, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("requestId", "get_requestId", None, 0, 1, 0, 0, 0, 0, 1),
        ("methodName", "get_methodName", None, 0, 1, 0, 0, 0, 0, 1),
        ("details", "get_details", None, 0, 1, 0, 0, 0, 0, 1),
        ("shippingAddress", "get_shippingAddress", None, 0, 1, 0, 0, 0, 0, 1),
        ("shippingOption", "get_shippingOption", None, 0, 1, 0, 0, 0, 0, 1),
        ("payerName", "get_payerName", None, 0, 1, 0, 0, 0, 0, 1),
        ("payerEmail", "get_payerEmail", None, 0, 1, 0, 0, 0, 0, 1),
        ("payerPhone", "get_payerPhone", None, 0, 1, 0, 0, 0, 0, 1),
        ("onpayerdetailchange", "get_onpayerdetailchange", "set_onpayerdetailchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("complete", "fn_complete", 0, 0, 1, 0, 1, 0, 0),
        ("retry", "fn_retry", 0, 0, 1, 0, 1, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_requestId(self):
        val = self._attr.get('requestId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.requestId -> get attr')

    def get_methodName(self):
        val = self._attr.get('methodName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.methodName -> get attr')

    def get_details(self):
        val = self._attr.get('details')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.details -> get attr')

    def get_shippingAddress(self):
        val = self._attr.get('shippingAddress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.shippingAddress -> get attr')

    def get_shippingOption(self):
        val = self._attr.get('shippingOption')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.shippingOption -> get attr')

    def get_payerName(self):
        val = self._attr.get('payerName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.payerName -> get attr')

    def get_payerEmail(self):
        val = self._attr.get('payerEmail')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.payerEmail -> get attr')

    def get_payerPhone(self):
        val = self._attr.get('payerPhone')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.payerPhone -> get attr')

    def get_onpayerdetailchange(self):
        val = self._attr.get('onpayerdetailchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.onpayerdetailchange -> get attr')

    def set_onpayerdetailchange(self, val):
        self._attr['onpayerdetailchange'] = val

    def fn_complete(self, *args):
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.complete{tuple(args)} -> method')

    def fn_retry(self, *args):
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.retry{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_payment_response.py -> PaymentResponse.toJSON{tuple(args)} -> method')
