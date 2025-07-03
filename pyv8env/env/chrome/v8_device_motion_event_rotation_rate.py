from .flags import *


@construct_100001
class DeviceMotionEventRotationRate:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("alpha", "get_alpha", None, 0, 1, 0, 0, 0, 0, 1),
        ("beta", "get_beta", None, 0, 1, 0, 0, 0, 0, 1),
        ("gamma", "get_gamma", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_alpha(self):
        val = self._attr.get('alpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event_rotation_rate.py -> DeviceMotionEventRotationRate.alpha -> get attr')

    def get_beta(self):
        val = self._attr.get('beta')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event_rotation_rate.py -> DeviceMotionEventRotationRate.beta -> get attr')

    def get_gamma(self):
        val = self._attr.get('gamma')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_motion_event_rotation_rate.py -> DeviceMotionEventRotationRate.gamma -> get attr')
