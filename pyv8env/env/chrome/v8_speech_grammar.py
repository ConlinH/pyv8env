from .flags import *


@construct_010000
class SpeechGrammar:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("weight", "get_weight", "set_weight", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_grammar.py -> SpeechGrammar.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_weight(self):
        val = self._attr.get('weight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_speech_grammar.py -> SpeechGrammar.weight -> get attr')

    def set_weight(self, val):
        self._attr['weight'] = val
