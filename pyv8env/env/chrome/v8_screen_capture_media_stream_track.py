from .flags import *
from .v8_media_stream_track import MediaStreamTrack


@construct_100001
class ScreenCaptureMediaStreamTrack(MediaStreamTrack):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ScreenCaptureMediaStreamTrack, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("screenDetailed", "fn_screenDetailed", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_screenDetailed(self, *args):
        logger.debug(f'patch -> v8_screen_capture_media_stream_track.py -> ScreenCaptureMediaStreamTrack.screenDetailed{tuple(args)} -> method')
