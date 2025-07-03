from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class VideoEncoder(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(VideoEncoder, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("encodeQueueSize", "get_encodeQueueSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("ondequeue", "get_ondequeue", "set_ondequeue", 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("configure", "fn_configure", 1, 0, 1, 0, 0, 0, 0),
        ("encode", "fn_encode", 1, 0, 1, 0, 0, 0, 0),
        ("flush", "fn_flush", 0, 0, 1, 0, 1, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 0, 0, 0),
        ("isConfigSupported", "fn_isConfigSupported", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_encodeQueueSize(self):
        val = self._attr.get('encodeQueueSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.encodeQueueSize -> get attr')

    def get_ondequeue(self):
        val = self._attr.get('ondequeue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.ondequeue -> get attr')

    def set_ondequeue(self, val):
        self._attr['ondequeue'] = val

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.state -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.close{tuple(args)} -> method')

    def fn_configure(self, *args):
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.configure{tuple(args)} -> method')

    def fn_encode(self, *args):
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.encode{tuple(args)} -> method')

    def fn_flush(self, *args):
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.flush{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.reset{tuple(args)} -> method')

    @classmethod
    def fn_isConfigSupported(cls, *args):
        logger.debug(f'patch -> v8_video_encoder.py -> VideoEncoder.isConfigSupported{tuple(args)} -> method')
