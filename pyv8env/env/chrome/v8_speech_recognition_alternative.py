from .flags import *


@construct_000000
class SpeechRecognitionAlternative:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("transcript", "get_transcript", None, 0, 1, 0, 0, 0, 0, 1),
        ("confidence", "get_confidence", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_transcript(self):
        val = self._attr.get('transcript')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_alternative.py -> SpeechRecognitionAlternative.transcript -> get attr')

    def get_confidence(self):
        val = self._attr.get('confidence')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition_alternative.py -> SpeechRecognitionAlternative.confidence -> get attr')
