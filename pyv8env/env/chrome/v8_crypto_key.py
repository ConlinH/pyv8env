from .flags import *


@construct_100001
class CryptoKey:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("extractable", "get_extractable", None, 0, 1, 0, 0, 0, 0, 1),
        ("algorithm", "get_algorithm", None, 0, 1, 0, 0, 0, 0, 1),
        ("usages", "get_usages", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_crypto_key.py -> CryptoKey.type -> get attr')

    def get_extractable(self):
        val = self._attr.get('extractable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_crypto_key.py -> CryptoKey.extractable -> get attr')

    def get_algorithm(self):
        val = self._attr.get('algorithm')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_crypto_key.py -> CryptoKey.algorithm -> get attr')

    def get_usages(self):
        val = self._attr.get('usages')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_crypto_key.py -> CryptoKey.usages -> get attr')
