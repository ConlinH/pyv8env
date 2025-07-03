from .flags import *


@construct_100001
class Crypto:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("subtle", "get_subtle", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getRandomValues", "fn_getRandomValues", 1, 0, 1, 0, 0, 0, 0),
        ("randomUUID", "fn_randomUUID", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_subtle(self):
        val = self._attr.get('subtle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_crypto.py -> Crypto.subtle -> get attr')

    def fn_getRandomValues(self, *args):
        logger.debug(f'patch -> v8_crypto.py -> Crypto.getRandomValues{tuple(args)} -> method')

    def fn_randomUUID(self, *args):
        logger.debug(f'patch -> v8_crypto.py -> Crypto.randomUUID{tuple(args)} -> method')
