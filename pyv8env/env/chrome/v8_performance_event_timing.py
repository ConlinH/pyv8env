from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class PerformanceEventTiming(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceEventTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("processingStart", "get_processingStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("processingEnd", "get_processingEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("cancelable", "get_cancelable", None, 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),
        ("interactionId", "get_interactionId", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_processingStart(self):
        val = self._attr.get('processingStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_event_timing.py -> PerformanceEventTiming.processingStart -> get attr')

    def get_processingEnd(self):
        val = self._attr.get('processingEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_event_timing.py -> PerformanceEventTiming.processingEnd -> get attr')

    def get_cancelable(self):
        val = self._attr.get('cancelable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_event_timing.py -> PerformanceEventTiming.cancelable -> get attr')

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_event_timing.py -> PerformanceEventTiming.target -> get attr')

    def get_interactionId(self):
        val = self._attr.get('interactionId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_event_timing.py -> PerformanceEventTiming.interactionId -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_event_timing.py -> PerformanceEventTiming.toJSON{tuple(args)} -> method')
