from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class RTCSctpTransport(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCSctpTransport, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("transport", "get_transport", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxMessageSize", "get_maxMessageSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxChannels", "get_maxChannels", None, 0, 1, 0, 0, 0, 0, 1),
        ("onstatechange", "get_onstatechange", "set_onstatechange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_transport(self):
        val = self._attr.get('transport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_sctp_transport.py -> RTCSctpTransport.transport -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_sctp_transport.py -> RTCSctpTransport.state -> get attr')

    def get_maxMessageSize(self):
        val = self._attr.get('maxMessageSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_sctp_transport.py -> RTCSctpTransport.maxMessageSize -> get attr')

    def get_maxChannels(self):
        val = self._attr.get('maxChannels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_sctp_transport.py -> RTCSctpTransport.maxChannels -> get attr')

    def get_onstatechange(self):
        val = self._attr.get('onstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_sctp_transport.py -> RTCSctpTransport.onstatechange -> get attr')

    def set_onstatechange(self, val):
        self._attr['onstatechange'] = val
