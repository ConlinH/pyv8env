from .flags import *


@construct_100001
class GPUDeviceLostInfo:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("reason", "get_reason", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_reason(self):
        val = self._attr.get('reason')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device_lost_info.py -> GPUDeviceLostInfo.reason -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device_lost_info.py -> GPUDeviceLostInfo.message -> get attr')
