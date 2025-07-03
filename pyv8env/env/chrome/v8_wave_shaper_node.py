from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class WaveShaperNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WaveShaperNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("curve", "get_curve", "set_curve", 0, 1, 0, 0, 0, 0, 1),
        ("oversample", "get_oversample", "set_oversample", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_curve(self):
        val = self._attr.get('curve')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wave_shaper_node.py -> WaveShaperNode.curve -> get attr')

    def set_curve(self, val):
        self._attr['curve'] = val

    def get_oversample(self):
        val = self._attr.get('oversample')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wave_shaper_node.py -> WaveShaperNode.oversample -> get attr')

    def set_oversample(self, val):
        self._attr['oversample'] = val
