from .flags import *


@construct_100001
class TimeRanges:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("end", "fn_end", 1, 0, 1, 0, 0, 0, 0),
        ("start", "fn_start", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_time_ranges.py -> TimeRanges.length -> get attr')

    def fn_end(self, *args):
        logger.debug(f'patch -> v8_time_ranges.py -> TimeRanges.end{tuple(args)} -> method')

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_time_ranges.py -> TimeRanges.start{tuple(args)} -> method')
