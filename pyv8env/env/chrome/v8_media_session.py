from .flags import *


@construct_100001
class MediaSession:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("metadata", "get_metadata", "set_metadata", 0, 1, 0, 0, 0, 0, 1),
        ("playbackState", "get_playbackState", "set_playbackState", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setActionHandler", "fn_setActionHandler", 2, 0, 1, 0, 0, 0, 0),
        ("setCameraActive", "fn_setCameraActive", 1, 0, 1, 0, 0, 0, 0),
        ("setMicrophoneActive", "fn_setMicrophoneActive", 1, 0, 1, 0, 0, 0, 0),
        ("setPositionState", "fn_setPositionState", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_metadata(self):
        val = self._attr.get('metadata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_session.py -> MediaSession.metadata -> get attr')

    def set_metadata(self, val):
        self._attr['metadata'] = val

    def get_playbackState(self):
        val = self._attr.get('playbackState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_session.py -> MediaSession.playbackState -> get attr')

    def set_playbackState(self, val):
        self._attr['playbackState'] = val

    def fn_setActionHandler(self, *args):
        logger.debug(f'patch -> v8_media_session.py -> MediaSession.setActionHandler{tuple(args)} -> method')

    def fn_setCameraActive(self, *args):
        logger.debug(f'patch -> v8_media_session.py -> MediaSession.setCameraActive{tuple(args)} -> method')

    def fn_setMicrophoneActive(self, *args):
        logger.debug(f'patch -> v8_media_session.py -> MediaSession.setMicrophoneActive{tuple(args)} -> method')

    def fn_setPositionState(self, *args):
        logger.debug(f'patch -> v8_media_session.py -> MediaSession.setPositionState{tuple(args)} -> method')
