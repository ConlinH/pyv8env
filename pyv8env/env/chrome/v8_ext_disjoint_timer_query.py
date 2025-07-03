from .flags import *


@construct_000000
class EXTDisjointTimerQuery:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    QUERY_COUNTER_BITS_EXT = 34916
    CURRENT_QUERY_EXT = 34917
    QUERY_RESULT_EXT = 34918
    QUERY_RESULT_AVAILABLE_EXT = 34919
    TIME_ELAPSED_EXT = 35007
    TIMESTAMP_EXT = 36392
    GPU_DISJOINT_EXT = 36795

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("beginQueryEXT", "fn_beginQueryEXT", 2, 0, 1, 0, 0, 0, 0),
        ("createQueryEXT", "fn_createQueryEXT", 0, 0, 1, 0, 0, 0, 0),
        ("deleteQueryEXT", "fn_deleteQueryEXT", 1, 0, 1, 0, 0, 0, 0),
        ("endQueryEXT", "fn_endQueryEXT", 1, 0, 1, 0, 0, 0, 0),
        ("getQueryEXT", "fn_getQueryEXT", 2, 0, 1, 0, 0, 0, 0),
        ("getQueryObjectEXT", "fn_getQueryObjectEXT", 2, 0, 1, 0, 0, 0, 0),
        ("isQueryEXT", "fn_isQueryEXT", 1, 0, 1, 0, 0, 0, 0),
        ("queryCounterEXT", "fn_queryCounterEXT", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_beginQueryEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.beginQueryEXT{tuple(args)} -> method')

    def fn_createQueryEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.createQueryEXT{tuple(args)} -> method')

    def fn_deleteQueryEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.deleteQueryEXT{tuple(args)} -> method')

    def fn_endQueryEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.endQueryEXT{tuple(args)} -> method')

    def fn_getQueryEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.getQueryEXT{tuple(args)} -> method')

    def fn_getQueryObjectEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.getQueryObjectEXT{tuple(args)} -> method')

    def fn_isQueryEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.isQueryEXT{tuple(args)} -> method')

    def fn_queryCounterEXT(self, *args):
        logger.debug(f'patch -> v8_ext_disjoint_timer_query.py -> EXTDisjointTimerQuery.queryCounterEXT{tuple(args)} -> method')
