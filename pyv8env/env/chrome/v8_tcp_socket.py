from .flags import *


@construct_112001
class TCPSocket:
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
        logger.debug(f'patch -> v8_tcp_socket.py -> TCPSocket.opened -> get attr')

    def get_closed(self):
        val = self._attr.get('closed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_tcp_socket.py -> TCPSocket.closed -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_tcp_socket.py -> TCPSocket.close{tuple(args)} -> method')
