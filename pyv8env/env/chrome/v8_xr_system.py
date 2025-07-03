from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class XRSystem(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRSystem, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("ondevicechange", "get_ondevicechange", "set_ondevicechange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("isSessionSupported", "fn_isSessionSupported", 1, 0, 1, 0, 1, 0, 0),
        ("requestSession", "fn_requestSession", 1, 0, 1, 0, 1, 0, 0),
        ("supportsSession", "fn_supportsSession", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_ondevicechange(self):
        val = self._attr.get('ondevicechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_system.py -> XRSystem.ondevicechange -> get attr')

    def set_ondevicechange(self, val):
        self._attr['ondevicechange'] = val

    def fn_isSessionSupported(self, *args):
        logger.debug(f'patch -> v8_xr_system.py -> XRSystem.isSessionSupported{tuple(args)} -> method')

    def fn_requestSession(self, *args):
        logger.debug(f'patch -> v8_xr_system.py -> XRSystem.requestSession{tuple(args)} -> method')

    def fn_supportsSession(self, *args):
        logger.debug(f'patch -> v8_xr_system.py -> XRSystem.supportsSession{tuple(args)} -> method')
