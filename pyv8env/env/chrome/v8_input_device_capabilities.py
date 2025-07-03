from .flags import *


@construct_110001
class InputDeviceCapabilities:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("firesTouchEvents", "get_firesTouchEvents", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_firesTouchEvents(self):
        val = self._attr.get('firesTouchEvents')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_input_device_capabilities.py -> InputDeviceCapabilities.firesTouchEvents -> get attr')
