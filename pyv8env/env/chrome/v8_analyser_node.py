from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class AnalyserNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AnalyserNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("fftSize", "get_fftSize", "set_fftSize", 0, 1, 0, 0, 0, 0, 1),
        ("frequencyBinCount", "get_frequencyBinCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("minDecibels", "get_minDecibels", "set_minDecibels", 0, 1, 0, 0, 0, 0, 1),
        ("maxDecibels", "get_maxDecibels", "set_maxDecibels", 0, 1, 0, 0, 0, 0, 1),
        ("smoothingTimeConstant", "get_smoothingTimeConstant", "set_smoothingTimeConstant", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getByteFrequencyData", "fn_getByteFrequencyData", 1, 0, 1, 0, 0, 0, 0),
        ("getByteTimeDomainData", "fn_getByteTimeDomainData", 1, 0, 1, 0, 0, 0, 0),
        ("getFloatFrequencyData", "fn_getFloatFrequencyData", 1, 0, 1, 0, 0, 0, 0),
        ("getFloatTimeDomainData", "fn_getFloatTimeDomainData", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_fftSize(self):
        val = self._attr.get('fftSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.fftSize -> get attr')

    def set_fftSize(self, val):
        self._attr['fftSize'] = val

    def get_frequencyBinCount(self):
        val = self._attr.get('frequencyBinCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.frequencyBinCount -> get attr')

    def get_minDecibels(self):
        val = self._attr.get('minDecibels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.minDecibels -> get attr')

    def set_minDecibels(self, val):
        self._attr['minDecibels'] = val

    def get_maxDecibels(self):
        val = self._attr.get('maxDecibels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.maxDecibels -> get attr')

    def set_maxDecibels(self, val):
        self._attr['maxDecibels'] = val

    def get_smoothingTimeConstant(self):
        val = self._attr.get('smoothingTimeConstant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.smoothingTimeConstant -> get attr')

    def set_smoothingTimeConstant(self, val):
        self._attr['smoothingTimeConstant'] = val

    def fn_getByteFrequencyData(self, *args):
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.getByteFrequencyData{tuple(args)} -> method')

    def fn_getByteTimeDomainData(self, *args):
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.getByteTimeDomainData{tuple(args)} -> method')

    def fn_getFloatFrequencyData(self, *args):
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.getFloatFrequencyData{tuple(args)} -> method')

    def fn_getFloatTimeDomainData(self, *args):
        logger.debug(f'patch -> v8_analyser_node.py -> AnalyserNode.getFloatTimeDomainData{tuple(args)} -> method')
