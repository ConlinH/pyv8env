from .flags import *


@construct_110001
class VideoTrackGenerator:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("writable", "get_writable", None, 0, 1, 0, 0, 0, 0, 1),
        ("muted", "get_muted", "set_muted", 0, 1, 0, 0, 0, 0, 1),
        ("track", "get_track", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_writable(self):
        val = self._attr.get('writable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track_generator.py -> VideoTrackGenerator.writable -> get attr')

    def get_muted(self):
        val = self._attr.get('muted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track_generator.py -> VideoTrackGenerator.muted -> get attr')

    def set_muted(self, val):
        self._attr['muted'] = val

    def get_track(self):
        val = self._attr.get('track')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_track_generator.py -> VideoTrackGenerator.track -> get attr')
