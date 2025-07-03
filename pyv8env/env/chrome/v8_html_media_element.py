from .flags import *
from .v8_html_element import HTMLElement


@construct_100001
class HTMLMediaElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLMediaElement, self).__init__(*args, **kw)
    NETWORK_EMPTY = 0
    NETWORK_IDLE = 1
    NETWORK_LOADING = 2
    NETWORK_NO_SOURCE = 3
    HAVE_NOTHING = 0
    HAVE_METADATA = 1
    HAVE_CURRENT_DATA = 2
    HAVE_FUTURE_DATA = 3
    HAVE_ENOUGH_DATA = 4

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("error", "get_error", None, 0, 1, 0, 0, 0, 0, 1),
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("currentSrc", "get_currentSrc", None, 0, 1, 0, 0, 0, 0, 1),
        ("crossOrigin", "get_crossOrigin", "set_crossOrigin", 0, 1, 0, 0, 0, 0, 1),
        ("networkState", "get_networkState", None, 0, 1, 0, 0, 0, 0, 1),
        ("preload", "get_preload", "set_preload", 0, 1, 0, 0, 0, 0, 1),
        ("buffered", "get_buffered", None, 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("seeking", "get_seeking", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentTime", "get_currentTime", "set_currentTime", 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),
        ("paused", "get_paused", None, 0, 1, 0, 0, 0, 0, 1),
        ("defaultPlaybackRate", "get_defaultPlaybackRate", "set_defaultPlaybackRate", 0, 1, 0, 0, 0, 0, 1),
        ("playbackRate", "get_playbackRate", "set_playbackRate", 0, 1, 0, 0, 0, 0, 1),
        ("played", "get_played", None, 0, 1, 0, 0, 0, 0, 1),
        ("seekable", "get_seekable", None, 0, 1, 0, 0, 0, 0, 1),
        ("ended", "get_ended", None, 0, 1, 0, 0, 0, 0, 1),
        ("autoplay", "get_autoplay", "set_autoplay", 0, 1, 0, 0, 0, 0, 1),
        ("loop", "get_loop", "set_loop", 0, 1, 0, 0, 0, 0, 1),
        ("preservesPitch", "get_preservesPitch", "set_preservesPitch", 0, 1, 0, 0, 0, 0, 1),
        ("controls", "get_controls", "set_controls", 0, 1, 0, 0, 0, 0, 1),
        ("controlsList", "get_controlsList", "set_controlsList", 0, 1, 0, 0, 0, 0, 1),
        ("volume", "get_volume", "set_volume", 0, 1, 0, 0, 0, 0, 1),
        ("muted", "get_muted", "set_muted", 0, 1, 0, 0, 0, 0, 1),
        ("defaultMuted", "get_defaultMuted", "set_defaultMuted", 0, 1, 0, 0, 0, 0, 1),
        ("textTracks", "get_textTracks", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitAudioDecodedByteCount", "get_webkitAudioDecodedByteCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitVideoDecodedByteCount", "get_webkitVideoDecodedByteCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("onencrypted", "get_onencrypted", "set_onencrypted", 0, 1, 0, 0, 0, 0, 1),
        ("onwaitingforkey", "get_onwaitingforkey", "set_onwaitingforkey", 0, 1, 0, 0, 0, 0, 1),
        ("srcObject", "get_srcObject", "set_srcObject", 0, 1, 0, 0, 0, 0, 1),
        ("latencyHint", "get_latencyHint", "set_latencyHint", 0, 1, 0, 0, 0, 0, 1),
        ("audioTracks", "get_audioTracks", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoTracks", "get_videoTracks", None, 0, 1, 0, 0, 0, 0, 1),
        ("sinkId", "get_sinkId", None, 0, 1, 0, 0, 0, 0, 1),
        ("remote", "get_remote", None, 0, 1, 0, 0, 0, 0, 1),
        ("disableRemotePlayback", "get_disableRemotePlayback", "set_disableRemotePlayback", 0, 1, 0, 0, 0, 0, 1),
        ("mediaKeys", "get_mediaKeys", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addTextTrack", "fn_addTextTrack", 1, 0, 1, 0, 0, 0, 0),
        ("canPlayType", "fn_canPlayType", 1, 0, 1, 0, 0, 0, 0),
        ("captureStream", "fn_captureStream", 0, 0, 1, 0, 0, 0, 0),
        ("load", "fn_load", 0, 0, 1, 0, 0, 0, 0),
        ("pause", "fn_pause", 0, 0, 1, 0, 0, 0, 0),
        ("play", "fn_play", 0, 0, 1, 0, 1, 0, 0),
        ("setSinkId", "fn_setSinkId", 1, 0, 1, 0, 1, 0, 0),
        ("setMediaKeys", "fn_setMediaKeys", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_error(self):
        val = self._attr.get('error')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.error -> get attr')

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_currentSrc(self):
        val = self._attr.get('currentSrc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.currentSrc -> get attr')

    def get_crossOrigin(self):
        val = self._attr.get('crossOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.crossOrigin -> get attr')

    def set_crossOrigin(self, val):
        self._attr['crossOrigin'] = val

    def get_networkState(self):
        val = self._attr.get('networkState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.networkState -> get attr')

    def get_preload(self):
        val = self._attr.get('preload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.preload -> get attr')

    def set_preload(self, val):
        self._attr['preload'] = val

    def get_buffered(self):
        val = self._attr.get('buffered')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.buffered -> get attr')

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.readyState -> get attr')

    def get_seeking(self):
        val = self._attr.get('seeking')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.seeking -> get attr')

    def get_currentTime(self):
        val = self._attr.get('currentTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.currentTime -> get attr')

    def set_currentTime(self, val):
        self._attr['currentTime'] = val

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.duration -> get attr')

    def get_paused(self):
        val = self._attr.get('paused')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.paused -> get attr')

    def get_defaultPlaybackRate(self):
        val = self._attr.get('defaultPlaybackRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.defaultPlaybackRate -> get attr')

    def set_defaultPlaybackRate(self, val):
        self._attr['defaultPlaybackRate'] = val

    def get_playbackRate(self):
        val = self._attr.get('playbackRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.playbackRate -> get attr')

    def set_playbackRate(self, val):
        self._attr['playbackRate'] = val

    def get_played(self):
        val = self._attr.get('played')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.played -> get attr')

    def get_seekable(self):
        val = self._attr.get('seekable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.seekable -> get attr')

    def get_ended(self):
        val = self._attr.get('ended')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.ended -> get attr')

    def get_autoplay(self):
        val = self._attr.get('autoplay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.autoplay -> get attr')

    def set_autoplay(self, val):
        self._attr['autoplay'] = val

    def get_loop(self):
        val = self._attr.get('loop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.loop -> get attr')

    def set_loop(self, val):
        self._attr['loop'] = val

    def get_preservesPitch(self):
        val = self._attr.get('preservesPitch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.preservesPitch -> get attr')

    def set_preservesPitch(self, val):
        self._attr['preservesPitch'] = val

    def get_controls(self):
        val = self._attr.get('controls')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.controls -> get attr')

    def set_controls(self, val):
        self._attr['controls'] = val

    def get_controlsList(self):
        val = self._attr.get('controlsList')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.controlsList -> get attr')

    def set_controlsList(self, val):
        self._attr['controlsList'] = val

    def get_volume(self):
        val = self._attr.get('volume')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.volume -> get attr')

    def set_volume(self, val):
        self._attr['volume'] = val

    def get_muted(self):
        val = self._attr.get('muted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.muted -> get attr')

    def set_muted(self, val):
        self._attr['muted'] = val

    def get_defaultMuted(self):
        val = self._attr.get('defaultMuted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.defaultMuted -> get attr')

    def set_defaultMuted(self, val):
        self._attr['defaultMuted'] = val

    def get_textTracks(self):
        val = self._attr.get('textTracks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.textTracks -> get attr')

    def get_webkitAudioDecodedByteCount(self):
        val = self._attr.get('webkitAudioDecodedByteCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.webkitAudioDecodedByteCount -> get attr')

    def get_webkitVideoDecodedByteCount(self):
        val = self._attr.get('webkitVideoDecodedByteCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.webkitVideoDecodedByteCount -> get attr')

    def get_onencrypted(self):
        val = self._attr.get('onencrypted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.onencrypted -> get attr')

    def set_onencrypted(self, val):
        self._attr['onencrypted'] = val

    def get_onwaitingforkey(self):
        val = self._attr.get('onwaitingforkey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.onwaitingforkey -> get attr')

    def set_onwaitingforkey(self, val):
        self._attr['onwaitingforkey'] = val

    def get_srcObject(self):
        val = self._attr.get('srcObject')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.srcObject -> get attr')

    def set_srcObject(self, val):
        self._attr['srcObject'] = val

    def get_latencyHint(self):
        val = self._attr.get('latencyHint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.latencyHint -> get attr')

    def set_latencyHint(self, val):
        self._attr['latencyHint'] = val

    def get_audioTracks(self):
        val = self._attr.get('audioTracks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.audioTracks -> get attr')

    def get_videoTracks(self):
        val = self._attr.get('videoTracks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.videoTracks -> get attr')

    def get_sinkId(self):
        val = self._attr.get('sinkId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.sinkId -> get attr')

    def get_remote(self):
        val = self._attr.get('remote')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.remote -> get attr')

    def get_disableRemotePlayback(self):
        val = self._attr.get('disableRemotePlayback')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.disableRemotePlayback -> get attr')

    def set_disableRemotePlayback(self, val):
        self._attr['disableRemotePlayback'] = val

    def get_mediaKeys(self):
        val = self._attr.get('mediaKeys')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.mediaKeys -> get attr')

    def fn_addTextTrack(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.addTextTrack{tuple(args)} -> method')

    def fn_canPlayType(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.canPlayType{tuple(args)} -> method')

    def fn_captureStream(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.captureStream{tuple(args)} -> method')

    def fn_load(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.load{tuple(args)} -> method')

    def fn_pause(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.pause{tuple(args)} -> method')

    def fn_play(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.play{tuple(args)} -> method')

    def fn_setSinkId(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.setSinkId{tuple(args)} -> method')

    def fn_setMediaKeys(self, *args):
        logger.debug(f'patch -> v8_html_media_element.py -> HTMLMediaElement.setMediaKeys{tuple(args)} -> method')
