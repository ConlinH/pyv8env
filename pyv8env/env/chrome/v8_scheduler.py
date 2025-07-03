from .flags import *


@construct_100001
class Scheduler:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("taskId", "get_taskId", "set_taskId", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("postTask", "fn_postTask", 1, 0, 1, 0, 1, 0, 0),
        ("yield", "fn_yield", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_taskId(self):
        val = self._attr.get('taskId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_scheduler.py -> Scheduler.taskId -> get attr')

    def set_taskId(self, val):
        self._attr['taskId'] = val

    def fn_postTask(self, *args):
        logger.debug(f'patch -> v8_scheduler.py -> Scheduler.postTask{tuple(args)} -> method')

    def fn_yield(self, *args):
        logger.debug(f'patch -> v8_scheduler.py -> Scheduler.yield{tuple(args)} -> method')
