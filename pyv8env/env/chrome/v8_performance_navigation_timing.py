from .flags import *
from .v8_performance_resource_timing import PerformanceResourceTiming


@construct_100001
class PerformanceNavigationTiming(PerformanceResourceTiming):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceNavigationTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("unloadEventStart", "get_unloadEventStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("unloadEventEnd", "get_unloadEventEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("domInteractive", "get_domInteractive", None, 0, 1, 0, 0, 0, 0, 1),
        ("domContentLoadedEventStart", "get_domContentLoadedEventStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("domContentLoadedEventEnd", "get_domContentLoadedEventEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("domComplete", "get_domComplete", None, 0, 1, 0, 0, 0, 0, 1),
        ("loadEventStart", "get_loadEventStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("loadEventEnd", "get_loadEventEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("redirectCount", "get_redirectCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("criticalCHRestart", "get_criticalCHRestart", None, 0, 1, 0, 0, 0, 0, 1),
        ("activationStart", "get_activationStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("systemEntropy", "get_systemEntropy", None, 0, 1, 0, 0, 0, 0, 1),
        ("notRestoredReasons", "get_notRestoredReasons", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_unloadEventStart(self):
        val = self._attr.get('unloadEventStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.unloadEventStart -> get attr')

    def get_unloadEventEnd(self):
        val = self._attr.get('unloadEventEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.unloadEventEnd -> get attr')

    def get_domInteractive(self):
        val = self._attr.get('domInteractive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.domInteractive -> get attr')

    def get_domContentLoadedEventStart(self):
        val = self._attr.get('domContentLoadedEventStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.domContentLoadedEventStart -> get attr')

    def get_domContentLoadedEventEnd(self):
        val = self._attr.get('domContentLoadedEventEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.domContentLoadedEventEnd -> get attr')

    def get_domComplete(self):
        val = self._attr.get('domComplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.domComplete -> get attr')

    def get_loadEventStart(self):
        val = self._attr.get('loadEventStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.loadEventStart -> get attr')

    def get_loadEventEnd(self):
        val = self._attr.get('loadEventEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.loadEventEnd -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.type -> get attr')

    def get_redirectCount(self):
        val = self._attr.get('redirectCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.redirectCount -> get attr')

    def get_criticalCHRestart(self):
        val = self._attr.get('criticalCHRestart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.criticalCHRestart -> get attr')

    def get_activationStart(self):
        val = self._attr.get('activationStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.activationStart -> get attr')

    def get_systemEntropy(self):
        val = self._attr.get('systemEntropy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.systemEntropy -> get attr')

    def get_notRestoredReasons(self):
        val = self._attr.get('notRestoredReasons')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.notRestoredReasons -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_navigation_timing.py -> PerformanceNavigationTiming.toJSON{tuple(args)} -> method')
