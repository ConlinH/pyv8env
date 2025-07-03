from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class BaseAudioContext(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BaseAudioContext, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("destination", "get_destination", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentTime", "get_currentTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("sampleRate", "get_sampleRate", None, 0, 1, 0, 0, 0, 0, 1),
        ("listener", "get_listener", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("onstatechange", "get_onstatechange", "set_onstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("audioWorklet", "get_audioWorklet", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createAnalyser", "fn_createAnalyser", 0, 0, 1, 0, 0, 0, 0),
        ("createBiquadFilter", "fn_createBiquadFilter", 0, 0, 1, 0, 0, 0, 0),
        ("createBuffer", "fn_createBuffer", 3, 0, 1, 0, 0, 0, 0),
        ("createBufferSource", "fn_createBufferSource", 0, 0, 1, 0, 0, 0, 0),
        ("createChannelMerger", "fn_createChannelMerger", 0, 0, 1, 0, 0, 0, 0),
        ("createChannelSplitter", "fn_createChannelSplitter", 0, 0, 1, 0, 0, 0, 0),
        ("createConstantSource", "fn_createConstantSource", 0, 0, 1, 0, 0, 0, 0),
        ("createConvolver", "fn_createConvolver", 0, 0, 1, 0, 0, 0, 0),
        ("createDelay", "fn_createDelay", 0, 0, 1, 0, 0, 0, 0),
        ("createDynamicsCompressor", "fn_createDynamicsCompressor", 0, 0, 1, 0, 0, 0, 0),
        ("createGain", "fn_createGain", 0, 0, 1, 0, 0, 0, 0),
        ("createIIRFilter", "fn_createIIRFilter", 2, 0, 1, 0, 0, 0, 0),
        ("createOscillator", "fn_createOscillator", 0, 0, 1, 0, 0, 0, 0),
        ("createPanner", "fn_createPanner", 0, 0, 1, 0, 0, 0, 0),
        ("createPeriodicWave", "fn_createPeriodicWave", 2, 0, 1, 0, 0, 0, 0),
        ("createScriptProcessor", "fn_createScriptProcessor", 0, 0, 1, 0, 0, 0, 0),
        ("createStereoPanner", "fn_createStereoPanner", 0, 0, 1, 0, 0, 0, 0),
        ("createWaveShaper", "fn_createWaveShaper", 0, 0, 1, 0, 0, 0, 0),
        ("decodeAudioData", "fn_decodeAudioData", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_destination(self):
        val = self._attr.get('destination')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.destination -> get attr')

    def get_currentTime(self):
        val = self._attr.get('currentTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.currentTime -> get attr')

    def get_sampleRate(self):
        val = self._attr.get('sampleRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.sampleRate -> get attr')

    def get_listener(self):
        val = self._attr.get('listener')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.listener -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.state -> get attr')

    def get_onstatechange(self):
        val = self._attr.get('onstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.onstatechange -> get attr')

    def set_onstatechange(self, val):
        self._attr['onstatechange'] = val

    def get_audioWorklet(self):
        val = self._attr.get('audioWorklet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.audioWorklet -> get attr')

    def fn_createAnalyser(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createAnalyser{tuple(args)} -> method')

    def fn_createBiquadFilter(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createBiquadFilter{tuple(args)} -> method')

    def fn_createBuffer(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createBuffer{tuple(args)} -> method')

    def fn_createBufferSource(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createBufferSource{tuple(args)} -> method')

    def fn_createChannelMerger(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createChannelMerger{tuple(args)} -> method')

    def fn_createChannelSplitter(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createChannelSplitter{tuple(args)} -> method')

    def fn_createConstantSource(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createConstantSource{tuple(args)} -> method')

    def fn_createConvolver(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createConvolver{tuple(args)} -> method')

    def fn_createDelay(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createDelay{tuple(args)} -> method')

    def fn_createDynamicsCompressor(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createDynamicsCompressor{tuple(args)} -> method')

    def fn_createGain(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createGain{tuple(args)} -> method')

    def fn_createIIRFilter(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createIIRFilter{tuple(args)} -> method')

    def fn_createOscillator(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createOscillator{tuple(args)} -> method')

    def fn_createPanner(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createPanner{tuple(args)} -> method')

    def fn_createPeriodicWave(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createPeriodicWave{tuple(args)} -> method')

    def fn_createScriptProcessor(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createScriptProcessor{tuple(args)} -> method')

    def fn_createStereoPanner(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createStereoPanner{tuple(args)} -> method')

    def fn_createWaveShaper(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.createWaveShaper{tuple(args)} -> method')

    def fn_decodeAudioData(self, *args):
        logger.debug(f'patch -> v8_base_audio_context.py -> BaseAudioContext.decodeAudioData{tuple(args)} -> method')
