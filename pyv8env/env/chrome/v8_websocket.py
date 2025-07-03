from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class WebSocket(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WebSocket, self).__init__(*args, **kw)
    CONNECTING = 0
    OPEN = 1
    CLOSING = 2
    CLOSED = 3

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("bufferedAmount", "get_bufferedAmount", None, 0, 1, 0, 0, 0, 0, 1),
        ("onopen", "get_onopen", "set_onopen", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),
        ("extensions", "get_extensions", None, 0, 1, 0, 0, 0, 0, 1),
        ("protocol", "get_protocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),
        ("binaryType", "get_binaryType", "set_binaryType", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("send", "fn_send", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.url -> get attr')

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.readyState -> get attr')

    def get_bufferedAmount(self):
        val = self._attr.get('bufferedAmount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.bufferedAmount -> get attr')

    def get_onopen(self):
        val = self._attr.get('onopen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.onopen -> get attr')

    def set_onopen(self, val):
        self._attr['onopen'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_extensions(self):
        val = self._attr.get('extensions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.extensions -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.protocol -> get attr')

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_binaryType(self):
        val = self._attr.get('binaryType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.binaryType -> get attr')

    def set_binaryType(self, val):
        self._attr['binaryType'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.close{tuple(args)} -> method')

    def fn_send(self, *args):
        logger.debug(f'patch -> v8_websocket.py -> WebSocket.send{tuple(args)} -> method')
