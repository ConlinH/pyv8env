from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class EventSource(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(EventSource, self).__init__(*args, **kw)
    CONNECTING = 0
    OPEN = 1
    CLOSED = 2

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("withCredentials", "get_withCredentials", None, 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("onopen", "get_onopen", "set_onopen", 0, 1, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event_source.py -> EventSource.url -> get attr')

    def get_withCredentials(self):
        val = self._attr.get('withCredentials')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event_source.py -> EventSource.withCredentials -> get attr')

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event_source.py -> EventSource.readyState -> get attr')

    def get_onopen(self):
        val = self._attr.get('onopen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event_source.py -> EventSource.onopen -> get attr')

    def set_onopen(self, val):
        self._attr['onopen'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event_source.py -> EventSource.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event_source.py -> EventSource.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_event_source.py -> EventSource.close{tuple(args)} -> method')
