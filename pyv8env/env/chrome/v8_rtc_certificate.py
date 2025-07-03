from .flags import *


@construct_100001
class RTCCertificate:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("expires", "get_expires", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getFingerprints", "fn_getFingerprints", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_expires(self):
        val = self._attr.get('expires')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_rtc_certificate.py -> RTCCertificate.expires -> get attr')

    def fn_getFingerprints(self, *args):
        logger.debug(f'patch -> v8_rtc_certificate.py -> RTCCertificate.getFingerprints{tuple(args)} -> method')
