from .flags import *
from .v8_audio_node import AudioNode


@construct_112001
class AudioWorkletNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioWorkletNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("parameters", "get_parameters", None, 0, 1, 0, 0, 0, 0, 1),
        ("port", "get_port", None, 0, 1, 0, 0, 0, 0, 1),
        ("onprocessorerror", "get_onprocessorerror", "set_onprocessorerror", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_parameters(self):
        val = self._attr.get('parameters')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_worklet_node.py -> AudioWorkletNode.parameters -> get attr')

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_worklet_node.py -> AudioWorkletNode.port -> get attr')

    def get_onprocessorerror(self):
        val = self._attr.get('onprocessorerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_worklet_node.py -> AudioWorkletNode.onprocessorerror -> get attr')

    def set_onprocessorerror(self, val):
        self._attr['onprocessorerror'] = val
