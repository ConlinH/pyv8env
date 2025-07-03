from .flags import *


@construct_100001
class PerformanceEntry:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("entryType", "get_entryType", None, 0, 1, 0, 0, 0, 0, 1),
        ("startTime", "get_startTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigationId", "get_navigationId", None, 0, 1, 0, 0, 0, 0, 1),
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_entry.py -> PerformanceEntry.name -> get attr')

    def get_entryType(self):
        val = self._attr.get('entryType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_entry.py -> PerformanceEntry.entryType -> get attr')

    def get_startTime(self):
        val = self._attr.get('startTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_entry.py -> PerformanceEntry.startTime -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_entry.py -> PerformanceEntry.duration -> get attr')

    def get_navigationId(self):
        val = self._attr.get('navigationId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_entry.py -> PerformanceEntry.navigationId -> get attr')

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_entry.py -> PerformanceEntry.source -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_entry.py -> PerformanceEntry.toJSON{tuple(args)} -> method')
