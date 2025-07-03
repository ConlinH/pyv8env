from .flags import *
from .v8_base_audio_context import BaseAudioContext


@construct_110001
class AudioContext(BaseAudioContext):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioContext, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("baseLatency", "get_baseLatency", None, 0, 1, 0, 0, 0, 0, 1),
        ("outputLatency", "get_outputLatency", None, 0, 1, 0, 0, 0, 0, 1),
        ("playoutStats", "get_playoutStats", None, 0, 1, 0, 0, 0, 0, 1),
        ("sinkId", "get_sinkId", None, 0, 1, 0, 0, 0, 0, 1),
        ("onsinkchange", "get_onsinkchange", "set_onsinkchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("createMediaElementSource", "fn_createMediaElementSource", 1, 0, 1, 0, 0, 0, 0),
        ("createMediaStreamDestination", "fn_createMediaStreamDestination", 0, 0, 1, 0, 0, 0, 0),
        ("createMediaStreamSource", "fn_createMediaStreamSource", 1, 0, 1, 0, 0, 0, 0),
        ("getOutputTimestamp", "fn_getOutputTimestamp", 0, 0, 1, 0, 0, 0, 0),
        ("resume", "fn_resume", 0, 0, 1, 0, 1, 0, 0),
        ("suspend", "fn_suspend", 0, 0, 1, 0, 1, 0, 0),
        ("setSinkId", "fn_setSinkId", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_baseLatency(self):
        val = self._attr.get('baseLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.baseLatency -> get attr')

    def get_outputLatency(self):
        val = self._attr.get('outputLatency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.outputLatency -> get attr')

    def get_playoutStats(self):
        val = self._attr.get('playoutStats')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.playoutStats -> get attr')

    def get_sinkId(self):
        val = self._attr.get('sinkId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.sinkId -> get attr')

    def get_onsinkchange(self):
        val = self._attr.get('onsinkchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.onsinkchange -> get attr')

    def set_onsinkchange(self, val):
        self._attr['onsinkchange'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.close{tuple(args)} -> method')

    def fn_createMediaElementSource(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.createMediaElementSource{tuple(args)} -> method')

    def fn_createMediaStreamDestination(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.createMediaStreamDestination{tuple(args)} -> method')

    def fn_createMediaStreamSource(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.createMediaStreamSource{tuple(args)} -> method')

    def fn_getOutputTimestamp(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.getOutputTimestamp{tuple(args)} -> method')

    def fn_resume(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.resume{tuple(args)} -> method')

    def fn_suspend(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.suspend{tuple(args)} -> method')

    def fn_setSinkId(self, *args):
        logger.debug(f'patch -> v8_audio_context.py -> AudioContext.setSinkId{tuple(args)} -> method')
