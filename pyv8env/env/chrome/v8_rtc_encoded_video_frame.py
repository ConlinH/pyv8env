from .flags import *


@construct_111001
class RTCEncodedVideoFrame:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", "set_data", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getMetadata", "fn_getMetadata", 0, 0, 1, 0, 0, 0, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),
        ("setMetadata", "fn_setMetadata", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_encoded_video_frame.py -> RTCEncodedVideoFrame.type -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_encoded_video_frame.py -> RTCEncodedVideoFrame.timestamp -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_encoded_video_frame.py -> RTCEncodedVideoFrame.data -> get attr')

    def set_data(self, val):
        self._attr['data'] = val

    def fn_getMetadata(self, *args):
        logger.debug(f'patch -> v8_rtc_encoded_video_frame.py -> RTCEncodedVideoFrame.getMetadata{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_rtc_encoded_video_frame.py -> RTCEncodedVideoFrame.toString{tuple(args)} -> method')

    def fn_setMetadata(self, *args):
        logger.debug(f'patch -> v8_rtc_encoded_video_frame.py -> RTCEncodedVideoFrame.setMetadata{tuple(args)} -> method')
