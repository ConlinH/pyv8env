from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class SpeechSynthesisUtterance(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SpeechSynthesisUtterance, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("text", "get_text", "set_text", 0, 1, 0, 0, 0, 0, 1),
        ("lang", "get_lang", "set_lang", 0, 1, 0, 0, 0, 0, 1),
        ("voice", "get_voice", "set_voice", 0, 1, 0, 0, 0, 0, 1),
        ("volume", "get_volume", "set_volume", 0, 1, 0, 0, 0, 0, 1),
        ("rate", "get_rate", "set_rate", 0, 1, 0, 0, 0, 0, 1),
        ("pitch", "get_pitch", "set_pitch", 0, 1, 0, 0, 0, 0, 1),
        ("onstart", "get_onstart", "set_onstart", 0, 1, 0, 0, 0, 0, 1),
        ("onend", "get_onend", "set_onend", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onpause", "get_onpause", "set_onpause", 0, 1, 0, 0, 0, 0, 1),
        ("onresume", "get_onresume", "set_onresume", 0, 1, 0, 0, 0, 0, 1),
        ("onmark", "get_onmark", "set_onmark", 0, 1, 0, 0, 0, 0, 1),
        ("onboundary", "get_onboundary", "set_onboundary", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.text -> get attr')

    def set_text(self, val):
        self._attr['text'] = val

    def get_lang(self):
        val = self._attr.get('lang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.lang -> get attr')

    def set_lang(self, val):
        self._attr['lang'] = val

    def get_voice(self):
        val = self._attr.get('voice')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.voice -> get attr')

    def set_voice(self, val):
        self._attr['voice'] = val

    def get_volume(self):
        val = self._attr.get('volume')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.volume -> get attr')

    def set_volume(self, val):
        self._attr['volume'] = val

    def get_rate(self):
        val = self._attr.get('rate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.rate -> get attr')

    def set_rate(self, val):
        self._attr['rate'] = val

    def get_pitch(self):
        val = self._attr.get('pitch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.pitch -> get attr')

    def set_pitch(self, val):
        self._attr['pitch'] = val

    def get_onstart(self):
        val = self._attr.get('onstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.onstart -> get attr')

    def set_onstart(self, val):
        self._attr['onstart'] = val

    def get_onend(self):
        val = self._attr.get('onend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.onend -> get attr')

    def set_onend(self, val):
        self._attr['onend'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onpause(self):
        val = self._attr.get('onpause')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.onpause -> get attr')

    def set_onpause(self, val):
        self._attr['onpause'] = val

    def get_onresume(self):
        val = self._attr.get('onresume')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.onresume -> get attr')

    def set_onresume(self, val):
        self._attr['onresume'] = val

    def get_onmark(self):
        val = self._attr.get('onmark')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.onmark -> get attr')

    def set_onmark(self, val):
        self._attr['onmark'] = val

    def get_onboundary(self):
        val = self._attr.get('onboundary')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis_utterance.py -> SpeechSynthesisUtterance.onboundary -> get attr')

    def set_onboundary(self, val):
        self._attr['onboundary'] = val
