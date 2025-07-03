from .flags import *
from .v8_dom_exception import DOMException


@construct_111001
class RTCError(DOMException):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCError, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("errorDetail", "get_errorDetail", None, 0, 1, 0, 0, 0, 0, 1),
        ("sdpLineNumber", "get_sdpLineNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("httpRequestStatusCode", "get_httpRequestStatusCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("sctpCauseCode", "get_sctpCauseCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("receivedAlert", "get_receivedAlert", None, 0, 1, 0, 0, 0, 0, 1),
        ("sentAlert", "get_sentAlert", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_errorDetail(self):
        val = self._attr.get('errorDetail')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_error.py -> RTCError.errorDetail -> get attr')

    def get_sdpLineNumber(self):
        val = self._attr.get('sdpLineNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_error.py -> RTCError.sdpLineNumber -> get attr')

    def get_httpRequestStatusCode(self):
        val = self._attr.get('httpRequestStatusCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_error.py -> RTCError.httpRequestStatusCode -> get attr')

    def get_sctpCauseCode(self):
        val = self._attr.get('sctpCauseCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_error.py -> RTCError.sctpCauseCode -> get attr')

    def get_receivedAlert(self):
        val = self._attr.get('receivedAlert')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_error.py -> RTCError.receivedAlert -> get attr')

    def get_sentAlert(self):
        val = self._attr.get('sentAlert')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_error.py -> RTCError.sentAlert -> get attr')
