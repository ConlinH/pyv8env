from .flags import *
from .v8_event import Event


@construct_011000
class SpeechRecognitionEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SpeechRecognitionEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("resultIndex", "get_resultIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("results", "get_results", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_resultIndex(self):
        val = self._attr.get('resultIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_event.py -> SpeechRecognitionEvent.resultIndex -> get attr')

    def get_results(self):
        val = self._attr.get('results')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_event.py -> SpeechRecognitionEvent.results -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_event.py -> SpeechRecognitionEvent.isTrusted -> get attr')
