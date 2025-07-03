from .flags import *


@construct_100001
class MediaStreamTrackAudioStats:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("deliveredFrames", "get_deliveredFrames", None, 0, 1, 0, 0, 0, 0, 1),
        ("deliveredFramesDuration", "get_deliveredFramesDuration", None, 0, 1, 0, 0, 0, 0, 1),
        ("totalFrames", "get_totalFrames", None, 0, 1, 0, 0, 0, 0, 1),
        ("totalFramesDuration", "get_totalFramesDuration", None, 0, 1, 0, 0, 0, 0, 1),
        ("latency", "get_latency", None, 0, 1, 0, 0, 0, 0, 1),
        ("averageLatency", "get_averageLatency", None, 0, 1, 0, 0, 0, 0, 1),
        ("minimumLatency", "get_minimumLatency", None, 0, 1, 0, 0, 0, 0, 1),
        ("maximumLatency", "get_maximumLatency", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("resetLatency", "fn_resetLatency", 0, 0, 1, 0, 0, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_deliveredFrames(self):
        val = self._attr.get('deliveredFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.deliveredFrames -> get attr')

    def get_deliveredFramesDuration(self):
        val = self._attr.get('deliveredFramesDuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.deliveredFramesDuration -> get attr')

    def get_totalFrames(self):
        val = self._attr.get('totalFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.totalFrames -> get attr')

    def get_totalFramesDuration(self):
        val = self._attr.get('totalFramesDuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.totalFramesDuration -> get attr')

    def get_latency(self):
        val = self._attr.get('latency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.latency -> get attr')

    def get_averageLatency(self):
        val = self._attr.get('averageLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.averageLatency -> get attr')

    def get_minimumLatency(self):
        val = self._attr.get('minimumLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.minimumLatency -> get attr')

    def get_maximumLatency(self):
        val = self._attr.get('maximumLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.maximumLatency -> get attr')

    def fn_resetLatency(self, *args):
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.resetLatency{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_media_stream_track_audio_stats.py -> MediaStreamTrackAudioStats.toJSON{tuple(args)} -> method')
