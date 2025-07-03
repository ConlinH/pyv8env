from .flags import *


@construct_000100
class SpeechRecognitionResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("isFinal", "get_isFinal", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("item", "fn_item", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.length -> get attr')

    def get_isFinal(self):
        val = self._attr.get('isFinal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.isFinal -> get attr')

    def fn_item(self, *args):
        logger.debug(f'patch -> v8_speech_recognition_result.py -> SpeechRecognitionResult.item{tuple(args)} -> method')
