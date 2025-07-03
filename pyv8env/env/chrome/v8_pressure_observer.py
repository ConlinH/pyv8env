from .flags import *


@construct_111001
class PressureObserver:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("knownSources", "get_knownSources", None, 0, 2, 0, 1, 1, 1, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("disconnect", "fn_disconnect", 0, 0, 1, 0, 0, 0, 0),
        ("observe", "fn_observe", 1, 0, 1, 0, 1, 0, 0),
        ("takeRecords", "fn_takeRecords", 0, 0, 1, 0, 0, 0, 0),
        ("unobserve", "fn_unobserve", 1, 0, 1, 0, 0, 0, 0),

    )

    @classmethod
    def get_knownSources(cls):
        logger.debug(f'patch -> v8_pressure_observer.py -> PressureObserver.knownSources -> get attr')

    def fn_disconnect(self, *args):
        logger.debug(f'patch -> v8_pressure_observer.py -> PressureObserver.disconnect{tuple(args)} -> method')

    def fn_observe(self, *args):
        logger.debug(f'patch -> v8_pressure_observer.py -> PressureObserver.observe{tuple(args)} -> method')

    def fn_takeRecords(self, *args):
        logger.debug(f'patch -> v8_pressure_observer.py -> PressureObserver.takeRecords{tuple(args)} -> method')

    def fn_unobserve(self, *args):
        logger.debug(f'patch -> v8_pressure_observer.py -> PressureObserver.unobserve{tuple(args)} -> method')
