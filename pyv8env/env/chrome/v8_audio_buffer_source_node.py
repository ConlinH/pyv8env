from .flags import *
from .v8_audio_scheduled_source_node import AudioScheduledSourceNode


@construct_111001
class AudioBufferSourceNode(AudioScheduledSourceNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioBufferSourceNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("buffer", "get_buffer", "set_buffer", 0, 1, 0, 0, 0, 0, 1),
        ("playbackRate", "get_playbackRate", None, 0, 1, 0, 0, 0, 0, 1),
        ("detune", "get_detune", None, 0, 1, 0, 0, 0, 0, 1),
        ("loop", "get_loop", "set_loop", 0, 1, 0, 0, 0, 0, 1),
        ("loopStart", "get_loopStart", "set_loopStart", 0, 1, 0, 0, 0, 0, 1),
        ("loopEnd", "get_loopEnd", "set_loopEnd", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_buffer(self):
        val = self._attr.get('buffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer_source_node.py -> AudioBufferSourceNode.buffer -> get attr')

    def set_buffer(self, val):
        self._attr['buffer'] = val

    def get_playbackRate(self):
        val = self._attr.get('playbackRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer_source_node.py -> AudioBufferSourceNode.playbackRate -> get attr')

    def get_detune(self):
        val = self._attr.get('detune')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer_source_node.py -> AudioBufferSourceNode.detune -> get attr')

    def get_loop(self):
        val = self._attr.get('loop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer_source_node.py -> AudioBufferSourceNode.loop -> get attr')

    def set_loop(self, val):
        self._attr['loop'] = val

    def get_loopStart(self):
        val = self._attr.get('loopStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer_source_node.py -> AudioBufferSourceNode.loopStart -> get attr')

    def set_loopStart(self, val):
        self._attr['loopStart'] = val

    def get_loopEnd(self):
        val = self._attr.get('loopEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_buffer_source_node.py -> AudioBufferSourceNode.loopEnd -> get attr')

    def set_loopEnd(self, val):
        self._attr['loopEnd'] = val

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_audio_buffer_source_node.py -> AudioBufferSourceNode.start{tuple(args)} -> method')
