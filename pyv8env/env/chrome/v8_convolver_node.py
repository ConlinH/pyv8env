from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class ConvolverNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ConvolverNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("buffer", "get_buffer", "set_buffer", 0, 1, 0, 0, 0, 0, 1),
        ("normalize", "get_normalize", "set_normalize", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_buffer(self):
        val = self._attr.get('buffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_convolver_node.py -> ConvolverNode.buffer -> get attr')

    def set_buffer(self, val):
        self._attr['buffer'] = val

    def get_normalize(self):
        val = self._attr.get('normalize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_convolver_node.py -> ConvolverNode.normalize -> get attr')

    def set_normalize(self, val):
        self._attr['normalize'] = val
