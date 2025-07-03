from .flags import *
from .v8_event import Event


@construct_112001
class RTCDataChannelEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCDataChannelEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("channel", "get_channel", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_channel(self):
        val = self._attr.get('channel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel_event.py -> RTCDataChannelEvent.channel -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel_event.py -> RTCDataChannelEvent.isTrusted -> get attr')
