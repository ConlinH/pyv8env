from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class LayoutShift(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(LayoutShift, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("value", "get_value", None, 0, 1, 0, 0, 0, 0, 1),
        ("hadRecentInput", "get_hadRecentInput", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastInputTime", "get_lastInputTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("sources", "get_sources", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_shift.py -> LayoutShift.value -> get attr')

    def get_hadRecentInput(self):
        val = self._attr.get('hadRecentInput')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_shift.py -> LayoutShift.hadRecentInput -> get attr')

    def get_lastInputTime(self):
        val = self._attr.get('lastInputTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_shift.py -> LayoutShift.lastInputTime -> get attr')

    def get_sources(self):
        val = self._attr.get('sources')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_shift.py -> LayoutShift.sources -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_layout_shift.py -> LayoutShift.toJSON{tuple(args)} -> method')
