from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class PaymentRequest(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PaymentRequest, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("shippingAddress", "get_shippingAddress", None, 0, 1, 0, 0, 0, 0, 1),
        ("shippingOption", "get_shippingOption", None, 0, 1, 0, 0, 0, 0, 1),
        ("shippingType", "get_shippingType", None, 0, 1, 0, 0, 0, 0, 1),
        ("onshippingaddresschange", "get_onshippingaddresschange", "set_onshippingaddresschange", 0, 1, 0, 0, 0, 0, 1),
        ("onshippingoptionchange", "get_onshippingoptionchange", "set_onshippingoptionchange", 0, 1, 0, 0, 0, 0, 1),
        ("onpaymentmethodchange", "get_onpaymentmethodchange", "set_onpaymentmethodchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 1, 0, 0),
        ("canMakePayment", "fn_canMakePayment", 0, 0, 1, 0, 1, 0, 0),
        ("hasEnrolledInstrument", "fn_hasEnrolledInstrument", 0, 0, 1, 0, 1, 0, 0),
        ("show", "fn_show", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.id -> get attr')

    def get_shippingAddress(self):
        val = self._attr.get('shippingAddress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.shippingAddress -> get attr')

    def get_shippingOption(self):
        val = self._attr.get('shippingOption')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.shippingOption -> get attr')

    def get_shippingType(self):
        val = self._attr.get('shippingType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.shippingType -> get attr')

    def get_onshippingaddresschange(self):
        val = self._attr.get('onshippingaddresschange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.onshippingaddresschange -> get attr')

    def set_onshippingaddresschange(self, val):
        self._attr['onshippingaddresschange'] = val

    def get_onshippingoptionchange(self):
        val = self._attr.get('onshippingoptionchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.onshippingoptionchange -> get attr')

    def set_onshippingoptionchange(self, val):
        self._attr['onshippingoptionchange'] = val

    def get_onpaymentmethodchange(self):
        val = self._attr.get('onpaymentmethodchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.onpaymentmethodchange -> get attr')

    def set_onpaymentmethodchange(self, val):
        self._attr['onpaymentmethodchange'] = val

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.abort{tuple(args)} -> method')

    def fn_canMakePayment(self, *args):
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.canMakePayment{tuple(args)} -> method')

    def fn_hasEnrolledInstrument(self, *args):
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.hasEnrolledInstrument{tuple(args)} -> method')

    def fn_show(self, *args):
        logger.debug(f'patch -> v8_payment_request.py -> PaymentRequest.show{tuple(args)} -> method')
