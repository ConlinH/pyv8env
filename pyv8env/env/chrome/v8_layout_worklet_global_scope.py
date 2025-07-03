from .flags import *
from .v8_worklet_global_scope import WorkletGlobalScope


@construct_100031
class LayoutWorkletGlobalScope(WorkletGlobalScope):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(LayoutWorkletGlobalScope, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("registerLayout", "fn_registerLayout", 2, 0, 0, 0, 0, 0, 0),

    )

    def fn_registerLayout(self, *args):
        logger.debug(f'patch -> v8_layout_worklet_global_scope.py -> LayoutWorkletGlobalScope.registerLayout{tuple(args)} -> method')
