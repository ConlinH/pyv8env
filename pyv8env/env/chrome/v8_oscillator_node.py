from .flags import *
from .v8_audio_scheduled_source_node import AudioScheduledSourceNode


@construct_111001
class OscillatorNode(AudioScheduledSourceNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(OscillatorNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("frequency", "get_frequency", None, 0, 1, 0, 0, 0, 0, 1),
        ("detune", "get_detune", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setPeriodicWave", "fn_setPeriodicWave", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_oscillator_node.py -> OscillatorNode.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_frequency(self):
        val = self._attr.get('frequency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_oscillator_node.py -> OscillatorNode.frequency -> get attr')

    def get_detune(self):
        val = self._attr.get('detune')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_oscillator_node.py -> OscillatorNode.detune -> get attr')

    def fn_setPeriodicWave(self, *args):
        logger.debug(f'patch -> v8_oscillator_node.py -> OscillatorNode.setPeriodicWave{tuple(args)} -> method')
