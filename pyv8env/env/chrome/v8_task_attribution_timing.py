from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class TaskAttributionTiming(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TaskAttributionTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("containerType", "get_containerType", None, 0, 1, 0, 0, 0, 0, 1),
        ("containerSrc", "get_containerSrc", None, 0, 1, 0, 0, 0, 0, 1),
        ("containerId", "get_containerId", None, 0, 1, 0, 0, 0, 0, 1),
        ("containerName", "get_containerName", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_containerType(self):
        val = self._attr.get('containerType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_task_attribution_timing.py -> TaskAttributionTiming.containerType -> get attr')

    def get_containerSrc(self):
        val = self._attr.get('containerSrc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_task_attribution_timing.py -> TaskAttributionTiming.containerSrc -> get attr')

    def get_containerId(self):
        val = self._attr.get('containerId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_task_attribution_timing.py -> TaskAttributionTiming.containerId -> get attr')

    def get_containerName(self):
        val = self._attr.get('containerName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_task_attribution_timing.py -> TaskAttributionTiming.containerName -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_task_attribution_timing.py -> TaskAttributionTiming.toJSON{tuple(args)} -> method')
