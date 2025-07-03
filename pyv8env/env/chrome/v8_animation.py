from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class Animation(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Animation, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("effect", "get_effect", "set_effect", 0, 1, 0, 0, 0, 0, 1),
        ("timeline", "get_timeline", "set_timeline", 0, 1, 0, 0, 0, 0, 1),
        ("startTime", "get_startTime", "set_startTime", 0, 1, 0, 0, 0, 0, 1),
        ("currentTime", "get_currentTime", "set_currentTime", 0, 1, 0, 0, 0, 0, 1),
        ("playbackRate", "get_playbackRate", "set_playbackRate", 0, 1, 0, 0, 0, 0, 1),
        ("playState", "get_playState", None, 0, 1, 0, 0, 0, 0, 1),
        ("replaceState", "get_replaceState", None, 0, 1, 0, 0, 0, 0, 1),
        ("pending", "get_pending", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", "set_id", 0, 1, 0, 0, 0, 0, 1),
        ("onfinish", "get_onfinish", "set_onfinish", 0, 1, 0, 0, 0, 0, 1),
        ("oncancel", "get_oncancel", "set_oncancel", 0, 1, 0, 0, 0, 0, 1),
        ("onremove", "get_onremove", "set_onremove", 0, 1, 0, 0, 0, 0, 1),
        ("finished", "get_finished", None, 0, 1, 0, 1, 0, 0, 1),
        ("ready", "get_ready", None, 0, 1, 0, 1, 0, 0, 1),
        ("progress", "get_progress", None, 0, 1, 0, 0, 0, 0, 1),
        ("rangeStart", "get_rangeStart", "set_rangeStart", 0, 1, 0, 0, 0, 0, 1),
        ("rangeEnd", "get_rangeEnd", "set_rangeEnd", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancel", "fn_cancel", 0, 0, 1, 0, 0, 0, 0),
        ("commitStyles", "fn_commitStyles", 0, 0, 1, 0, 0, 0, 0),
        ("finish", "fn_finish", 0, 0, 1, 0, 0, 0, 0),
        ("pause", "fn_pause", 0, 0, 1, 0, 0, 0, 0),
        ("persist", "fn_persist", 0, 0, 1, 0, 0, 0, 0),
        ("play", "fn_play", 0, 0, 1, 0, 0, 0, 0),
        ("reverse", "fn_reverse", 0, 0, 1, 0, 0, 0, 0),
        ("updatePlaybackRate", "fn_updatePlaybackRate", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_effect(self):
        val = self._attr.get('effect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.effect -> get attr')

    def set_effect(self, val):
        self._attr['effect'] = val

    def get_timeline(self):
        val = self._attr.get('timeline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.timeline -> get attr')

    def set_timeline(self, val):
        self._attr['timeline'] = val

    def get_startTime(self):
        val = self._attr.get('startTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.startTime -> get attr')

    def set_startTime(self, val):
        self._attr['startTime'] = val

    def get_currentTime(self):
        val = self._attr.get('currentTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.currentTime -> get attr')

    def set_currentTime(self, val):
        self._attr['currentTime'] = val

    def get_playbackRate(self):
        val = self._attr.get('playbackRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.playbackRate -> get attr')

    def set_playbackRate(self, val):
        self._attr['playbackRate'] = val

    def get_playState(self):
        val = self._attr.get('playState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.playState -> get attr')

    def get_replaceState(self):
        val = self._attr.get('replaceState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.replaceState -> get attr')

    def get_pending(self):
        val = self._attr.get('pending')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.pending -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.id -> get attr')

    def set_id(self, val):
        self._attr['id'] = val

    def get_onfinish(self):
        val = self._attr.get('onfinish')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.onfinish -> get attr')

    def set_onfinish(self, val):
        self._attr['onfinish'] = val

    def get_oncancel(self):
        val = self._attr.get('oncancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.oncancel -> get attr')

    def set_oncancel(self, val):
        self._attr['oncancel'] = val

    def get_onremove(self):
        val = self._attr.get('onremove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.onremove -> get attr')

    def set_onremove(self, val):
        self._attr['onremove'] = val

    def get_finished(self):
        val = self._attr.get('finished')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.finished -> get attr')

    def get_ready(self):
        val = self._attr.get('ready')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.ready -> get attr')

    def get_progress(self):
        val = self._attr.get('progress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.progress -> get attr')

    def get_rangeStart(self):
        val = self._attr.get('rangeStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.rangeStart -> get attr')

    def set_rangeStart(self, val):
        self._attr['rangeStart'] = val

    def get_rangeEnd(self):
        val = self._attr.get('rangeEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation.py -> Animation.rangeEnd -> get attr')

    def set_rangeEnd(self, val):
        self._attr['rangeEnd'] = val

    def fn_cancel(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.cancel{tuple(args)} -> method')

    def fn_commitStyles(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.commitStyles{tuple(args)} -> method')

    def fn_finish(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.finish{tuple(args)} -> method')

    def fn_pause(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.pause{tuple(args)} -> method')

    def fn_persist(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.persist{tuple(args)} -> method')

    def fn_play(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.play{tuple(args)} -> method')

    def fn_reverse(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.reverse{tuple(args)} -> method')

    def fn_updatePlaybackRate(self, *args):
        logger.debug(f'patch -> v8_animation.py -> Animation.updatePlaybackRate{tuple(args)} -> method')
