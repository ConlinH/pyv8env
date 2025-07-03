from .flags import *


@construct_100001
class RTCRtpReceiver:
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
        ("playoutDelayHint", "get_playoutDelayHint", "set_playoutDelayHint", 0, 1, 0, 0, 0, 0, 1),
        ("jitterBufferTarget", "get_jitterBufferTarget", "set_jitterBufferTarget", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createEncodedStreams", "fn_createEncodedStreams", 0, 0, 1, 0, 0, 0, 0),
        ("getContributingSources", "fn_getContributingSources", 0, 0, 1, 0, 0, 0, 0),
        ("getParameters", "fn_getParameters", 0, 0, 1, 0, 0, 0, 0),
        ("getStats", "fn_getStats", 0, 0, 1, 0, 1, 0, 0),
        ("getSynchronizationSources", "fn_getSynchronizationSources", 0, 0, 1, 0, 0, 0, 0),
        ("getCapabilities", "fn_getCapabilities", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_track(self):
        val = self._attr.get('track')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.track -> get attr')

    def get_transport(self):
        val = self._attr.get('transport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.transport -> get attr')

    def get_rtcpTransport(self):
        val = self._attr.get('rtcpTransport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.rtcpTransport -> get attr')

    def get_playoutDelayHint(self):
        val = self._attr.get('playoutDelayHint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.playoutDelayHint -> get attr')

    def set_playoutDelayHint(self, val):
        self._attr['playoutDelayHint'] = val

    def get_jitterBufferTarget(self):
        val = self._attr.get('jitterBufferTarget')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.jitterBufferTarget -> get attr')

    def set_jitterBufferTarget(self, val):
        self._attr['jitterBufferTarget'] = val

    def fn_createEncodedStreams(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.createEncodedStreams{tuple(args)} -> method')

    def fn_getContributingSources(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.getContributingSources{tuple(args)} -> method')

    def fn_getParameters(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.getParameters{tuple(args)} -> method')

    def fn_getStats(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.getStats{tuple(args)} -> method')

    def fn_getSynchronizationSources(self, *args):
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.getSynchronizationSources{tuple(args)} -> method')

    @classmethod
    def fn_getCapabilities(cls, *args):
        logger.debug(f'patch -> v8_rtc_rtp_receiver.py -> RTCRtpReceiver.getCapabilities{tuple(args)} -> method')
