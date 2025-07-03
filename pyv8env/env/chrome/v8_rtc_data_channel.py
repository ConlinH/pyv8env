from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class RTCDataChannel(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCDataChannel, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("label", "get_label", None, 0, 1, 0, 0, 0, 0, 1),
        ("ordered", "get_ordered", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxPacketLifeTime", "get_maxPacketLifeTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxRetransmits", "get_maxRetransmits", None, 0, 1, 0, 0, 0, 0, 1),
        ("protocol", "get_protocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("negotiated", "get_negotiated", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("bufferedAmount", "get_bufferedAmount", None, 0, 1, 0, 0, 0, 0, 1),
        ("bufferedAmountLowThreshold", "get_bufferedAmountLowThreshold", "set_bufferedAmountLowThreshold", 0, 1, 0, 0, 0, 0, 1),
        ("onopen", "get_onopen", "set_onopen", 0, 1, 0, 0, 0, 0, 1),
        ("onbufferedamountlow", "get_onbufferedamountlow", "set_onbufferedamountlow", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onclosing", "get_onclosing", "set_onclosing", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),
        ("binaryType", "get_binaryType", "set_binaryType", 0, 1, 0, 0, 0, 0, 1),
        ("reliable", "get_reliable", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("send", "fn_send", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.label -> get attr')

    def get_ordered(self):
        val = self._attr.get('ordered')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.ordered -> get attr')

    def get_maxPacketLifeTime(self):
        val = self._attr.get('maxPacketLifeTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.maxPacketLifeTime -> get attr')

    def get_maxRetransmits(self):
        val = self._attr.get('maxRetransmits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.maxRetransmits -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.protocol -> get attr')

    def get_negotiated(self):
        val = self._attr.get('negotiated')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.negotiated -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.id -> get attr')

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.readyState -> get attr')

    def get_bufferedAmount(self):
        val = self._attr.get('bufferedAmount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.bufferedAmount -> get attr')

    def get_bufferedAmountLowThreshold(self):
        val = self._attr.get('bufferedAmountLowThreshold')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.bufferedAmountLowThreshold -> get attr')

    def set_bufferedAmountLowThreshold(self, val):
        self._attr['bufferedAmountLowThreshold'] = val

    def get_onopen(self):
        val = self._attr.get('onopen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.onopen -> get attr')

    def set_onopen(self, val):
        self._attr['onopen'] = val

    def get_onbufferedamountlow(self):
        val = self._attr.get('onbufferedamountlow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.onbufferedamountlow -> get attr')

    def set_onbufferedamountlow(self, val):
        self._attr['onbufferedamountlow'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onclosing(self):
        val = self._attr.get('onclosing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.onclosing -> get attr')

    def set_onclosing(self, val):
        self._attr['onclosing'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_binaryType(self):
        val = self._attr.get('binaryType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.binaryType -> get attr')

    def set_binaryType(self, val):
        self._attr['binaryType'] = val

    def get_reliable(self):
        val = self._attr.get('reliable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.reliable -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.close{tuple(args)} -> method')

    def fn_send(self, *args):
        logger.debug(f'patch -> v8_rtc_data_channel.py -> RTCDataChannel.send{tuple(args)} -> method')
