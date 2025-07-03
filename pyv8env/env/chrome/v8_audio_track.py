from .flags import *


@construct_100001
class AudioTrack:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("kind", "get_kind", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", None, 0, 1, 0, 0, 0, 0, 1),
        ("language", "get_language", None, 0, 1, 0, 0, 0, 0, 1),
        ("enabled", "get_enabled", "set_enabled", 0, 1, 0, 0, 0, 0, 1),
        ("sourceBuffer", "get_sourceBuffer", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_track.py -> AudioTrack.id -> get attr')

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_track.py -> AudioTrack.kind -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_track.py -> AudioTrack.label -> get attr')

    def get_language(self):
        val = self._attr.get('language')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_track.py -> AudioTrack.language -> get attr')

    def get_enabled(self):
        val = self._attr.get('enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_track.py -> AudioTrack.enabled -> get attr')

    def set_enabled(self, val):
        self._attr['enabled'] = val

    def get_sourceBuffer(self):
        val = self._attr.get('sourceBuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_track.py -> AudioTrack.sourceBuffer -> get attr')
