from .flags import *


@construct_110001
class RTCSessionDescription:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("sdp", "get_sdp", "set_sdp", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_session_description.py -> RTCSessionDescription.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_sdp(self):
        val = self._attr.get('sdp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_session_description.py -> RTCSessionDescription.sdp -> get attr')

    def set_sdp(self, val):
        self._attr['sdp'] = val

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_rtc_session_description.py -> RTCSessionDescription.toJSON{tuple(args)} -> method')
