from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class PerformanceElementTiming(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceElementTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("renderTime", "get_renderTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("loadTime", "get_loadTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("intersectionRect", "get_intersectionRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("identifier", "get_identifier", None, 0, 1, 0, 0, 0, 0, 1),
        ("naturalWidth", "get_naturalWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("naturalHeight", "get_naturalHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("element", "get_element", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_renderTime(self):
        val = self._attr.get('renderTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.renderTime -> get attr')

    def get_loadTime(self):
        val = self._attr.get('loadTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.loadTime -> get attr')

    def get_intersectionRect(self):
        val = self._attr.get('intersectionRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.intersectionRect -> get attr')

    def get_identifier(self):
        val = self._attr.get('identifier')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.identifier -> get attr')

    def get_naturalWidth(self):
        val = self._attr.get('naturalWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.naturalWidth -> get attr')

    def get_naturalHeight(self):
        val = self._attr.get('naturalHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.naturalHeight -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.id -> get attr')

    def get_element(self):
        val = self._attr.get('element')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.element -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.url -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_element_timing.py -> PerformanceElementTiming.toJSON{tuple(args)} -> method')
