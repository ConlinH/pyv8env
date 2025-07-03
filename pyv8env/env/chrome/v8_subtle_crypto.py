from .flags import *


@construct_100001
class SubtleCrypto:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("decrypt", "fn_decrypt", 3, 0, 1, 0, 1, 0, 0),
        ("deriveBits", "fn_deriveBits", 3, 0, 1, 0, 1, 0, 0),
        ("deriveKey", "fn_deriveKey", 5, 0, 1, 0, 1, 0, 0),
        ("digest", "fn_digest", 2, 0, 1, 0, 1, 0, 0),
        ("encrypt", "fn_encrypt", 3, 0, 1, 0, 1, 0, 0),
        ("exportKey", "fn_exportKey", 2, 0, 1, 0, 1, 0, 0),
        ("generateKey", "fn_generateKey", 3, 0, 1, 0, 1, 0, 0),
        ("importKey", "fn_importKey", 5, 0, 1, 0, 1, 0, 0),
        ("sign", "fn_sign", 3, 0, 1, 0, 1, 0, 0),
        ("unwrapKey", "fn_unwrapKey", 7, 0, 1, 0, 1, 0, 0),
        ("verify", "fn_verify", 4, 0, 1, 0, 1, 0, 0),
        ("wrapKey", "fn_wrapKey", 4, 0, 1, 0, 1, 0, 0),

    )

    def fn_decrypt(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.decrypt{tuple(args)} -> method')

    def fn_deriveBits(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.deriveBits{tuple(args)} -> method')

    def fn_deriveKey(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.deriveKey{tuple(args)} -> method')

    def fn_digest(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.digest{tuple(args)} -> method')

    def fn_encrypt(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.encrypt{tuple(args)} -> method')

    def fn_exportKey(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.exportKey{tuple(args)} -> method')

    def fn_generateKey(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.generateKey{tuple(args)} -> method')

    def fn_importKey(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.importKey{tuple(args)} -> method')

    def fn_sign(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.sign{tuple(args)} -> method')

    def fn_unwrapKey(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.unwrapKey{tuple(args)} -> method')

    def fn_verify(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.verify{tuple(args)} -> method')

    def fn_wrapKey(self, *args):
        logger.debug(f'patch -> v8_subtle_crypto.py -> SubtleCrypto.wrapKey{tuple(args)} -> method')
