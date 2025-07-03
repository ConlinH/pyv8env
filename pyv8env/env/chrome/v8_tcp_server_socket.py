from .flags import *


@construct_111001
class TCPServerSocket:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("opened", "get_opened", None, 0, 1, 0, 1, 0, 0, 1),
        ("closed", "get_closed", None, 0, 1, 0, 1, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_opened(self):
        val = self._attr.get('opened')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_tcp_server_socket.py -> TCPServerSocket.opened -> get attr')

    def get_closed(self):
        val = self._attr.get('closed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_tcp_server_socket.py -> TCPServerSocket.closed -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_tcp_server_socket.py -> TCPServerSocket.close{tuple(args)} -> method')
