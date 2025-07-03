from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class StereoPannerNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(StereoPannerNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("pan", "get_pan", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_pan(self):
        val = self._attr.get('pan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_stereo_panner_node.py -> StereoPannerNode.pan -> get attr')
