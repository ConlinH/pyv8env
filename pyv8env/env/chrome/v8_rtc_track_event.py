from .flags import *
from .v8_event import Event


@construct_112001
class RTCTrackEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCTrackEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("receiver", "get_receiver", None, 0, 1, 0, 0, 0, 0, 1),
        ("track", "get_track", None, 0, 1, 0, 0, 0, 0, 1),
        ("streams", "get_streams", None, 0, 1, 0, 0, 0, 0, 1),
        ("transceiver", "get_transceiver", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_receiver(self):
        val = self._attr.get('receiver')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_track_event.py -> RTCTrackEvent.receiver -> get attr')

    def get_track(self):
        val = self._attr.get('track')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_track_event.py -> RTCTrackEvent.track -> get attr')

    def get_streams(self):
        val = self._attr.get('streams')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_track_event.py -> RTCTrackEvent.streams -> get attr')

    def get_transceiver(self):
        val = self._attr.get('transceiver')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_track_event.py -> RTCTrackEvent.transceiver -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_track_event.py -> RTCTrackEvent.isTrusted -> get attr')
