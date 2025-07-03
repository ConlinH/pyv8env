from .flags import *
from .v8_worklet_global_scope import WorkletGlobalScope


@construct_100031
class AudioWorkletGlobalScope(WorkletGlobalScope):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioWorkletGlobalScope, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("currentFrame", "get_currentFrame", None, 0, 0, 0, 0, 0, 0, 1),
        ("currentTime", "get_currentTime", None, 0, 0, 0, 0, 0, 0, 1),
        ("sampleRate", "get_sampleRate", None, 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("registerProcessor", "fn_registerProcessor", 2, 0, 0, 0, 0, 0, 0),

    )

    def get_currentFrame(self):
        val = self._attr.get('currentFrame')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_worklet_global_scope.py -> AudioWorkletGlobalScope.currentFrame -> get attr')

    def get_currentTime(self):
        val = self._attr.get('currentTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_worklet_global_scope.py -> AudioWorkletGlobalScope.currentTime -> get attr')

    def get_sampleRate(self):
        val = self._attr.get('sampleRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_worklet_global_scope.py -> AudioWorkletGlobalScope.sampleRate -> get attr')

    def fn_registerProcessor(self, *args):
        logger.debug(f'patch -> v8_audio_worklet_global_scope.py -> AudioWorkletGlobalScope.registerProcessor{tuple(args)} -> method')
