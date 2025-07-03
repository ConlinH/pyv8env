from .flags import *


@construct_100001
class PaymentManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("userHint", "get_userHint", "set_userHint", 0, 1, 0, 0, 0, 0, 1),
        ("instruments", "get_instruments", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("enableDelegations", "fn_enableDelegations", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_userHint(self):
        val = self._attr.get('userHint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_manager.py -> PaymentManager.userHint -> get attr')

    def set_userHint(self, val):
        self._attr['userHint'] = val

    def get_instruments(self):
        val = self._attr.get('instruments')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_payment_manager.py -> PaymentManager.instruments -> get attr')

    def fn_enableDelegations(self, *args):
        logger.debug(f'patch -> v8_payment_manager.py -> PaymentManager.enableDelegations{tuple(args)} -> method')
