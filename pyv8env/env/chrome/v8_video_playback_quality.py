from .flags import *


@construct_100001
class VideoPlaybackQuality:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("creationTime", "get_creationTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("totalVideoFrames", "get_totalVideoFrames", None, 0, 1, 0, 0, 0, 0, 1),
        ("droppedVideoFrames", "get_droppedVideoFrames", None, 0, 1, 0, 0, 0, 0, 1),
        ("corruptedVideoFrames", "get_corruptedVideoFrames", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_creationTime(self):
        val = self._attr.get('creationTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_playback_quality.py -> VideoPlaybackQuality.creationTime -> get attr')

    def get_totalVideoFrames(self):
        val = self._attr.get('totalVideoFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_playback_quality.py -> VideoPlaybackQuality.totalVideoFrames -> get attr')

    def get_droppedVideoFrames(self):
        val = self._attr.get('droppedVideoFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_playback_quality.py -> VideoPlaybackQuality.droppedVideoFrames -> get attr')

    def get_corruptedVideoFrames(self):
        val = self._attr.get('corruptedVideoFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_playback_quality.py -> VideoPlaybackQuality.corruptedVideoFrames -> get attr')
