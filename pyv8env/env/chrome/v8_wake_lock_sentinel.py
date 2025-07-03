from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class WakeLockSentinel(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WakeLockSentinel, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onrelease", "get_onrelease", "set_onrelease", 0, 1, 0, 0, 0, 0, 1),
        ("released", "get_released", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("release", "fn_release", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_onrelease(self):
        val = self._attr.get('onrelease')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wake_lock_sentinel.py -> WakeLockSentinel.onrelease -> get attr')

    def set_onrelease(self, val):
        self._attr['onrelease'] = val

    def get_released(self):
        val = self._attr.get('released')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wake_lock_sentinel.py -> WakeLockSentinel.released -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wake_lock_sentinel.py -> WakeLockSentinel.type -> get attr')

    def fn_release(self, *args):
        logger.debug(f'patch -> v8_wake_lock_sentinel.py -> WakeLockSentinel.release{tuple(args)} -> method')
