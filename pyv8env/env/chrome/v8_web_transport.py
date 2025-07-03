from .flags import *


@construct_111001
class WebTransport:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("incomingUnidirectionalStreams", "get_incomingUnidirectionalStreams", None, 0, 1, 0, 0, 0, 0, 1),
        ("incomingBidirectionalStreams", "get_incomingBidirectionalStreams", None, 0, 1, 0, 0, 0, 0, 1),
        ("datagrams", "get_datagrams", None, 0, 1, 0, 0, 0, 0, 1),
        ("ready", "get_ready", None, 0, 1, 0, 1, 0, 0, 1),
        ("closed", "get_closed", None, 0, 1, 0, 1, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("createBidirectionalStream", "fn_createBidirectionalStream", 0, 0, 1, 0, 1, 0, 0),
        ("createUnidirectionalStream", "fn_createUnidirectionalStream", 0, 0, 1, 0, 1, 0, 0),
        ("getStats", "fn_getStats", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_incomingUnidirectionalStreams(self):
        val = self._attr.get('incomingUnidirectionalStreams')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.incomingUnidirectionalStreams -> get attr')

    def get_incomingBidirectionalStreams(self):
        val = self._attr.get('incomingBidirectionalStreams')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.incomingBidirectionalStreams -> get attr')

    def get_datagrams(self):
        val = self._attr.get('datagrams')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.datagrams -> get attr')

    def get_ready(self):
        val = self._attr.get('ready')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.ready -> get attr')

    def get_closed(self):
        val = self._attr.get('closed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.closed -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.close{tuple(args)} -> method')

    def fn_createBidirectionalStream(self, *args):
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.createBidirectionalStream{tuple(args)} -> method')

    def fn_createUnidirectionalStream(self, *args):
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.createUnidirectionalStream{tuple(args)} -> method')

    def fn_getStats(self, *args):
        logger.debug(f'patch -> v8_web_transport.py -> WebTransport.getStats{tuple(args)} -> method')
