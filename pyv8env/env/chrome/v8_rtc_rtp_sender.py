from .flags import *


@construct_100001
class RTCRtpSender:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("track", "get_track", None, 0, 1, 0, 0, 0, 0, 1),
        ("transport", "get_transport", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcpTransport", "get_rtcpTransport", None, 0, 1, 0, 0, 0, 0, 1),
        ("dtmf", "get_dtmf", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createEncodedStreams", "fn_createEncodedStreams", 0, 0, 1, 0, 0, 0, 0),
        ("getParameters", "fn_getParameters", 0, 0, 1, 0, 0, 0, 0),
        ("getStats", "fn_getStats", 0, 0, 1, 0, 1, 0, 0),
        ("replaceTrack", "fn_replaceTrack", 1, 0, 1, 0, 1, 0, 0),
        ("setParameters", "fn_setParameters", 1, 0, 1, 0, 1, 0, 0),
        ("setStreams", "fn_setStreams", 0, 0, 1, 0, 0, 0, 0),
        ("getCapabilities", "fn_getCapabilities", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_track(self):
        val = self._attr.get('track')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.track -> get attr')

    def get_transport(self):
        val = self._attr.get('transport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.transport -> get attr')

    def get_rtcpTransport(self):
        val = self._attr.get('rtcpTransport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.rtcpTransport -> get attr')

    def get_dtmf(self):
        val = self._attr.get('dtmf')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.dtmf -> get attr')

    def fn_createEncodedStreams(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.createEncodedStreams{tuple(args)} -> method')

    def fn_getParameters(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.getParameters{tuple(args)} -> method')

    def fn_getStats(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.getStats{tuple(args)} -> method')

    def fn_replaceTrack(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.replaceTrack{tuple(args)} -> method')

    def fn_setParameters(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.setParameters{tuple(args)} -> method')

    def fn_setStreams(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.setStreams{tuple(args)} -> method')

    @classmethod
    def fn_getCapabilities(cls, *args):
        logger.debug(f'patch -> v8_rtc_rtp_sender.py -> RTCRtpSender.getCapabilities{tuple(args)} -> method')
