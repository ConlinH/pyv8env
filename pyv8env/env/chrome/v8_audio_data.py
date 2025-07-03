from .flags import *


@construct_111001
class AudioData:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("format", "get_format", None, 0, 1, 0, 0, 0, 0, 1),
        ("sampleRate", "get_sampleRate", None, 0, 1, 0, 0, 0, 0, 1),
        ("numberOfFrames", "get_numberOfFrames", None, 0, 1, 0, 0, 0, 0, 1),
        ("numberOfChannels", "get_numberOfChannels", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("allocationSize", "fn_allocationSize", 1, 0, 1, 0, 0, 0, 0),
        ("clone", "fn_clone", 0, 0, 1, 0, 0, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("copyTo", "fn_copyTo", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_format(self):
        val = self._attr.get('format')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.format -> get attr')

    def get_sampleRate(self):
        val = self._attr.get('sampleRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.sampleRate -> get attr')

    def get_numberOfFrames(self):
        val = self._attr.get('numberOfFrames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.numberOfFrames -> get attr')

    def get_numberOfChannels(self):
        val = self._attr.get('numberOfChannels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.numberOfChannels -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.duration -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.timestamp -> get attr')

    def fn_allocationSize(self, *args):
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.allocationSize{tuple(args)} -> method')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.clone{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.close{tuple(args)} -> method')

    def fn_copyTo(self, *args):
        logger.debug(f'patch -> v8_audio_data.py -> AudioData.copyTo{tuple(args)} -> method')
