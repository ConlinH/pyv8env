from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class PerformanceMeasure(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceMeasure, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("detail", "get_detail", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_detail(self):
        val = self._attr.get('detail')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_measure.py -> PerformanceMeasure.detail -> get attr')
