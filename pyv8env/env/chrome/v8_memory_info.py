from .flags import *


@construct_000000
class MemoryInfo:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("totalJSHeapSize", "get_totalJSHeapSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("usedJSHeapSize", "get_usedJSHeapSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("jsHeapSizeLimit", "get_jsHeapSizeLimit", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_totalJSHeapSize(self):
        val = self._attr.get('totalJSHeapSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_memory_info.py -> MemoryInfo.totalJSHeapSize -> get attr')

    def get_usedJSHeapSize(self):
        val = self._attr.get('usedJSHeapSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_memory_info.py -> MemoryInfo.usedJSHeapSize -> get attr')

    def get_jsHeapSizeLimit(self):
        val = self._attr.get('jsHeapSizeLimit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_memory_info.py -> MemoryInfo.jsHeapSizeLimit -> get attr')
