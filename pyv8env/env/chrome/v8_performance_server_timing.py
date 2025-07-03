from .flags import *


@construct_100001
class PerformanceServerTiming:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),
        ("description", "get_description", None, 0, 1, 0, 0, 0, 0, 1),

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
        logger.debug(f'patch -> v8_performance_server_timing.py -> PerformanceServerTiming.name -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_server_timing.py -> PerformanceServerTiming.duration -> get attr')

    def get_description(self):
        val = self._attr.get('description')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_server_timing.py -> PerformanceServerTiming.description -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_server_timing.py -> PerformanceServerTiming.toJSON{tuple(args)} -> method')
