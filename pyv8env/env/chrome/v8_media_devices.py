from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class MediaDevices(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaDevices, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("ondevicechange", "get_ondevicechange", "set_ondevicechange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("enumerateDevices", "fn_enumerateDevices", 0, 0, 1, 0, 1, 0, 0),
        ("getSupportedConstraints", "fn_getSupportedConstraints", 0, 0, 1, 0, 0, 0, 0),
        ("getUserMedia", "fn_getUserMedia", 0, 0, 1, 0, 1, 0, 0),
        ("getDisplayMedia", "fn_getDisplayMedia", 0, 0, 1, 0, 1, 0, 0),
        ("setCaptureHandleConfig", "fn_setCaptureHandleConfig", 0, 0, 1, 0, 0, 0, 0),
        ("getAllScreensMedia", "fn_getAllScreensMedia", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_ondevicechange(self):
        val = self._attr.get('ondevicechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_devices.py -> MediaDevices.ondevicechange -> get attr')

    def set_ondevicechange(self, val):
        self._attr['ondevicechange'] = val

    def fn_enumerateDevices(self, *args):
        logger.debug(f'patch -> v8_media_devices.py -> MediaDevices.enumerateDevices{tuple(args)} -> method')

    def fn_getSupportedConstraints(self, *args):
        logger.debug(f'patch -> v8_media_devices.py -> MediaDevices.getSupportedConstraints{tuple(args)} -> method')

    def fn_getUserMedia(self, *args):
        logger.debug(f'patch -> v8_media_devices.py -> MediaDevices.getUserMedia{tuple(args)} -> method')

    def fn_getDisplayMedia(self, *args):
        logger.debug(f'patch -> v8_media_devices.py -> MediaDevices.getDisplayMedia{tuple(args)} -> method')

    def fn_setCaptureHandleConfig(self, *args):
        logger.debug(f'patch -> v8_media_devices.py -> MediaDevices.setCaptureHandleConfig{tuple(args)} -> method')

    def fn_getAllScreensMedia(self, *args):
        logger.debug(f'patch -> v8_media_devices.py -> MediaDevices.getAllScreensMedia{tuple(args)} -> method')
