from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class RTCIceTransport(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCIceTransport, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("role", "get_role", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("gatheringState", "get_gatheringState", None, 0, 1, 0, 0, 0, 0, 1),
        ("onstatechange", "get_onstatechange", "set_onstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("ongatheringstatechange", "get_ongatheringstatechange", "set_ongatheringstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("onselectedcandidatepairchange", "get_onselectedcandidatepairchange", "set_onselectedcandidatepairchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getLocalCandidates", "fn_getLocalCandidates", 0, 0, 1, 0, 0, 0, 0),
        ("getLocalParameters", "fn_getLocalParameters", 0, 0, 1, 0, 0, 0, 0),
        ("getRemoteCandidates", "fn_getRemoteCandidates", 0, 0, 1, 0, 0, 0, 0),
        ("getRemoteParameters", "fn_getRemoteParameters", 0, 0, 1, 0, 0, 0, 0),
        ("getSelectedCandidatePair", "fn_getSelectedCandidatePair", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_role(self):
        val = self._attr.get('role')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.role -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.state -> get attr')

    def get_gatheringState(self):
        val = self._attr.get('gatheringState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.gatheringState -> get attr')

    def get_onstatechange(self):
        val = self._attr.get('onstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.onstatechange -> get attr')

    def set_onstatechange(self, val):
        self._attr['onstatechange'] = val

    def get_ongatheringstatechange(self):
        val = self._attr.get('ongatheringstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.ongatheringstatechange -> get attr')

    def set_ongatheringstatechange(self, val):
        self._attr['ongatheringstatechange'] = val

    def get_onselectedcandidatepairchange(self):
        val = self._attr.get('onselectedcandidatepairchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.onselectedcandidatepairchange -> get attr')

    def set_onselectedcandidatepairchange(self, val):
        self._attr['onselectedcandidatepairchange'] = val

    def fn_getLocalCandidates(self, *args):
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.getLocalCandidates{tuple(args)} -> method')

    def fn_getLocalParameters(self, *args):
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.getLocalParameters{tuple(args)} -> method')

    def fn_getRemoteCandidates(self, *args):
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.getRemoteCandidates{tuple(args)} -> method')

    def fn_getRemoteParameters(self, *args):
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.getRemoteParameters{tuple(args)} -> method')

    def fn_getSelectedCandidatePair(self, *args):
        logger.debug(f'patch -> v8_rtc_ice_transport.py -> RTCIceTransport.getSelectedCandidatePair{tuple(args)} -> method')
