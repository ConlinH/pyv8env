from .flags import *
from .v8_event_target import EventTarget


@construct_010000
class SpeechRecognition(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SpeechRecognition, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("grammars", "get_grammars", "set_grammars", 0, 1, 0, 0, 0, 0, 1),
        ("lang", "get_lang", "set_lang", 0, 1, 0, 0, 0, 0, 1),
        ("continuous", "get_continuous", "set_continuous", 0, 1, 0, 0, 0, 0, 1),
        ("interimResults", "get_interimResults", "set_interimResults", 0, 1, 0, 0, 0, 0, 1),
        ("maxAlternatives", "get_maxAlternatives", "set_maxAlternatives", 0, 1, 0, 0, 0, 0, 1),
        ("onaudiostart", "get_onaudiostart", "set_onaudiostart", 0, 1, 0, 0, 0, 0, 1),
        ("onsoundstart", "get_onsoundstart", "set_onsoundstart", 0, 1, 0, 0, 0, 0, 1),
        ("onspeechstart", "get_onspeechstart", "set_onspeechstart", 0, 1, 0, 0, 0, 0, 1),
        ("onspeechend", "get_onspeechend", "set_onspeechend", 0, 1, 0, 0, 0, 0, 1),
        ("onsoundend", "get_onsoundend", "set_onsoundend", 0, 1, 0, 0, 0, 0, 1),
        ("onaudioend", "get_onaudioend", "set_onaudioend", 0, 1, 0, 0, 0, 0, 1),
        ("onresult", "get_onresult", "set_onresult", 0, 1, 0, 0, 0, 0, 1),
        ("onnomatch", "get_onnomatch", "set_onnomatch", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onstart", "get_onstart", "set_onstart", 0, 1, 0, 0, 0, 0, 1),
        ("onend", "get_onend", "set_onend", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 0, 0, 0),
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_grammars(self):
        val = self._attr.get('grammars')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.grammars -> get attr')

    def set_grammars(self, val):
        self._attr['grammars'] = val

    def get_lang(self):
        val = self._attr.get('lang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.lang -> get attr')

    def set_lang(self, val):
        self._attr['lang'] = val

    def get_continuous(self):
        val = self._attr.get('continuous')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.continuous -> get attr')

    def set_continuous(self, val):
        self._attr['continuous'] = val

    def get_interimResults(self):
        val = self._attr.get('interimResults')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.interimResults -> get attr')

    def set_interimResults(self, val):
        self._attr['interimResults'] = val

    def get_maxAlternatives(self):
        val = self._attr.get('maxAlternatives')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.maxAlternatives -> get attr')

    def set_maxAlternatives(self, val):
        self._attr['maxAlternatives'] = val

    def get_onaudiostart(self):
        val = self._attr.get('onaudiostart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onaudiostart -> get attr')

    def set_onaudiostart(self, val):
        self._attr['onaudiostart'] = val

    def get_onsoundstart(self):
        val = self._attr.get('onsoundstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onsoundstart -> get attr')

    def set_onsoundstart(self, val):
        self._attr['onsoundstart'] = val

    def get_onspeechstart(self):
        val = self._attr.get('onspeechstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onspeechstart -> get attr')

    def set_onspeechstart(self, val):
        self._attr['onspeechstart'] = val

    def get_onspeechend(self):
        val = self._attr.get('onspeechend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onspeechend -> get attr')

    def set_onspeechend(self, val):
        self._attr['onspeechend'] = val

    def get_onsoundend(self):
        val = self._attr.get('onsoundend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onsoundend -> get attr')

    def set_onsoundend(self, val):
        self._attr['onsoundend'] = val

    def get_onaudioend(self):
        val = self._attr.get('onaudioend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onaudioend -> get attr')

    def set_onaudioend(self, val):
        self._attr['onaudioend'] = val

    def get_onresult(self):
        val = self._attr.get('onresult')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onresult -> get attr')

    def set_onresult(self, val):
        self._attr['onresult'] = val

    def get_onnomatch(self):
        val = self._attr.get('onnomatch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onnomatch -> get attr')

    def set_onnomatch(self, val):
        self._attr['onnomatch'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onstart(self):
        val = self._attr.get('onstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onstart -> get attr')

    def set_onstart(self, val):
        self._attr['onstart'] = val

    def get_onend(self):
        val = self._attr.get('onend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.onend -> get attr')

    def set_onend(self, val):
        self._attr['onend'] = val

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.abort{tuple(args)} -> method')

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.start{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_speech_recognition.py -> SpeechRecognition.stop{tuple(args)} -> method')
