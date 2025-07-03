from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class MediaStream(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaStream, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("active", "get_active", None, 0, 1, 0, 0, 0, 0, 1),
        ("onaddtrack", "get_onaddtrack", "set_onaddtrack", 0, 1, 0, 0, 0, 0, 1),
        ("onremovetrack", "get_onremovetrack", "set_onremovetrack", 0, 1, 0, 0, 0, 0, 1),
        ("onactive", "get_onactive", "set_onactive", 0, 1, 0, 0, 0, 0, 1),
        ("oninactive", "get_oninactive", "set_oninactive", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addTrack", "fn_addTrack", 1, 0, 1, 0, 0, 0, 0),
        ("clone", "fn_clone", 0, 0, 1, 0, 0, 0, 0),
        ("getAudioTracks", "fn_getAudioTracks", 0, 0, 1, 0, 0, 0, 0),
        ("getTrackById", "fn_getTrackById", 1, 0, 1, 0, 0, 0, 0),
        ("getTracks", "fn_getTracks", 0, 0, 1, 0, 0, 0, 0),
        ("getVideoTracks", "fn_getVideoTracks", 0, 0, 1, 0, 0, 0, 0),
        ("removeTrack", "fn_removeTrack", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.id -> get attr')

    def get_active(self):
        val = self._attr.get('active')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.active -> get attr')

    def get_onaddtrack(self):
        val = self._attr.get('onaddtrack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.onaddtrack -> get attr')

    def set_onaddtrack(self, val):
        self._attr['onaddtrack'] = val

    def get_onremovetrack(self):
        val = self._attr.get('onremovetrack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.onremovetrack -> get attr')

    def set_onremovetrack(self, val):
        self._attr['onremovetrack'] = val

    def get_onactive(self):
        val = self._attr.get('onactive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.onactive -> get attr')

    def set_onactive(self, val):
        self._attr['onactive'] = val

    def get_oninactive(self):
        val = self._attr.get('oninactive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.oninactive -> get attr')

    def set_oninactive(self, val):
        self._attr['oninactive'] = val

    def fn_addTrack(self, *args):
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.addTrack{tuple(args)} -> method')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.clone{tuple(args)} -> method')

    def fn_getAudioTracks(self, *args):
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.getAudioTracks{tuple(args)} -> method')

    def fn_getTrackById(self, *args):
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.getTrackById{tuple(args)} -> method')

    def fn_getTracks(self, *args):
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.getTracks{tuple(args)} -> method')

    def fn_getVideoTracks(self, *args):
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.getVideoTracks{tuple(args)} -> method')

    def fn_removeTrack(self, *args):
        logger.debug(f'patch -> v8_media_stream.py -> MediaStream.removeTrack{tuple(args)} -> method')
