from .flags import *
from .v8_audio_node import AudioNode


@construct_100001
class AudioScheduledSourceNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioScheduledSourceNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onended", "get_onended", "set_onended", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_onended(self):
        val = self._attr.get('onended')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_scheduled_source_node.py -> AudioScheduledSourceNode.onended -> get attr')

    def set_onended(self, val):
        self._attr['onended'] = val

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_audio_scheduled_source_node.py -> AudioScheduledSourceNode.start{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_audio_scheduled_source_node.py -> AudioScheduledSourceNode.stop{tuple(args)} -> method')
