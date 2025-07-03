from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class VideoDecoder(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(VideoDecoder, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("decodeQueueSize", "get_decodeQueueSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("ondequeue", "get_ondequeue", "set_ondequeue", 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("configure", "fn_configure", 1, 0, 1, 0, 0, 0, 0),
        ("decode", "fn_decode", 1, 0, 1, 0, 0, 0, 0),
        ("flush", "fn_flush", 0, 0, 1, 0, 1, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 0, 0, 0),
        ("isConfigSupported", "fn_isConfigSupported", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_decodeQueueSize(self):
        val = self._attr.get('decodeQueueSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.decodeQueueSize -> get attr')

    def get_ondequeue(self):
        val = self._attr.get('ondequeue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.ondequeue -> get attr')

    def set_ondequeue(self, val):
        self._attr['ondequeue'] = val

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.state -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.close{tuple(args)} -> method')

    def fn_configure(self, *args):
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.configure{tuple(args)} -> method')

    def fn_decode(self, *args):
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.decode{tuple(args)} -> method')

    def fn_flush(self, *args):
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.flush{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.reset{tuple(args)} -> method')

    @classmethod
    def fn_isConfigSupported(cls, *args):
        logger.debug(f'patch -> v8_video_decoder.py -> VideoDecoder.isConfigSupported{tuple(args)} -> method')
