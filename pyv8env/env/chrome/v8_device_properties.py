from .flags import *


@construct_110001
class DeviceProperties:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("uniqueId", "get_uniqueId", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_uniqueId(self):
        val = self._attr.get('uniqueId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_device_properties.py -> DeviceProperties.uniqueId -> get attr')
