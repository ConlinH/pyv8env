from .flags import *
from .v8_audio_node import AudioNode


@construct_112001
class MediaStreamAudioSourceNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaStreamAudioSourceNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("mediaStream", "get_mediaStream", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_mediaStream(self):
        val = self._attr.get('mediaStream')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_audio_source_node.py -> MediaStreamAudioSourceNode.mediaStream -> get attr')
