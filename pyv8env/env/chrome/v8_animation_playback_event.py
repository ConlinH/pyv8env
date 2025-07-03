from .flags import *
from .v8_event import Event


@construct_111001
class AnimationPlaybackEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AnimationPlaybackEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("currentTime", "get_currentTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("timelineTime", "get_timelineTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_currentTime(self):
        val = self._attr.get('currentTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_playback_event.py -> AnimationPlaybackEvent.currentTime -> get attr')

    def get_timelineTime(self):
        val = self._attr.get('timelineTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_playback_event.py -> AnimationPlaybackEvent.timelineTime -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_playback_event.py -> AnimationPlaybackEvent.isTrusted -> get attr')
