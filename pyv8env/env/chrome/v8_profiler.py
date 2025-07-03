from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class Profiler(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Profiler, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("sampleInterval", "get_sampleInterval", None, 0, 1, 0, 0, 0, 0, 1),
        ("stopped", "get_stopped", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("stop", "fn_stop", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_sampleInterval(self):
        val = self._attr.get('sampleInterval')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_profiler.py -> Profiler.sampleInterval -> get attr')

    def get_stopped(self):
        val = self._attr.get('stopped')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_profiler.py -> Profiler.stopped -> get attr')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_profiler.py -> Profiler.stop{tuple(args)} -> method')
