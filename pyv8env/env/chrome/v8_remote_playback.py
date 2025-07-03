from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class RemotePlayback(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RemotePlayback, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("onconnecting", "get_onconnecting", "set_onconnecting", 0, 1, 0, 0, 0, 0, 1),
        ("onconnect", "get_onconnect", "set_onconnect", 0, 1, 0, 0, 0, 0, 1),
        ("ondisconnect", "get_ondisconnect", "set_ondisconnect", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancelWatchAvailability", "fn_cancelWatchAvailability", 0, 0, 1, 0, 1, 0, 0),
        ("prompt", "fn_prompt", 0, 0, 1, 0, 1, 0, 0),
        ("watchAvailability", "fn_watchAvailability", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_remote_playback.py -> RemotePlayback.state -> get attr')

    def get_onconnecting(self):
        val = self._attr.get('onconnecting')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_remote_playback.py -> RemotePlayback.onconnecting -> get attr')

    def set_onconnecting(self, val):
        self._attr['onconnecting'] = val

    def get_onconnect(self):
        val = self._attr.get('onconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_remote_playback.py -> RemotePlayback.onconnect -> get attr')

    def set_onconnect(self, val):
        self._attr['onconnect'] = val

    def get_ondisconnect(self):
        val = self._attr.get('ondisconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_remote_playback.py -> RemotePlayback.ondisconnect -> get attr')

    def set_ondisconnect(self, val):
        self._attr['ondisconnect'] = val

    def fn_cancelWatchAvailability(self, *args):
        logger.debug(f'patch -> v8_remote_playback.py -> RemotePlayback.cancelWatchAvailability{tuple(args)} -> method')

    def fn_prompt(self, *args):
        logger.debug(f'patch -> v8_remote_playback.py -> RemotePlayback.prompt{tuple(args)} -> method')

    def fn_watchAvailability(self, *args):
        logger.debug(f'patch -> v8_remote_playback.py -> RemotePlayback.watchAvailability{tuple(args)} -> method')
