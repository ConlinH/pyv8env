from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class DevicePosture(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DevicePosture, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_posture.py -> DevicePosture.type -> get attr')

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_posture.py -> DevicePosture.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val
