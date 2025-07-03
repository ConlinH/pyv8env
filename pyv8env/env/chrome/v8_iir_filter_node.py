from .flags import *
from .v8_audio_node import AudioNode


@construct_112001
class IIRFilterNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IIRFilterNode, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getFrequencyResponse", "fn_getFrequencyResponse", 3, 0, 1, 0, 0, 0, 0),

    )

    def fn_getFrequencyResponse(self, *args):
        logger.debug(f'patch -> v8_iir_filter_node.py -> IIRFilterNode.getFrequencyResponse{tuple(args)} -> method')
