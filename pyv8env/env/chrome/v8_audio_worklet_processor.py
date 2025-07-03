from .flags import *


@construct_110001
class AudioWorkletProcessor:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("port", "get_port", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_worklet_processor.py -> AudioWorkletProcessor.port -> get attr')
