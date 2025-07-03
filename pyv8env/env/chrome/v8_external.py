from .flags import *


@construct_100001
class External:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("AddSearchProvider", "fn_AddSearchProvider", 0, 0, 1, 0, 0, 0, 0),
        ("IsSearchProviderInstalled", "fn_IsSearchProviderInstalled", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_AddSearchProvider(self, *args):
        logger.debug(f'patch -> v8_external.py -> External.AddSearchProvider{tuple(args)} -> method')

    def fn_IsSearchProviderInstalled(self, *args):
        logger.debug(f'patch -> v8_external.py -> External.IsSearchProviderInstalled{tuple(args)} -> method')
