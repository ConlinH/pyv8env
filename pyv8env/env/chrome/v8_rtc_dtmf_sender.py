from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class RTCDTMFSender(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RTCDTMFSender, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("ontonechange", "get_ontonechange", "set_ontonechange", 0, 1, 0, 0, 0, 0, 1),
        ("canInsertDTMF", "get_canInsertDTMF", None, 0, 1, 0, 0, 0, 0, 1),
        ("toneBuffer", "get_toneBuffer", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("insertDTMF", "fn_insertDTMF", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_ontonechange(self):
        val = self._attr.get('ontonechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_dtmf_sender.py -> RTCDTMFSender.ontonechange -> get attr')

    def set_ontonechange(self, val):
        self._attr['ontonechange'] = val

    def get_canInsertDTMF(self):
        val = self._attr.get('canInsertDTMF')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_dtmf_sender.py -> RTCDTMFSender.canInsertDTMF -> get attr')

    def get_toneBuffer(self):
        val = self._attr.get('toneBuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_dtmf_sender.py -> RTCDTMFSender.toneBuffer -> get attr')

    def fn_insertDTMF(self, *args):
        logger.debug(f'patch -> v8_rtc_dtmf_sender.py -> RTCDTMFSender.insertDTMF{tuple(args)} -> method')
