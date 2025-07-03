from .flags import *


@construct_110001
class RTCIceCandidate:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("candidate", "get_candidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("sdpMid", "get_sdpMid", None, 0, 1, 0, 0, 0, 0, 1),
        ("sdpMLineIndex", "get_sdpMLineIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("foundation", "get_foundation", None, 0, 1, 0, 0, 0, 0, 1),
        ("component", "get_component", None, 0, 1, 0, 0, 0, 0, 1),
        ("priority", "get_priority", None, 0, 1, 0, 0, 0, 0, 1),
        ("address", "get_address", None, 0, 1, 0, 0, 0, 0, 1),
        ("protocol", "get_protocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("port", "get_port", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("tcpType", "get_tcpType", None, 0, 1, 0, 0, 0, 0, 1),
        ("relatedAddress", "get_relatedAddress", None, 0, 1, 0, 0, 0, 0, 1),
        ("relatedPort", "get_relatedPort", None, 0, 1, 0, 0, 0, 0, 1),
        ("usernameFragment", "get_usernameFragment", None, 0, 1, 0, 0, 0, 0, 1),
        ("relayProtocol", "get_relayProtocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_candidate(self):
        val = self._attr.get('candidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.candidate -> get attr')

    def get_sdpMid(self):
        val = self._attr.get('sdpMid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.sdpMid -> get attr')

    def get_sdpMLineIndex(self):
        val = self._attr.get('sdpMLineIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.sdpMLineIndex -> get attr')

    def get_foundation(self):
        val = self._attr.get('foundation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.foundation -> get attr')

    def get_component(self):
        val = self._attr.get('component')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.component -> get attr')

    def get_priority(self):
        val = self._attr.get('priority')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.priority -> get attr')

    def get_address(self):
        val = self._attr.get('address')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.address -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.protocol -> get attr')

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.port -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.type -> get attr')

    def get_tcpType(self):
        val = self._attr.get('tcpType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.tcpType -> get attr')

    def get_relatedAddress(self):
        val = self._attr.get('relatedAddress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.relatedAddress -> get attr')

    def get_relatedPort(self):
        val = self._attr.get('relatedPort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.relatedPort -> get attr')

    def get_usernameFragment(self):
        val = self._attr.get('usernameFragment')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.usernameFragment -> get attr')

    def get_relayProtocol(self):
        val = self._attr.get('relayProtocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.relayProtocol -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.url -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_rtc_ice_candidate.py -> RTCIceCandidate.toJSON{tuple(args)} -> method')
