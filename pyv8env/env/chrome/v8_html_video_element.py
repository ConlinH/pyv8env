from .flags import *
from .v8_html_media_element import HTMLMediaElement


@construct_110001
class HTMLVideoElement(HTMLMediaElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLVideoElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("videoWidth", "get_videoWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoHeight", "get_videoHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("poster", "get_poster", "set_poster", 0, 1, 0, 0, 0, 0, 1),
        ("webkitDecodedFrameCount", "get_webkitDecodedFrameCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitDroppedFrameCount", "get_webkitDroppedFrameCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("playsInline", "get_playsInline", "set_playsInline", 0, 1, 0, 0, 0, 0, 1),
        ("onenterpictureinpicture", "get_onenterpictureinpicture", "set_onenterpictureinpicture", 0, 1, 0, 0, 0, 0, 1),
        ("onleavepictureinpicture", "get_onleavepictureinpicture", "set_onleavepictureinpicture", 0, 1, 0, 0, 0, 0, 1),
        ("disablePictureInPicture", "get_disablePictureInPicture", "set_disablePictureInPicture", 0, 1, 0, 0, 0, 0, 1),
        ("webkitSupportsFullscreen", "get_webkitSupportsFullscreen", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitDisplayingFullscreen", "get_webkitDisplayingFullscreen", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancelVideoFrameCallback", "fn_cancelVideoFrameCallback", 1, 0, 1, 0, 0, 0, 0),
        ("getVideoPlaybackQuality", "fn_getVideoPlaybackQuality", 0, 0, 1, 0, 0, 0, 0),
        ("requestPictureInPicture", "fn_requestPictureInPicture", 0, 0, 1, 0, 1, 0, 0),
        ("requestVideoFrameCallback", "fn_requestVideoFrameCallback", 1, 0, 1, 0, 0, 0, 0),
        ("webkitEnterFullScreen", "fn_webkitEnterFullScreen", 0, 0, 1, 0, 0, 0, 0),
        ("webkitEnterFullscreen", "fn_webkitEnterFullscreen", 0, 0, 1, 0, 0, 0, 0),
        ("webkitExitFullScreen", "fn_webkitExitFullScreen", 0, 0, 1, 0, 0, 0, 0),
        ("webkitExitFullscreen", "fn_webkitExitFullscreen", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_videoWidth(self):
        val = self._attr.get('videoWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.videoWidth -> get attr')

    def get_videoHeight(self):
        val = self._attr.get('videoHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.videoHeight -> get attr')

    def get_poster(self):
        val = self._attr.get('poster')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.poster -> get attr')

    def set_poster(self, val):
        self._attr['poster'] = val

    def get_webkitDecodedFrameCount(self):
        val = self._attr.get('webkitDecodedFrameCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitDecodedFrameCount -> get attr')

    def get_webkitDroppedFrameCount(self):
        val = self._attr.get('webkitDroppedFrameCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitDroppedFrameCount -> get attr')

    def get_playsInline(self):
        val = self._attr.get('playsInline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.playsInline -> get attr')

    def set_playsInline(self, val):
        self._attr['playsInline'] = val

    def get_onenterpictureinpicture(self):
        val = self._attr.get('onenterpictureinpicture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.onenterpictureinpicture -> get attr')

    def set_onenterpictureinpicture(self, val):
        self._attr['onenterpictureinpicture'] = val

    def get_onleavepictureinpicture(self):
        val = self._attr.get('onleavepictureinpicture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.onleavepictureinpicture -> get attr')

    def set_onleavepictureinpicture(self, val):
        self._attr['onleavepictureinpicture'] = val

    def get_disablePictureInPicture(self):
        val = self._attr.get('disablePictureInPicture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.disablePictureInPicture -> get attr')

    def set_disablePictureInPicture(self, val):
        self._attr['disablePictureInPicture'] = val

    def get_webkitSupportsFullscreen(self):
        val = self._attr.get('webkitSupportsFullscreen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitSupportsFullscreen -> get attr')

    def get_webkitDisplayingFullscreen(self):
        val = self._attr.get('webkitDisplayingFullscreen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitDisplayingFullscreen -> get attr')

    def fn_cancelVideoFrameCallback(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.cancelVideoFrameCallback{tuple(args)} -> method')

    def fn_getVideoPlaybackQuality(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.getVideoPlaybackQuality{tuple(args)} -> method')

    def fn_requestPictureInPicture(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.requestPictureInPicture{tuple(args)} -> method')

    def fn_requestVideoFrameCallback(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.requestVideoFrameCallback{tuple(args)} -> method')

    def fn_webkitEnterFullScreen(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitEnterFullScreen{tuple(args)} -> method')

    def fn_webkitEnterFullscreen(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitEnterFullscreen{tuple(args)} -> method')

    def fn_webkitExitFullScreen(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitExitFullScreen{tuple(args)} -> method')

    def fn_webkitExitFullscreen(self, *args):
        logger.debug(f'patch -> v8_html_video_element.py -> HTMLVideoElement.webkitExitFullscreen{tuple(args)} -> method')
