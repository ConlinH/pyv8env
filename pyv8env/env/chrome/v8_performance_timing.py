from .flags import *


@construct_100001
class PerformanceTiming:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("navigationStart", "get_navigationStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("unloadEventStart", "get_unloadEventStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("unloadEventEnd", "get_unloadEventEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("redirectStart", "get_redirectStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("redirectEnd", "get_redirectEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("fetchStart", "get_fetchStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("domainLookupStart", "get_domainLookupStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("domainLookupEnd", "get_domainLookupEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("connectStart", "get_connectStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("connectEnd", "get_connectEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("secureConnectionStart", "get_secureConnectionStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("requestStart", "get_requestStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseStart", "get_responseStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseEnd", "get_responseEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("domLoading", "get_domLoading", None, 0, 1, 0, 0, 0, 0, 1),
        ("domInteractive", "get_domInteractive", None, 0, 1, 0, 0, 0, 0, 1),
        ("domContentLoadedEventStart", "get_domContentLoadedEventStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("domContentLoadedEventEnd", "get_domContentLoadedEventEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("domComplete", "get_domComplete", None, 0, 1, 0, 0, 0, 0, 1),
        ("loadEventStart", "get_loadEventStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("loadEventEnd", "get_loadEventEnd", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_navigationStart(self):
        val = self._attr.get('navigationStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.navigationStart -> get attr')

    def get_unloadEventStart(self):
        val = self._attr.get('unloadEventStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.unloadEventStart -> get attr')

    def get_unloadEventEnd(self):
        val = self._attr.get('unloadEventEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.unloadEventEnd -> get attr')

    def get_redirectStart(self):
        val = self._attr.get('redirectStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.redirectStart -> get attr')

    def get_redirectEnd(self):
        val = self._attr.get('redirectEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.redirectEnd -> get attr')

    def get_fetchStart(self):
        val = self._attr.get('fetchStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.fetchStart -> get attr')

    def get_domainLookupStart(self):
        val = self._attr.get('domainLookupStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.domainLookupStart -> get attr')

    def get_domainLookupEnd(self):
        val = self._attr.get('domainLookupEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.domainLookupEnd -> get attr')

    def get_connectStart(self):
        val = self._attr.get('connectStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.connectStart -> get attr')

    def get_connectEnd(self):
        val = self._attr.get('connectEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.connectEnd -> get attr')

    def get_secureConnectionStart(self):
        val = self._attr.get('secureConnectionStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.secureConnectionStart -> get attr')

    def get_requestStart(self):
        val = self._attr.get('requestStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.requestStart -> get attr')

    def get_responseStart(self):
        val = self._attr.get('responseStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.responseStart -> get attr')

    def get_responseEnd(self):
        val = self._attr.get('responseEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.responseEnd -> get attr')

    def get_domLoading(self):
        val = self._attr.get('domLoading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.domLoading -> get attr')

    def get_domInteractive(self):
        val = self._attr.get('domInteractive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.domInteractive -> get attr')

    def get_domContentLoadedEventStart(self):
        val = self._attr.get('domContentLoadedEventStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.domContentLoadedEventStart -> get attr')

    def get_domContentLoadedEventEnd(self):
        val = self._attr.get('domContentLoadedEventEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.domContentLoadedEventEnd -> get attr')

    def get_domComplete(self):
        val = self._attr.get('domComplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.domComplete -> get attr')

    def get_loadEventStart(self):
        val = self._attr.get('loadEventStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.loadEventStart -> get attr')

    def get_loadEventEnd(self):
        val = self._attr.get('loadEventEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.loadEventEnd -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_timing.py -> PerformanceTiming.toJSON{tuple(args)} -> method')
