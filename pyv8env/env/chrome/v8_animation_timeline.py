from .flags import *


@construct_100001
class AnimationTimeline:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("currentTime", "get_currentTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getCurrentTime", "fn_getCurrentTime", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_currentTime(self):
        val = self._attr.get('currentTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_timeline.py -> AnimationTimeline.currentTime -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_timeline.py -> AnimationTimeline.duration -> get attr')

    def fn_getCurrentTime(self, *args):
        logger.debug(f'patch -> v8_animation_timeline.py -> AnimationTimeline.getCurrentTime{tuple(args)} -> method')
