from .flags import *


@construct_100001
class PrivateAttribution:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getEncryptedMatchKey", "fn_getEncryptedMatchKey", 2, 0, 1, 0, 1, 0, 0),
        ("getHelperNetworks", "fn_getHelperNetworks", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_getEncryptedMatchKey(self, *args):
        logger.debug(f'patch -> v8_private_attribution.py -> PrivateAttribution.getEncryptedMatchKey{tuple(args)} -> method')

    def fn_getHelperNetworks(self, *args):
        logger.debug(f'patch -> v8_private_attribution.py -> PrivateAttribution.getHelperNetworks{tuple(args)} -> method')
