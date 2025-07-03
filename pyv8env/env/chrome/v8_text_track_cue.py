from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class TextTrackCue(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TextTrackCue, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("track", "get_track", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", "set_id", 0, 1, 0, 0, 0, 0, 1),
        ("startTime", "get_startTime", "set_startTime", 0, 1, 0, 0, 0, 0, 1),
        ("endTime", "get_endTime", "set_endTime", 0, 1, 0, 0, 0, 0, 1),
        ("pauseOnExit", "get_pauseOnExit", "set_pauseOnExit", 0, 1, 0, 0, 0, 0, 1),
        ("onenter", "get_onenter", "set_onenter", 0, 1, 0, 0, 0, 0, 1),
        ("onexit", "get_onexit", "set_onexit", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_track(self):
        val = self._attr.get('track')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_cue.py -> TextTrackCue.track -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_cue.py -> TextTrackCue.id -> get attr')

    def set_id(self, val):
        self._attr['id'] = val

    def get_startTime(self):
        val = self._attr.get('startTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_cue.py -> TextTrackCue.startTime -> get attr')

    def set_startTime(self, val):
        self._attr['startTime'] = val

    def get_endTime(self):
        val = self._attr.get('endTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_cue.py -> TextTrackCue.endTime -> get attr')

    def set_endTime(self, val):
        self._attr['endTime'] = val

    def get_pauseOnExit(self):
        val = self._attr.get('pauseOnExit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_cue.py -> TextTrackCue.pauseOnExit -> get attr')

    def set_pauseOnExit(self, val):
        self._attr['pauseOnExit'] = val

    def get_onenter(self):
        val = self._attr.get('onenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_cue.py -> TextTrackCue.onenter -> get attr')

    def set_onenter(self, val):
        self._attr['onenter'] = val

    def get_onexit(self):
        val = self._attr.get('onexit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_cue.py -> TextTrackCue.onexit -> get attr')

    def set_onexit(self, val):
        self._attr['onexit'] = val
