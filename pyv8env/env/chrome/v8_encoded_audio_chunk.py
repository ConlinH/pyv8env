from .flags import *


@construct_111001
class EncodedAudioChunk:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("byteLength", "get_byteLength", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("copyTo", "fn_copyTo", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_encoded_audio_chunk.py -> EncodedAudioChunk.type -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_encoded_audio_chunk.py -> EncodedAudioChunk.timestamp -> get attr')

    def get_byteLength(self):
        val = self._attr.get('byteLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_encoded_audio_chunk.py -> EncodedAudioChunk.byteLength -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_encoded_audio_chunk.py -> EncodedAudioChunk.duration -> get attr')

    def fn_copyTo(self, *args):
        logger.debug(f'patch -> v8_encoded_audio_chunk.py -> EncodedAudioChunk.copyTo{tuple(args)} -> method')
