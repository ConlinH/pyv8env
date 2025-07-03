from .flags import *
from .v8_abort_controller import AbortController


@construct_110001
class TaskController(AbortController):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TaskController, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setPriority", "fn_setPriority", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_setPriority(self, *args):
        logger.debug(f'patch -> v8_task_controller.py -> TaskController.setPriority{tuple(args)} -> method')
