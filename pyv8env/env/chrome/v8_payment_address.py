from .flags import *


@construct_100001
class PaymentAddress:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("city", "get_city", None, 0, 1, 0, 0, 0, 0, 1),
        ("country", "get_country", None, 0, 1, 0, 0, 0, 0, 1),
        ("dependentLocality", "get_dependentLocality", None, 0, 1, 0, 0, 0, 0, 1),
        ("organization", "get_organization", None, 0, 1, 0, 0, 0, 0, 1),
        ("phone", "get_phone", None, 0, 1, 0, 0, 0, 0, 1),
        ("postalCode", "get_postalCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("recipient", "get_recipient", None, 0, 1, 0, 0, 0, 0, 1),
        ("region", "get_region", None, 0, 1, 0, 0, 0, 0, 1),
        ("sortingCode", "get_sortingCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("addressLine", "get_addressLine", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_city(self):
        val = self._attr.get('city')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.city -> get attr')

    def get_country(self):
        val = self._attr.get('country')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.country -> get attr')

    def get_dependentLocality(self):
        val = self._attr.get('dependentLocality')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.dependentLocality -> get attr')

    def get_organization(self):
        val = self._attr.get('organization')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.organization -> get attr')

    def get_phone(self):
        val = self._attr.get('phone')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.phone -> get attr')

    def get_postalCode(self):
        val = self._attr.get('postalCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.postalCode -> get attr')

    def get_recipient(self):
        val = self._attr.get('recipient')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.recipient -> get attr')

    def get_region(self):
        val = self._attr.get('region')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.region -> get attr')

    def get_sortingCode(self):
        val = self._attr.get('sortingCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.sortingCode -> get attr')

    def get_addressLine(self):
        val = self._attr.get('addressLine')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.addressLine -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_payment_address.py -> PaymentAddress.toJSON{tuple(args)} -> method')
