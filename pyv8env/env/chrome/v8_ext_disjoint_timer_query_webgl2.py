from .flags import *


@construct_000000
class EXTDisjointTimerQueryWebGL2:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    QUERY_COUNTER_BITS_EXT = 34916
    TIME_ELAPSED_EXT = 35007
    TIMESTAMP_EXT = 36392
    GPU_DISJOINT_EXT = 36795

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("queryCounterEXT", "fn_queryCounterEXT", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_queryCounterEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query_webgl2.py -> EXTDisjointTimerQueryWebGL2.queryCounterEXT{tuple(args)} -> method')
