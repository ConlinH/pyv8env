from .flags import *
from .v8_abort_signal import AbortSignal


@construct_100001
class TaskSignal(AbortSignal):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TaskSignal, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("priority", "get_priority", None, 0, 1, 0, 0, 0, 0, 1),
        ("onprioritychange", "get_onprioritychange", "set_onprioritychange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("any", "fn_any", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_priority(self):
        val = self._attr.get('priority')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_task_signal.py -> TaskSignal.priority -> get attr')

    def get_onprioritychange(self):
        val = self._attr.get('onprioritychange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_task_signal.py -> TaskSignal.onprioritychange -> get attr')

    def set_onprioritychange(self, val):
        self._attr['onprioritychange'] = val

    @classmethod
    def fn_any(cls, *args):
        logger.debug(f'patch -> v8_task_signal.py -> TaskSignal.any{tuple(args)} -> method')
