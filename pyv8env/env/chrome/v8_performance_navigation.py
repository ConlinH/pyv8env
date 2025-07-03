from .flags import *


@construct_100001
class PerformanceNavigation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    TYPE_NAVIGATE = 0
    TYPE_RELOAD = 1
    TYPE_BACK_FORWARD = 2
    TYPE_RESERVED = 255

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("redirectCount", "get_redirectCount", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation.py -> PerformanceNavigation.type -> get attr')

    def get_redirectCount(self):
        val = self._attr.get('redirectCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_navigation.py -> PerformanceNavigation.redirectCount -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_navigation.py -> PerformanceNavigation.toJSON{tuple(args)} -> method')
