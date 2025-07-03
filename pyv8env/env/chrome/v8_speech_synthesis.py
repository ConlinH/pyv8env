from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class SpeechSynthesis(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SpeechSynthesis, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("pending", "get_pending", None, 0, 1, 0, 0, 0, 0, 1),
        ("speaking", "get_speaking", None, 0, 1, 0, 0, 0, 0, 1),
        ("paused", "get_paused", None, 0, 1, 0, 0, 0, 0, 1),
        ("onvoiceschanged", "get_onvoiceschanged", "set_onvoiceschanged", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancel", "fn_cancel", 0, 0, 1, 0, 0, 0, 0),
        ("getVoices", "fn_getVoices", 0, 0, 1, 0, 0, 0, 0),
        ("pause", "fn_pause", 0, 0, 1, 0, 0, 0, 0),
        ("resume", "fn_resume", 0, 0, 1, 0, 0, 0, 0),
        ("speak", "fn_speak", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_pending(self):
        val = self._attr.get('pending')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.pending -> get attr')

    def get_speaking(self):
        val = self._attr.get('speaking')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.speaking -> get attr')

    def get_paused(self):
        val = self._attr.get('paused')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.paused -> get attr')

    def get_onvoiceschanged(self):
        val = self._attr.get('onvoiceschanged')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.onvoiceschanged -> get attr')

    def set_onvoiceschanged(self, val):
        self._attr['onvoiceschanged'] = val

    def fn_cancel(self, *args):
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.cancel{tuple(args)} -> method')

    def fn_getVoices(self, *args):
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.getVoices{tuple(args)} -> method')

    def fn_pause(self, *args):
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.pause{tuple(args)} -> method')

    def fn_resume(self, *args):
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.resume{tuple(args)} -> method')

    def fn_speak(self, *args):
        logger.debug(f'patch -> v8_speech_synthesis.py -> SpeechSynthesis.speak{tuple(args)} -> method')
