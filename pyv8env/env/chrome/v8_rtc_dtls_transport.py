from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class RTCDtlsTransport(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCDtlsTransport, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("iceTransport", "get_iceTransport", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("onstatechange", "get_onstatechange", "set_onstatechange", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getRemoteCertificates", "fn_getRemoteCertificates", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_iceTransport(self):
        val = self._attr.get('iceTransport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_dtls_transport.py -> RTCDtlsTransport.iceTransport -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_dtls_transport.py -> RTCDtlsTransport.state -> get attr')

    def get_onstatechange(self):
        val = self._attr.get('onstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_dtls_transport.py -> RTCDtlsTransport.onstatechange -> get attr')

    def set_onstatechange(self, val):
        self._attr['onstatechange'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_dtls_transport.py -> RTCDtlsTransport.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def fn_getRemoteCertificates(self, *args):
        logger.debug(f'patch -> v8_rtc_dtls_transport.py -> RTCDtlsTransport.getRemoteCertificates{tuple(args)} -> method')
