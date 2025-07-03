from .flags import *


@construct_100001
class AudioPlayoutStats:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("fallbackFramesDuration", "get_fallbackFramesDuration", None, 0, 1, 0, 0, 0, 0, 1),
        ("fallbackFramesEvents", "get_fallbackFramesEvents", None, 0, 1, 0, 0, 0, 0, 1),
        ("totalFramesDuration", "get_totalFramesDuration", None, 0, 1, 0, 0, 0, 0, 1),
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

    def get_fallbackFramesDuration(self):
        val = self._attr.get('fallbackFramesDuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.fallbackFramesDuration -> get attr')

    def get_fallbackFramesEvents(self):
        val = self._attr.get('fallbackFramesEvents')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.fallbackFramesEvents -> get attr')

    def get_totalFramesDuration(self):
        val = self._attr.get('totalFramesDuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.totalFramesDuration -> get attr')

    def get_averageLatency(self):
        val = self._attr.get('averageLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.averageLatency -> get attr')

    def get_minimumLatency(self):
        val = self._attr.get('minimumLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.minimumLatency -> get attr')

    def get_maximumLatency(self):
        val = self._attr.get('maximumLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.maximumLatency -> get attr')

    def fn_resetLatency(self, *args):
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.resetLatency{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_audio_playout_stats.py -> AudioPlayoutStats.toJSON{tuple(args)} -> method')
