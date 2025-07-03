from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class TextTrack(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TextTrack, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("kind", "get_kind", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", None, 0, 1, 0, 0, 0, 0, 1),
        ("language", "get_language", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("mode", "get_mode", "set_mode", 0, 1, 0, 0, 0, 0, 1),
        ("cues", "get_cues", None, 0, 1, 0, 0, 0, 0, 1),
        ("activeCues", "get_activeCues", None, 0, 1, 0, 0, 0, 0, 1),
        ("oncuechange", "get_oncuechange", "set_oncuechange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addCue", "fn_addCue", 1, 0, 1, 0, 0, 0, 0),
        ("removeCue", "fn_removeCue", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.kind -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.label -> get attr')

    def get_language(self):
        val = self._attr.get('language')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.language -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.id -> get attr')

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.mode -> get attr')

    def set_mode(self, val):
        self._attr['mode'] = val

    def get_cues(self):
        val = self._attr.get('cues')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.cues -> get attr')

    def get_activeCues(self):
        val = self._attr.get('activeCues')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.activeCues -> get attr')

    def get_oncuechange(self):
        val = self._attr.get('oncuechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.oncuechange -> get attr')

    def set_oncuechange(self, val):
        self._attr['oncuechange'] = val

    def fn_addCue(self, *args):
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.addCue{tuple(args)} -> method')

    def fn_removeCue(self, *args):
        logger.debug(f'patch -> v8_text_track.py -> TextTrack.removeCue{tuple(args)} -> method')
