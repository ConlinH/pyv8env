from .flags import *


@construct_100001
class WebTransportDatagramDuplexStream:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("readable", "get_readable", None, 0, 1, 0, 0, 0, 0, 1),
        ("writable", "get_writable", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxDatagramSize", "get_maxDatagramSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("incomingMaxAge", "get_incomingMaxAge", "set_incomingMaxAge", 0, 1, 0, 0, 0, 0, 1),
        ("outgoingMaxAge", "get_outgoingMaxAge", "set_outgoingMaxAge", 0, 1, 0, 0, 0, 0, 1),
        ("incomingHighWaterMark", "get_incomingHighWaterMark", "set_incomingHighWaterMark", 0, 1, 0, 0, 0, 0, 1),
        ("outgoingHighWaterMark", "get_outgoingHighWaterMark", "set_outgoingHighWaterMark", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_readable(self):
        val = self._attr.get('readable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_datagram_duplex_stream.py -> WebTransportDatagramDuplexStream.readable -> get attr')

    def get_writable(self):
        val = self._attr.get('writable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_datagram_duplex_stream.py -> WebTransportDatagramDuplexStream.writable -> get attr')

    def get_maxDatagramSize(self):
        val = self._attr.get('maxDatagramSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_datagram_duplex_stream.py -> WebTransportDatagramDuplexStream.maxDatagramSize -> get attr')

    def get_incomingMaxAge(self):
        val = self._attr.get('incomingMaxAge')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_datagram_duplex_stream.py -> WebTransportDatagramDuplexStream.incomingMaxAge -> get attr')

    def set_incomingMaxAge(self, val):
        self._attr['incomingMaxAge'] = val

    def get_outgoingMaxAge(self):
        val = self._attr.get('outgoingMaxAge')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_datagram_duplex_stream.py -> WebTransportDatagramDuplexStream.outgoingMaxAge -> get attr')

    def set_outgoingMaxAge(self, val):
        self._attr['outgoingMaxAge'] = val

    def get_incomingHighWaterMark(self):
        val = self._attr.get('incomingHighWaterMark')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_datagram_duplex_stream.py -> WebTransportDatagramDuplexStream.incomingHighWaterMark -> get attr')

    def set_incomingHighWaterMark(self, val):
        self._attr['incomingHighWaterMark'] = val

    def get_outgoingHighWaterMark(self):
        val = self._attr.get('outgoingHighWaterMark')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_datagram_duplex_stream.py -> WebTransportDatagramDuplexStream.outgoingHighWaterMark -> get attr')

    def set_outgoingHighWaterMark(self, val):
        self._attr['outgoingHighWaterMark'] = val
