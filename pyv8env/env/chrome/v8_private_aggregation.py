from .flags import *


@construct_100001
class PrivateAggregation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("contributeToHistogram", "fn_contributeToHistogram", 1, 0, 1, 0, 0, 0, 0),
        ("enableDebugMode", "fn_enableDebugMode", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_contributeToHistogram(self, *args):
        logger.debug(f'patch -> v8_private_aggregation.py -> PrivateAggregation.contributeToHistogram{tuple(args)} -> method')

    def fn_enableDebugMode(self, *args):
        logger.debug(f'patch -> v8_private_aggregation.py -> PrivateAggregation.enableDebugMode{tuple(args)} -> method')
