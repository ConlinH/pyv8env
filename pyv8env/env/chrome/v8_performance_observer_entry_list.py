from .flags import *


@construct_100001
class PerformanceObserverEntryList:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getEntries", "fn_getEntries", 0, 0, 1, 0, 0, 0, 0),
        ("getEntriesByName", "fn_getEntriesByName", 1, 0, 1, 0, 0, 0, 0),
        ("getEntriesByType", "fn_getEntriesByType", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_getEntries(self, *args):
        logger.debug(f'patch -> v8_performance_observer_entry_list.py -> PerformanceObserverEntryList.getEntries{tuple(args)} -> method')

    def fn_getEntriesByName(self, *args):
        logger.debug(f'patch -> v8_performance_observer_entry_list.py -> PerformanceObserverEntryList.getEntriesByName{tuple(args)} -> method')

    def fn_getEntriesByType(self, *args):
        logger.debug(f'patch -> v8_performance_observer_entry_list.py -> PerformanceObserverEntryList.getEntriesByType{tuple(args)} -> method')
