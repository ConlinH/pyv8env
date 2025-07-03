from .flags import *
from .v8_media_stream_track import MediaStreamTrack


@construct_100001
class CanvasCaptureMediaStreamTrack(MediaStreamTrack):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CanvasCaptureMediaStreamTrack, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("canvas", "get_canvas", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("requestFrame", "fn_requestFrame", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_canvas(self):
        val = self._attr.get('canvas')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_canvas_capture_media_stream_track.py -> CanvasCaptureMediaStreamTrack.canvas -> get attr')

    def fn_requestFrame(self, *args):
        logger.debug(f'patch -> v8_canvas_capture_media_stream_track.py -> CanvasCaptureMediaStreamTrack.requestFrame{tuple(args)} -> method')
