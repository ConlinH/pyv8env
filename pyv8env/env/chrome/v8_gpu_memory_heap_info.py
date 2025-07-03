from .flags import *


@construct_100001
class GPUMemoryHeapInfo:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),
        ("properties", "get_properties", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_memory_heap_info.py -> GPUMemoryHeapInfo.size -> get attr')

    def get_properties(self):
        val = self._attr.get('properties')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_memory_heap_info.py -> GPUMemoryHeapInfo.properties -> get attr')
