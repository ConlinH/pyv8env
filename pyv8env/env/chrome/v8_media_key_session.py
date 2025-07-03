from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class MediaKeySession(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaKeySession, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("sessionId", "get_sessionId", None, 0, 1, 0, 0, 0, 0, 1),
        ("expiration", "get_expiration", None, 0, 1, 0, 0, 0, 0, 1),
        ("closed", "get_closed", None, 0, 1, 0, 1, 0, 0, 1),
        ("keyStatuses", "get_keyStatuses", None, 0, 1, 0, 0, 0, 0, 1),
        ("onkeystatuseschange", "get_onkeystatuseschange", "set_onkeystatuseschange", 0, 1, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("generateRequest", "fn_generateRequest", 2, 0, 1, 0, 1, 0, 0),
        ("load", "fn_load", 1, 0, 1, 0, 1, 0, 0),
        ("remove", "fn_remove", 0, 0, 1, 0, 1, 0, 0),
        ("update", "fn_update", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_sessionId(self):
        val = self._attr.get('sessionId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.sessionId -> get attr')

    def get_expiration(self):
        val = self._attr.get('expiration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.expiration -> get attr')

    def get_closed(self):
        val = self._attr.get('closed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.closed -> get attr')

    def get_keyStatuses(self):
        val = self._attr.get('keyStatuses')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.keyStatuses -> get attr')

    def get_onkeystatuseschange(self):
        val = self._attr.get('onkeystatuseschange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.onkeystatuseschange -> get attr')

    def set_onkeystatuseschange(self, val):
        self._attr['onkeystatuseschange'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.close{tuple(args)} -> method')

    def fn_generateRequest(self, *args):
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.generateRequest{tuple(args)} -> method')

    def fn_load(self, *args):
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.load{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.remove{tuple(args)} -> method')

    def fn_update(self, *args):
        logger.debug(f'patch -> v8_media_key_session.py -> MediaKeySession.update{tuple(args)} -> method')
