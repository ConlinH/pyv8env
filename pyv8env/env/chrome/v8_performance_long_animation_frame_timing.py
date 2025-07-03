from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class PerformanceLongAnimationFrameTiming(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceLongAnimationFrameTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("renderStart", "get_renderStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("styleAndLayoutStart", "get_styleAndLayoutStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstUIEventTimestamp", "get_firstUIEventTimestamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockingDuration", "get_blockingDuration", None, 0, 1, 0, 0, 0, 0, 1),
        ("scripts", "get_scripts", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_renderStart(self):
        val = self._attr.get('renderStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_long_animation_frame_timing.py -> PerformanceLongAnimationFrameTiming.renderStart -> get attr')

    def get_styleAndLayoutStart(self):
        val = self._attr.get('styleAndLayoutStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_long_animation_frame_timing.py -> PerformanceLongAnimationFrameTiming.styleAndLayoutStart -> get attr')

    def get_firstUIEventTimestamp(self):
        val = self._attr.get('firstUIEventTimestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_long_animation_frame_timing.py -> PerformanceLongAnimationFrameTiming.firstUIEventTimestamp -> get attr')

    def get_blockingDuration(self):
        val = self._attr.get('blockingDuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_long_animation_frame_timing.py -> PerformanceLongAnimationFrameTiming.blockingDuration -> get attr')

    def get_scripts(self):
        val = self._attr.get('scripts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_long_animation_frame_timing.py -> PerformanceLongAnimationFrameTiming.scripts -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_long_animation_frame_timing.py -> PerformanceLongAnimationFrameTiming.toJSON{tuple(args)} -> method')
