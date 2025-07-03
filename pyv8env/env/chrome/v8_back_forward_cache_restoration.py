from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class BackForwardCacheRestoration(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BackForwardCacheRestoration, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("pageshowEventStart", "get_pageshowEventStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageshowEventEnd", "get_pageshowEventEnd", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_pageshowEventStart(self):
        val = self._attr.get('pageshowEventStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_back_forward_cache_restoration.py -> BackForwardCacheRestoration.pageshowEventStart -> get attr')

    def get_pageshowEventEnd(self):
        val = self._attr.get('pageshowEventEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_back_forward_cache_restoration.py -> BackForwardCacheRestoration.pageshowEventEnd -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_back_forward_cache_restoration.py -> BackForwardCacheRestoration.toJSON{tuple(args)} -> method')
