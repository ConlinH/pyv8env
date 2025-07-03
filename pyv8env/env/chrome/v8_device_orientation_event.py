from .flags import *
from .v8_event import Event


@construct_111001
class DeviceOrientationEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DeviceOrientationEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("alpha", "get_alpha", None, 0, 1, 0, 0, 0, 0, 1),
        ("beta", "get_beta", None, 0, 1, 0, 0, 0, 0, 1),
        ("gamma", "get_gamma", None, 0, 1, 0, 0, 0, 0, 1),
        ("absolute", "get_absolute", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("requestPermission", "fn_requestPermission", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_alpha(self):
        val = self._attr.get('alpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_orientation_event.py -> DeviceOrientationEvent.alpha -> get attr')

    def get_beta(self):
        val = self._attr.get('beta')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_orientation_event.py -> DeviceOrientationEvent.beta -> get attr')

    def get_gamma(self):
        val = self._attr.get('gamma')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_orientation_event.py -> DeviceOrientationEvent.gamma -> get attr')

    def get_absolute(self):
        val = self._attr.get('absolute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_orientation_event.py -> DeviceOrientationEvent.absolute -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_orientation_event.py -> DeviceOrientationEvent.isTrusted -> get attr')

    @classmethod
    def fn_requestPermission(cls, *args):
        logger.debug(f'patch -> v8_device_orientation_event.py -> DeviceOrientationEvent.requestPermission{tuple(args)} -> method')
