from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class AudioNode(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("context", "get_context", None, 0, 1, 0, 0, 0, 0, 1),
        ("numberOfInputs", "get_numberOfInputs", None, 0, 1, 0, 0, 0, 0, 1),
        ("numberOfOutputs", "get_numberOfOutputs", None, 0, 1, 0, 0, 0, 0, 1),
        ("channelCount", "get_channelCount", "set_channelCount", 0, 1, 0, 0, 0, 0, 1),
        ("channelCountMode", "get_channelCountMode", "set_channelCountMode", 0, 1, 0, 0, 0, 0, 1),
        ("channelInterpretation", "get_channelInterpretation", "set_channelInterpretation", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("connect", "fn_connect", 1, 0, 1, 0, 0, 0, 0),
        ("disconnect", "fn_disconnect", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_context(self):
        val = self._attr.get('context')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.context -> get attr')

    def get_numberOfInputs(self):
        val = self._attr.get('numberOfInputs')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.numberOfInputs -> get attr')

    def get_numberOfOutputs(self):
        val = self._attr.get('numberOfOutputs')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.numberOfOutputs -> get attr')

    def get_channelCount(self):
        val = self._attr.get('channelCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.channelCount -> get attr')

    def set_channelCount(self, val):
        self._attr['channelCount'] = val

    def get_channelCountMode(self):
        val = self._attr.get('channelCountMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.channelCountMode -> get attr')

    def set_channelCountMode(self, val):
        self._attr['channelCountMode'] = val

    def get_channelInterpretation(self):
        val = self._attr.get('channelInterpretation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.channelInterpretation -> get attr')

    def set_channelInterpretation(self, val):
        self._attr['channelInterpretation'] = val

    def fn_connect(self, *args):
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.connect{tuple(args)} -> method')

    def fn_disconnect(self, *args):
        logger.debug(f'patch -> v8_audio_node.py -> AudioNode.disconnect{tuple(args)} -> method')
