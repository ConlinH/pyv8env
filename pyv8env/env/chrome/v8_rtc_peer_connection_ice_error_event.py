from .flags import *
from .v8_event import Event


@construct_112001
class RTCPeerConnectionIceErrorEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCPeerConnectionIceErrorEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("address", "get_address", None, 0, 1, 0, 0, 0, 0, 1),
        ("port", "get_port", None, 0, 1, 0, 0, 0, 0, 1),
        ("hostCandidate", "get_hostCandidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("errorCode", "get_errorCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("errorText", "get_errorText", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_address(self):
        val = self._attr.get('address')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection_ice_error_event.py -> RTCPeerConnectionIceErrorEvent.address -> get attr')

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection_ice_error_event.py -> RTCPeerConnectionIceErrorEvent.port -> get attr')

    def get_hostCandidate(self):
        val = self._attr.get('hostCandidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection_ice_error_event.py -> RTCPeerConnectionIceErrorEvent.hostCandidate -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection_ice_error_event.py -> RTCPeerConnectionIceErrorEvent.url -> get attr')

    def get_errorCode(self):
        val = self._attr.get('errorCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection_ice_error_event.py -> RTCPeerConnectionIceErrorEvent.errorCode -> get attr')

    def get_errorText(self):
        val = self._attr.get('errorText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection_ice_error_event.py -> RTCPeerConnectionIceErrorEvent.errorText -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection_ice_error_event.py -> RTCPeerConnectionIceErrorEvent.isTrusted -> get attr')
