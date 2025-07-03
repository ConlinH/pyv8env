from .flags import *
from .v8_audio_node import AudioNode


@construct_112001
class MediaElementAudioSourceNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaElementAudioSourceNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("mediaElement", "get_mediaElement", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_mediaElement(self):
        val = self._attr.get('mediaElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_element_audio_source_node.py -> MediaElementAudioSourceNode.mediaElement -> get attr')
