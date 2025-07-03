from .flags import *


@construct_000001
class WorkerInternals:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("collectGarbage", "fn_collectGarbage", 0, 0, 1, 0, 0, 0, 0),
        ("countDeprecation", "fn_countDeprecation", 1, 0, 1, 0, 0, 0, 0),
        ("countFeature", "fn_countFeature", 1, 0, 1, 0, 0, 0, 0),
        ("getInitialResourcePriority", "fn_getInitialResourcePriority", 2, 0, 1, 0, 1, 0, 0),
        ("getInternalResponseURLList", "fn_getInternalResponseURLList", 1, 0, 1, 0, 0, 0, 0),
        ("originTrialsTest", "fn_originTrialsTest", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_collectGarbage(self, *args):
        logger.debug(f'patch -> v8_worker_internals.py -> WorkerInternals.collectGarbage{tuple(args)} -> method')

    def fn_countDeprecation(self, *args):
        logger.debug(f'patch -> v8_worker_internals.py -> WorkerInternals.countDeprecation{tuple(args)} -> method')

    def fn_countFeature(self, *args):
        logger.debug(f'patch -> v8_worker_internals.py -> WorkerInternals.countFeature{tuple(args)} -> method')

    def fn_getInitialResourcePriority(self, *args):
        logger.debug(f'patch -> v8_worker_internals.py -> WorkerInternals.getInitialResourcePriority{tuple(args)} -> method')

    def fn_getInternalResponseURLList(self, *args):
        logger.debug(f'patch -> v8_worker_internals.py -> WorkerInternals.getInternalResponseURLList{tuple(args)} -> method')

    def fn_originTrialsTest(self, *args):
        logger.debug(f'patch -> v8_worker_internals.py -> WorkerInternals.originTrialsTest{tuple(args)} -> method')
