from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class BiquadFilterNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BiquadFilterNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("frequency", "get_frequency", None, 0, 1, 0, 0, 0, 0, 1),
        ("detune", "get_detune", None, 0, 1, 0, 0, 0, 0, 1),
        ("Q", "get_Q", None, 0, 1, 0, 0, 0, 0, 1),
        ("gain", "get_gain", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getFrequencyResponse", "fn_getFrequencyResponse", 3, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_biquad_filter_node.py -> BiquadFilterNode.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_frequency(self):
        val = self._attr.get('frequency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_biquad_filter_node.py -> BiquadFilterNode.frequency -> get attr')

    def get_detune(self):
        val = self._attr.get('detune')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_biquad_filter_node.py -> BiquadFilterNode.detune -> get attr')

    def get_Q(self):
        val = self._attr.get('Q')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_biquad_filter_node.py -> BiquadFilterNode.Q -> get attr')

    def get_gain(self):
        val = self._attr.get('gain')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_biquad_filter_node.py -> BiquadFilterNode.gain -> get attr')

    def fn_getFrequencyResponse(self, *args):
        logger.debug(f'patch -> v8_biquad_filter_node.py -> BiquadFilterNode.getFrequencyResponse{tuple(args)} -> method')
