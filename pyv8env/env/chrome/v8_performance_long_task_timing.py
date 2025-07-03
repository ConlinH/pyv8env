from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class PerformanceLongTaskTiming(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceLongTaskTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("attribution", "get_attribution", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_attribution(self):
        val = self._attr.get('attribution')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_long_task_timing.py -> PerformanceLongTaskTiming.attribution -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_long_task_timing.py -> PerformanceLongTaskTiming.toJSON{tuple(args)} -> method')
