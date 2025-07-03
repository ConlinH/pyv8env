from .flags import *


@construct_100001
class VideoTrack:
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
        ("selected", "get_selected", "set_selected", 0, 1, 0, 0, 0, 0, 1),
        ("sourceBuffer", "get_sourceBuffer", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track.py -> VideoTrack.id -> get attr')

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track.py -> VideoTrack.kind -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track.py -> VideoTrack.label -> get attr')

    def get_language(self):
        val = self._attr.get('language')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track.py -> VideoTrack.language -> get attr')

    def get_selected(self):
        val = self._attr.get('selected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track.py -> VideoTrack.selected -> get attr')

    def set_selected(self, val):
        self._attr['selected'] = val

    def get_sourceBuffer(self):
        val = self._attr.get('sourceBuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track.py -> VideoTrack.sourceBuffer -> get attr')
