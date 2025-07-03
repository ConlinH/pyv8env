from .flags import *
from .v8_media_stream_track import MediaStreamTrack


@construct_100001
class BrowserCaptureMediaStreamTrack(MediaStreamTrack):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BrowserCaptureMediaStreamTrack, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cropTo", "fn_cropTo", 1, 0, 1, 0, 1, 0, 0),
        ("restrictTo", "fn_restrictTo", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_cropTo(self, *args):
        logger.debug(f'patch -> v8_browser_capture_media_stream_track.py -> BrowserCaptureMediaStreamTrack.cropTo{tuple(args)} -> method')

    def fn_restrictTo(self, *args):
        logger.debug(f'patch -> v8_browser_capture_media_stream_track.py -> BrowserCaptureMediaStreamTrack.restrictTo{tuple(args)} -> method')
