from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class ChannelSplitterNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ChannelSplitterNode, self).__init__(*args, **kw)
