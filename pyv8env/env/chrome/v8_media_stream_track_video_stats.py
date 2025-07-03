from .flags import *


@construct_100001
class MediaStreamTrackVideoStats:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("deliveredFrames", "get_deliveredFrames", None, 0, 1, 0, 0, 0, 0, 1),
        ("discardedFrames", "get_discardedFrames", None, 0, 1, 0, 0, 0, 0, 1),
        ("totalFrames", "get_totalFrames", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_deliveredFrames(self):
        val = self._attr.get('deliveredFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_video_stats.py -> MediaStreamTrackVideoStats.deliveredFrames -> get attr')

    def get_discardedFrames(self):
        val = self._attr.get('discardedFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_video_stats.py -> MediaStreamTrackVideoStats.discardedFrames -> get attr')

    def get_totalFrames(self):
        val = self._attr.get('totalFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_video_stats.py -> MediaStreamTrackVideoStats.totalFrames -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_media_stream_track_video_stats.py -> MediaStreamTrackVideoStats.toJSON{tuple(args)} -> method')
