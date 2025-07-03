from .flags import *
from .v8_audio_node import AudioNode


@construct_100001
class AudioDestinationNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioDestinationNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("maxChannelCount", "get_maxChannelCount", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_maxChannelCount(self):
        val = self._attr.get('maxChannelCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_destination_node.py -> AudioDestinationNode.maxChannelCount -> get attr')
