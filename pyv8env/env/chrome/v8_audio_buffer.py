from .flags import *


@construct_111001
class AudioBuffer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),
        ("sampleRate", "get_sampleRate", None, 0, 1, 0, 0, 0, 0, 1),
        ("numberOfChannels", "get_numberOfChannels", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("copyFromChannel", "fn_copyFromChannel", 2, 0, 1, 0, 0, 0, 0),
        ("copyToChannel", "fn_copyToChannel", 2, 0, 1, 0, 0, 0, 0),
        ("getChannelData", "fn_getChannelData", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer.py -> AudioBuffer.length -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer.py -> AudioBuffer.duration -> get attr')

    def get_sampleRate(self):
        val = self._attr.get('sampleRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer.py -> AudioBuffer.sampleRate -> get attr')

    def get_numberOfChannels(self):
        val = self._attr.get('numberOfChannels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer.py -> AudioBuffer.numberOfChannels -> get attr')

    def fn_copyFromChannel(self, *args):
        logger.debug(f'patch -> v8_audio_buffer.py -> AudioBuffer.copyFromChannel{tuple(args)} -> method')

    def fn_copyToChannel(self, *args):
        logger.debug(f'patch -> v8_audio_buffer.py -> AudioBuffer.copyToChannel{tuple(args)} -> method')

    def fn_getChannelData(self, *args):
        logger.debug(f'patch -> v8_audio_buffer.py -> AudioBuffer.getChannelData{tuple(args)} -> method')
