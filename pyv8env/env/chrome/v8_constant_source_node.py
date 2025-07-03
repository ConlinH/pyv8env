from .flags import *
from .v8_audio_scheduled_source_node import AudioScheduledSourceNode


@construct_111001
class ConstantSourceNode(AudioScheduledSourceNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ConstantSourceNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("offset", "get_offset", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_offset(self):
        val = self._attr.get('offset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_constant_source_node.py -> ConstantSourceNode.offset -> get attr')
