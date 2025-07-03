from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Performance(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Performance, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("timeOrigin", "get_timeOrigin", None, 0, 1, 0, 0, 0, 0, 1),
        ("onresourcetimingbufferfull", "get_onresourcetimingbufferfull", "set_onresourcetimingbufferfull", 0, 1, 0, 0, 0, 0, 1),
        ("softNavPaintMetricsSupported", "get_softNavPaintMetricsSupported", None, 0, 1, 0, 0, 0, 0, 1),
        ("timing", "get_timing", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigation", "get_navigation", None, 0, 1, 0, 0, 0, 0, 1),
        ("memory", "get_memory", None, 0, 1, 0, 0, 0, 0, 1),
        ("eventCounts", "get_eventCounts", None, 0, 1, 0, 0, 0, 0, 1),
        ("interactionCount", "get_interactionCount", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clearMarks", "fn_clearMarks", 0, 0, 1, 0, 0, 0, 0),
        ("clearMeasures", "fn_clearMeasures", 0, 0, 1, 0, 0, 0, 0),
        ("clearResourceTimings", "fn_clearResourceTimings", 0, 0, 1, 0, 0, 0, 0),
        ("getEntries", "fn_getEntries", 0, 0, 1, 0, 0, 0, 0),
        ("getEntriesByName", "fn_getEntriesByName", 1, 0, 1, 0, 0, 0, 0),
        ("getEntriesByType", "fn_getEntriesByType", 1, 0, 1, 0, 0, 0, 0),
        ("mark", "fn_mark", 1, 0, 1, 0, 0, 0, 0),
        ("measure", "fn_measure", 1, 0, 1, 0, 0, 0, 0),
        ("now", "fn_now", 0, 0, 1, 0, 0, 0, 1),
        ("setResourceTimingBufferSize", "fn_setResourceTimingBufferSize", 1, 0, 1, 0, 0, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("measureUserAgentSpecificMemory", "fn_measureUserAgentSpecificMemory", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_timeOrigin(self):
        val = self._attr.get('timeOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.timeOrigin -> get attr')

    def get_onresourcetimingbufferfull(self):
        val = self._attr.get('onresourcetimingbufferfull')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.onresourcetimingbufferfull -> get attr')

    def set_onresourcetimingbufferfull(self, val):
        self._attr['onresourcetimingbufferfull'] = val

    def get_softNavPaintMetricsSupported(self):
        val = self._attr.get('softNavPaintMetricsSupported')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.softNavPaintMetricsSupported -> get attr')

    def get_timing(self):
        val = self._attr.get('timing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.timing -> get attr')

    def get_navigation(self):
        val = self._attr.get('navigation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.navigation -> get attr')

    def get_memory(self):
        val = self._attr.get('memory')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.memory -> get attr')

    def get_eventCounts(self):
        val = self._attr.get('eventCounts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.eventCounts -> get attr')

    def get_interactionCount(self):
        val = self._attr.get('interactionCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance.py -> Performance.interactionCount -> get attr')

    def fn_clearMarks(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.clearMarks{tuple(args)} -> method')

    def fn_clearMeasures(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.clearMeasures{tuple(args)} -> method')

    def fn_clearResourceTimings(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.clearResourceTimings{tuple(args)} -> method')

    def fn_getEntries(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.getEntries{tuple(args)} -> method')

    def fn_getEntriesByName(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.getEntriesByName{tuple(args)} -> method')

    def fn_getEntriesByType(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.getEntriesByType{tuple(args)} -> method')

    def fn_mark(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.mark{tuple(args)} -> method')

    def fn_measure(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.measure{tuple(args)} -> method')

    def fn_now(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.now{tuple(args)} -> method')

    def fn_setResourceTimingBufferSize(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.setResourceTimingBufferSize{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.toJSON{tuple(args)} -> method')

    def fn_measureUserAgentSpecificMemory(self, *args):
        logger.debug(f'patch -> v8_performance.py -> Performance.measureUserAgentSpecificMemory{tuple(args)} -> method')
