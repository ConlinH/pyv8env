from .flags import *
from .v8_event import Event


@construct_112001
class SpeechSynthesisEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SpeechSynthesisEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("utterance", "get_utterance", None, 0, 1, 0, 0, 0, 0, 1),
        ("charIndex", "get_charIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("charLength", "get_charLength", None, 0, 1, 0, 0, 0, 0, 1),
        ("elapsedTime", "get_elapsedTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_utterance(self):
        val = self._attr.get('utterance')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_event.py -> SpeechSynthesisEvent.utterance -> get attr')

    def get_charIndex(self):
        val = self._attr.get('charIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_event.py -> SpeechSynthesisEvent.charIndex -> get attr')

    def get_charLength(self):
        val = self._attr.get('charLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_event.py -> SpeechSynthesisEvent.charLength -> get attr')

    def get_elapsedTime(self):
        val = self._attr.get('elapsedTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_event.py -> SpeechSynthesisEvent.elapsedTime -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_event.py -> SpeechSynthesisEvent.name -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_event.py -> SpeechSynthesisEvent.isTrusted -> get attr')
