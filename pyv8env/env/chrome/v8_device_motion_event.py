from .flags import *
from .v8_event import Event


@construct_111001
class DeviceMotionEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DeviceMotionEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("acceleration", "get_acceleration", None, 0, 1, 0, 0, 0, 0, 1),
        ("accelerationIncludingGravity", "get_accelerationIncludingGravity", None, 0, 1, 0, 0, 0, 0, 1),
        ("rotationRate", "get_rotationRate", None, 0, 1, 0, 0, 0, 0, 1),
        ("interval", "get_interval", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("requestPermission", "fn_requestPermission", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_acceleration(self):
        val = self._attr.get('acceleration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event.py -> DeviceMotionEvent.acceleration -> get attr')

    def get_accelerationIncludingGravity(self):
        val = self._attr.get('accelerationIncludingGravity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event.py -> DeviceMotionEvent.accelerationIncludingGravity -> get attr')

    def get_rotationRate(self):
        val = self._attr.get('rotationRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event.py -> DeviceMotionEvent.rotationRate -> get attr')

    def get_interval(self):
        val = self._attr.get('interval')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event.py -> DeviceMotionEvent.interval -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event.py -> DeviceMotionEvent.isTrusted -> get attr')

    @classmethod
    def fn_requestPermission(cls, *args):
        logger.debug(f'patch -> v8_device_motion_event.py -> DeviceMotionEvent.requestPermission{tuple(args)} -> method')
