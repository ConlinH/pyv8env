from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_rtc_peer_connection_ice_event import RTCPeerConnectionIceEvent as V8RTCPeerConnectionIceEvent


@impl_warp
class RTCPeerConnectionIceEvent(V8RTCPeerConnectionIceEvent):
    def __init__(self, *args, **kw):
        kw.setdefault('isTrusted', True)
        super(RTCPeerConnectionIceEvent, self).__init__(*args, **kw)
