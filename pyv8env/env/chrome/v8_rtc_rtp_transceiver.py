from .flags import *


@construct_100001
class RTCRtpTransceiver:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("mid", "get_mid", None, 0, 1, 0, 0, 0, 0, 1),
        ("sender", "get_sender", None, 0, 1, 0, 0, 0, 0, 1),
        ("receiver", "get_receiver", None, 0, 1, 0, 0, 0, 0, 1),
        ("stopped", "get_stopped", None, 0, 1, 0, 0, 0, 0, 1),
        ("direction", "get_direction", "set_direction", 0, 1, 0, 0, 0, 0, 1),
        ("currentDirection", "get_currentDirection", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setCodecPreferences", "fn_setCodecPreferences", 1, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),
        ("getHeaderExtensionsToNegotiate", "fn_getHeaderExtensionsToNegotiate", 0, 0, 1, 0, 0, 0, 0),
        ("getNegotiatedHeaderExtensions", "fn_getNegotiatedHeaderExtensions", 0, 0, 1, 0, 0, 0, 0),
        ("setHeaderExtensionsToNegotiate", "fn_setHeaderExtensionsToNegotiate", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_mid(self):
        val = self._attr.get('mid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.mid -> get attr')

    def get_sender(self):
        val = self._attr.get('sender')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.sender -> get attr')

    def get_receiver(self):
        val = self._attr.get('receiver')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.receiver -> get attr')

    def get_stopped(self):
        val = self._attr.get('stopped')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.stopped -> get attr')

    def get_direction(self):
        val = self._attr.get('direction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.direction -> get attr')

    def set_direction(self, val):
        self._attr['direction'] = val

    def get_currentDirection(self):
        val = self._attr.get('currentDirection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.currentDirection -> get attr')

    def fn_setCodecPreferences(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.setCodecPreferences{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.stop{tuple(args)} -> method')

    def fn_getHeaderExtensionsToNegotiate(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.getHeaderExtensionsToNegotiate{tuple(args)} -> method')

    def fn_getNegotiatedHeaderExtensions(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.getNegotiatedHeaderExtensions{tuple(args)} -> method')

    def fn_setHeaderExtensionsToNegotiate(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_transceiver.py -> RTCRtpTransceiver.setHeaderExtensionsToNegotiate{tuple(args)} -> method')
