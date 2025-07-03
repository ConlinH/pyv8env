from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class RTCPeerConnection(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCPeerConnection, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("localDescription", "get_localDescription", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentLocalDescription", "get_currentLocalDescription", None, 0, 1, 0, 0, 0, 0, 1),
        ("pendingLocalDescription", "get_pendingLocalDescription", None, 0, 1, 0, 0, 0, 0, 1),
        ("remoteDescription", "get_remoteDescription", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentRemoteDescription", "get_currentRemoteDescription", None, 0, 1, 0, 0, 0, 0, 1),
        ("pendingRemoteDescription", "get_pendingRemoteDescription", None, 0, 1, 0, 0, 0, 0, 1),
        ("signalingState", "get_signalingState", None, 0, 1, 0, 0, 0, 0, 1),
        ("iceGatheringState", "get_iceGatheringState", None, 0, 1, 0, 0, 0, 0, 1),
        ("iceConnectionState", "get_iceConnectionState", None, 0, 1, 0, 0, 0, 0, 1),
        ("connectionState", "get_connectionState", None, 0, 1, 0, 0, 0, 0, 1),
        ("canTrickleIceCandidates", "get_canTrickleIceCandidates", None, 0, 1, 0, 0, 0, 0, 1),
        ("onnegotiationneeded", "get_onnegotiationneeded", "set_onnegotiationneeded", 0, 1, 0, 0, 0, 0, 1),
        ("onicecandidate", "get_onicecandidate", "set_onicecandidate", 0, 1, 0, 0, 0, 0, 1),
        ("onsignalingstatechange", "get_onsignalingstatechange", "set_onsignalingstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("oniceconnectionstatechange", "get_oniceconnectionstatechange", "set_oniceconnectionstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("onconnectionstatechange", "get_onconnectionstatechange", "set_onconnectionstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("onicegatheringstatechange", "get_onicegatheringstatechange", "set_onicegatheringstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("onicecandidateerror", "get_onicecandidateerror", "set_onicecandidateerror", 0, 1, 0, 0, 0, 0, 1),
        ("ontrack", "get_ontrack", "set_ontrack", 0, 1, 0, 0, 0, 0, 1),
        ("sctp", "get_sctp", None, 0, 1, 0, 0, 0, 0, 1),
        ("ondatachannel", "get_ondatachannel", "set_ondatachannel", 0, 1, 0, 0, 0, 0, 1),
        ("onaddstream", "get_onaddstream", "set_onaddstream", 0, 1, 0, 0, 0, 0, 1),
        ("onremovestream", "get_onremovestream", "set_onremovestream", 0, 1, 0, 0, 0, 0, 1),
        ("rtpTransport", "get_rtpTransport", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addIceCandidate", "fn_addIceCandidate", 0, 0, 1, 0, 1, 0, 0),
        ("addStream", "fn_addStream", 1, 0, 1, 0, 0, 0, 0),
        ("addTrack", "fn_addTrack", 1, 0, 1, 0, 0, 0, 0),
        ("addTransceiver", "fn_addTransceiver", 1, 0, 1, 0, 0, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("createAnswer", "fn_createAnswer", 0, 0, 1, 0, 1, 0, 0),
        ("createDTMFSender", "fn_createDTMFSender", 1, 0, 1, 0, 0, 0, 0),
        ("createDataChannel", "fn_createDataChannel", 1, 0, 1, 0, 0, 0, 0),
        ("createOffer", "fn_createOffer", 0, 0, 1, 0, 1, 0, 0),
        ("getConfiguration", "fn_getConfiguration", 0, 0, 1, 0, 0, 0, 0),
        ("getLocalStreams", "fn_getLocalStreams", 0, 0, 1, 0, 0, 0, 0),
        ("getReceivers", "fn_getReceivers", 0, 0, 1, 0, 0, 0, 0),
        ("getRemoteStreams", "fn_getRemoteStreams", 0, 0, 1, 0, 0, 0, 0),
        ("getSenders", "fn_getSenders", 0, 0, 1, 0, 0, 0, 0),
        ("getStats", "fn_getStats", 0, 0, 1, 0, 1, 0, 0),
        ("getTransceivers", "fn_getTransceivers", 0, 0, 1, 0, 0, 0, 0),
        ("removeStream", "fn_removeStream", 1, 0, 1, 0, 0, 0, 0),
        ("removeTrack", "fn_removeTrack", 1, 0, 1, 0, 0, 0, 0),
        ("restartIce", "fn_restartIce", 0, 0, 1, 0, 0, 0, 0),
        ("setConfiguration", "fn_setConfiguration", 0, 0, 1, 0, 0, 0, 0),
        ("setLocalDescription", "fn_setLocalDescription", 0, 0, 1, 0, 1, 0, 0),
        ("setRemoteDescription", "fn_setRemoteDescription", 1, 0, 1, 0, 1, 0, 0),
        ("generateCertificate", "fn_generateCertificate", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_localDescription(self):
        val = self._attr.get('localDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.localDescription -> get attr')

    def get_currentLocalDescription(self):
        val = self._attr.get('currentLocalDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.currentLocalDescription -> get attr')

    def get_pendingLocalDescription(self):
        val = self._attr.get('pendingLocalDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.pendingLocalDescription -> get attr')

    def get_remoteDescription(self):
        val = self._attr.get('remoteDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.remoteDescription -> get attr')

    def get_currentRemoteDescription(self):
        val = self._attr.get('currentRemoteDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.currentRemoteDescription -> get attr')

    def get_pendingRemoteDescription(self):
        val = self._attr.get('pendingRemoteDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.pendingRemoteDescription -> get attr')

    def get_signalingState(self):
        val = self._attr.get('signalingState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.signalingState -> get attr')

    def get_iceGatheringState(self):
        val = self._attr.get('iceGatheringState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.iceGatheringState -> get attr')

    def get_iceConnectionState(self):
        val = self._attr.get('iceConnectionState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.iceConnectionState -> get attr')

    def get_connectionState(self):
        val = self._attr.get('connectionState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.connectionState -> get attr')

    def get_canTrickleIceCandidates(self):
        val = self._attr.get('canTrickleIceCandidates')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.canTrickleIceCandidates -> get attr')

    def get_onnegotiationneeded(self):
        val = self._attr.get('onnegotiationneeded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onnegotiationneeded -> get attr')

    def set_onnegotiationneeded(self, val):
        self._attr['onnegotiationneeded'] = val

    def get_onicecandidate(self):
        val = self._attr.get('onicecandidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onicecandidate -> get attr')

    def set_onicecandidate(self, val):
        self._attr['onicecandidate'] = val

    def get_onsignalingstatechange(self):
        val = self._attr.get('onsignalingstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onsignalingstatechange -> get attr')

    def set_onsignalingstatechange(self, val):
        self._attr['onsignalingstatechange'] = val

    def get_oniceconnectionstatechange(self):
        val = self._attr.get('oniceconnectionstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.oniceconnectionstatechange -> get attr')

    def set_oniceconnectionstatechange(self, val):
        self._attr['oniceconnectionstatechange'] = val

    def get_onconnectionstatechange(self):
        val = self._attr.get('onconnectionstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onconnectionstatechange -> get attr')

    def set_onconnectionstatechange(self, val):
        self._attr['onconnectionstatechange'] = val

    def get_onicegatheringstatechange(self):
        val = self._attr.get('onicegatheringstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onicegatheringstatechange -> get attr')

    def set_onicegatheringstatechange(self, val):
        self._attr['onicegatheringstatechange'] = val

    def get_onicecandidateerror(self):
        val = self._attr.get('onicecandidateerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onicecandidateerror -> get attr')

    def set_onicecandidateerror(self, val):
        self._attr['onicecandidateerror'] = val

    def get_ontrack(self):
        val = self._attr.get('ontrack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.ontrack -> get attr')

    def set_ontrack(self, val):
        self._attr['ontrack'] = val

    def get_sctp(self):
        val = self._attr.get('sctp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.sctp -> get attr')

    def get_ondatachannel(self):
        val = self._attr.get('ondatachannel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.ondatachannel -> get attr')

    def set_ondatachannel(self, val):
        self._attr['ondatachannel'] = val

    def get_onaddstream(self):
        val = self._attr.get('onaddstream')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onaddstream -> get attr')

    def set_onaddstream(self, val):
        self._attr['onaddstream'] = val

    def get_onremovestream(self):
        val = self._attr.get('onremovestream')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.onremovestream -> get attr')

    def set_onremovestream(self, val):
        self._attr['onremovestream'] = val

    def get_rtpTransport(self):
        val = self._attr.get('rtpTransport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.rtpTransport -> get attr')

    def fn_addIceCandidate(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.addIceCandidate{tuple(args)} -> method')

    def fn_addStream(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.addStream{tuple(args)} -> method')

    def fn_addTrack(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.addTrack{tuple(args)} -> method')

    def fn_addTransceiver(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.addTransceiver{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.close{tuple(args)} -> method')

    def fn_createAnswer(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.createAnswer{tuple(args)} -> method')

    def fn_createDTMFSender(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.createDTMFSender{tuple(args)} -> method')

    def fn_createDataChannel(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.createDataChannel{tuple(args)} -> method')

    def fn_createOffer(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.createOffer{tuple(args)} -> method')

    def fn_getConfiguration(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.getConfiguration{tuple(args)} -> method')

    def fn_getLocalStreams(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.getLocalStreams{tuple(args)} -> method')

    def fn_getReceivers(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.getReceivers{tuple(args)} -> method')

    def fn_getRemoteStreams(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.getRemoteStreams{tuple(args)} -> method')

    def fn_getSenders(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.getSenders{tuple(args)} -> method')

    def fn_getStats(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.getStats{tuple(args)} -> method')

    def fn_getTransceivers(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.getTransceivers{tuple(args)} -> method')

    def fn_removeStream(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.removeStream{tuple(args)} -> method')

    def fn_removeTrack(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.removeTrack{tuple(args)} -> method')

    def fn_restartIce(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.restartIce{tuple(args)} -> method')

    def fn_setConfiguration(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.setConfiguration{tuple(args)} -> method')

    def fn_setLocalDescription(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.setLocalDescription{tuple(args)} -> method')

    def fn_setRemoteDescription(self, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.setRemoteDescription{tuple(args)} -> method')

    @classmethod
    def fn_generateCertificate(cls, *args):
        logger.debug(f'patch -> v8_rtc_peer_connection.py -> RTCPeerConnection.generateCertificate{tuple(args)} -> method')
