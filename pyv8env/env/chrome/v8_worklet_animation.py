from .flags import *


@construct_112001
class WorkletAnimation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("animatorName", "get_animatorName", None, 0, 1, 0, 0, 0, 0, 1),
        ("effect", "get_effect", None, 0, 1, 0, 0, 0, 0, 1),
        ("timeline", "get_timeline", None, 0, 1, 0, 0, 0, 0, 1),
        ("playState", "get_playState", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentTime", "get_currentTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("startTime", "get_startTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("playbackRate", "get_playbackRate", "set_playbackRate", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancel", "fn_cancel", 0, 0, 1, 0, 0, 0, 0),
        ("pause", "fn_pause", 0, 0, 1, 0, 0, 0, 0),
        ("play", "fn_play", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_animatorName(self):
        val = self._attr.get('animatorName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.animatorName -> get attr')

    def get_effect(self):
        val = self._attr.get('effect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.effect -> get attr')

    def get_timeline(self):
        val = self._attr.get('timeline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.timeline -> get attr')

    def get_playState(self):
        val = self._attr.get('playState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.playState -> get attr')

    def get_currentTime(self):
        val = self._attr.get('currentTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.currentTime -> get attr')

    def get_startTime(self):
        val = self._attr.get('startTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.startTime -> get attr')

    def get_playbackRate(self):
        val = self._attr.get('playbackRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.playbackRate -> get attr')

    def set_playbackRate(self, val):
        self._attr['playbackRate'] = val

    def fn_cancel(self, *args):
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.cancel{tuple(args)} -> method')

    def fn_pause(self, *args):
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.pause{tuple(args)} -> method')

    def fn_play(self, *args):
        logger.debug(f'patch -> v8_worklet_animation.py -> WorkletAnimation.play{tuple(args)} -> method')
