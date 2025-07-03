from .flags import *
from .v8_event import Event


@construct_011000
class SpeechRecognitionErrorEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SpeechRecognitionErrorEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("error", "get_error", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_error(self):
        val = self._attr.get('error')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_error_event.py -> SpeechRecognitionErrorEvent.error -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_error_event.py -> SpeechRecognitionErrorEvent.message -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_error_event.py -> SpeechRecognitionErrorEvent.isTrusted -> get attr')
