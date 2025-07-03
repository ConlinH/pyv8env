from .flags import *
from .v8_audio_node import AudioNode


@construct_100001
class ScriptProcessorNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ScriptProcessorNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onaudioprocess", "get_onaudioprocess", "set_onaudioprocess", 0, 1, 0, 0, 0, 0, 1),
        ("bufferSize", "get_bufferSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_onaudioprocess(self):
        val = self._attr.get('onaudioprocess')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_script_processor_node.py -> ScriptProcessorNode.onaudioprocess -> get attr')

    def set_onaudioprocess(self, val):
        self._attr['onaudioprocess'] = val

    def get_bufferSize(self):
        val = self._attr.get('bufferSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_script_processor_node.py -> ScriptProcessorNode.bufferSize -> get attr')
