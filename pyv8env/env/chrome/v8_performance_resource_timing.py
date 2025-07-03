from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class PerformanceResourceTiming(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceResourceTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("initiatorType", "get_initiatorType", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextHopProtocol", "get_nextHopProtocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("deliveryType", "get_deliveryType", None, 0, 1, 0, 0, 0, 0, 1),
        ("workerStart", "get_workerStart", None, 0, 1, 0, 0, 0, 0, 1),
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
        ("transferSize", "get_transferSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("encodedBodySize", "get_encodedBodySize", None, 0, 1, 0, 0, 0, 0, 1),
        ("decodedBodySize", "get_decodedBodySize", None, 0, 1, 0, 0, 0, 0, 1),
        ("serverTiming", "get_serverTiming", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseStatus", "get_responseStatus", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstInterimResponseStart", "get_firstInterimResponseStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("workerRouterEvaluationStart", "get_workerRouterEvaluationStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("workerCacheLookupStart", "get_workerCacheLookupStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("matchedSourceType", "get_matchedSourceType", None, 0, 1, 0, 0, 0, 0, 1),
        ("finalSourceType", "get_finalSourceType", None, 0, 1, 0, 0, 0, 0, 1),
        ("renderBlockingStatus", "get_renderBlockingStatus", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentType", "get_contentType", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_initiatorType(self):
        val = self._attr.get('initiatorType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.initiatorType -> get attr')

    def get_nextHopProtocol(self):
        val = self._attr.get('nextHopProtocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.nextHopProtocol -> get attr')

    def get_deliveryType(self):
        val = self._attr.get('deliveryType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.deliveryType -> get attr')

    def get_workerStart(self):
        val = self._attr.get('workerStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.workerStart -> get attr')

    def get_redirectStart(self):
        val = self._attr.get('redirectStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.redirectStart -> get attr')

    def get_redirectEnd(self):
        val = self._attr.get('redirectEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.redirectEnd -> get attr')

    def get_fetchStart(self):
        val = self._attr.get('fetchStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.fetchStart -> get attr')

    def get_domainLookupStart(self):
        val = self._attr.get('domainLookupStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.domainLookupStart -> get attr')

    def get_domainLookupEnd(self):
        val = self._attr.get('domainLookupEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.domainLookupEnd -> get attr')

    def get_connectStart(self):
        val = self._attr.get('connectStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.connectStart -> get attr')

    def get_connectEnd(self):
        val = self._attr.get('connectEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.connectEnd -> get attr')

    def get_secureConnectionStart(self):
        val = self._attr.get('secureConnectionStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.secureConnectionStart -> get attr')

    def get_requestStart(self):
        val = self._attr.get('requestStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.requestStart -> get attr')

    def get_responseStart(self):
        val = self._attr.get('responseStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.responseStart -> get attr')

    def get_responseEnd(self):
        val = self._attr.get('responseEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.responseEnd -> get attr')

    def get_transferSize(self):
        val = self._attr.get('transferSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.transferSize -> get attr')

    def get_encodedBodySize(self):
        val = self._attr.get('encodedBodySize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.encodedBodySize -> get attr')

    def get_decodedBodySize(self):
        val = self._attr.get('decodedBodySize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.decodedBodySize -> get attr')

    def get_serverTiming(self):
        val = self._attr.get('serverTiming')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.serverTiming -> get attr')

    def get_responseStatus(self):
        val = self._attr.get('responseStatus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.responseStatus -> get attr')

    def get_firstInterimResponseStart(self):
        val = self._attr.get('firstInterimResponseStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.firstInterimResponseStart -> get attr')

    def get_workerRouterEvaluationStart(self):
        val = self._attr.get('workerRouterEvaluationStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.workerRouterEvaluationStart -> get attr')

    def get_workerCacheLookupStart(self):
        val = self._attr.get('workerCacheLookupStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.workerCacheLookupStart -> get attr')

    def get_matchedSourceType(self):
        val = self._attr.get('matchedSourceType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.matchedSourceType -> get attr')

    def get_finalSourceType(self):
        val = self._attr.get('finalSourceType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.finalSourceType -> get attr')

    def get_renderBlockingStatus(self):
        val = self._attr.get('renderBlockingStatus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.renderBlockingStatus -> get attr')

    def get_contentType(self):
        val = self._attr.get('contentType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.contentType -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_resource_timing.py -> PerformanceResourceTiming.toJSON{tuple(args)} -> method')
