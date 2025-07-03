from .flags import *


@construct_100001
class SpeechSynthesisVoice:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("voiceURI", "get_voiceURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("lang", "get_lang", None, 0, 1, 0, 0, 0, 0, 1),
        ("localService", "get_localService", None, 0, 1, 0, 0, 0, 0, 1),
        ("default", "get_default", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_voiceURI(self):
        val = self._attr.get('voiceURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_voice.py -> SpeechSynthesisVoice.voiceURI -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_voice.py -> SpeechSynthesisVoice.name -> get attr')

    def get_lang(self):
        val = self._attr.get('lang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_voice.py -> SpeechSynthesisVoice.lang -> get attr')

    def get_localService(self):
        val = self._attr.get('localService')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_voice.py -> SpeechSynthesisVoice.localService -> get attr')

    def get_default(self):
        val = self._attr.get('default')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_voice.py -> SpeechSynthesisVoice.default -> get attr')
