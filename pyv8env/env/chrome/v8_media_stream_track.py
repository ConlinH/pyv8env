from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class MediaStreamTrack(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaStreamTrack, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("kind", "get_kind", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", None, 0, 1, 0, 0, 0, 0, 1),
        ("enabled", "get_enabled", "set_enabled", 0, 1, 0, 0, 0, 0, 1),
        ("muted", "get_muted", None, 0, 1, 0, 0, 0, 0, 1),
        ("onmute", "get_onmute", "set_onmute", 0, 1, 0, 0, 0, 0, 1),
        ("onunmute", "get_onunmute", "set_onunmute", 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("onended", "get_onended", "set_onended", 0, 1, 0, 0, 0, 0, 1),
        ("stats", "get_stats", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentHint", "get_contentHint", "set_contentHint", 0, 1, 0, 0, 0, 0, 1),
        ("oncapturehandlechange", "get_oncapturehandlechange", "set_oncapturehandlechange", 0, 1, 0, 0, 0, 0, 1),
        ("onconfigurationchange", "get_onconfigurationchange", "set_onconfigurationchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("applyConstraints", "fn_applyConstraints", 0, 0, 1, 0, 1, 0, 0),
        ("clone", "fn_clone", 0, 0, 1, 0, 0, 0, 0),
        ("getCapabilities", "fn_getCapabilities", 0, 0, 1, 0, 0, 0, 0),
        ("getConstraints", "fn_getConstraints", 0, 0, 1, 0, 0, 0, 0),
        ("getSettings", "fn_getSettings", 0, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),
        ("getCaptureHandle", "fn_getCaptureHandle", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.kind -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.id -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.label -> get attr')

    def get_enabled(self):
        val = self._attr.get('enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.enabled -> get attr')

    def set_enabled(self, val):
        self._attr['enabled'] = val

    def get_muted(self):
        val = self._attr.get('muted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.muted -> get attr')

    def get_onmute(self):
        val = self._attr.get('onmute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.onmute -> get attr')

    def set_onmute(self, val):
        self._attr['onmute'] = val

    def get_onunmute(self):
        val = self._attr.get('onunmute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.onunmute -> get attr')

    def set_onunmute(self, val):
        self._attr['onunmute'] = val

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.readyState -> get attr')

    def get_onended(self):
        val = self._attr.get('onended')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.onended -> get attr')

    def set_onended(self, val):
        self._attr['onended'] = val

    def get_stats(self):
        val = self._attr.get('stats')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.stats -> get attr')

    def get_contentHint(self):
        val = self._attr.get('contentHint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.contentHint -> get attr')

    def set_contentHint(self, val):
        self._attr['contentHint'] = val

    def get_oncapturehandlechange(self):
        val = self._attr.get('oncapturehandlechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.oncapturehandlechange -> get attr')

    def set_oncapturehandlechange(self, val):
        self._attr['oncapturehandlechange'] = val

    def get_onconfigurationchange(self):
        val = self._attr.get('onconfigurationchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.onconfigurationchange -> get attr')

    def set_onconfigurationchange(self, val):
        self._attr['onconfigurationchange'] = val

    def fn_applyConstraints(self, *args):
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.applyConstraints{tuple(args)} -> method')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.clone{tuple(args)} -> method')

    def fn_getCapabilities(self, *args):
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.getCapabilities{tuple(args)} -> method')

    def fn_getConstraints(self, *args):
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.getConstraints{tuple(args)} -> method')

    def fn_getSettings(self, *args):
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.getSettings{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.stop{tuple(args)} -> method')

    def fn_getCaptureHandle(self, *args):
        logger.debug(f'patch -> v8_media_stream_track.py -> MediaStreamTrack.getCaptureHandle{tuple(args)} -> method')
