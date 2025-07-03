from .flags import *
from .v8_worklet_global_scope import WorkletGlobalScope


@construct_100031
class PaintWorkletGlobalScope(WorkletGlobalScope):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PaintWorkletGlobalScope, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("devicePixelRatio", "get_devicePixelRatio", None, 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("registerPaint", "fn_registerPaint", 2, 0, 0, 0, 0, 0, 0),

    )

    def get_devicePixelRatio(self):
        val = self._attr.get('devicePixelRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_worklet_global_scope.py -> PaintWorkletGlobalScope.devicePixelRatio -> get attr')

    def fn_registerPaint(self, *args):
        logger.debug(f'patch -> v8_paint_worklet_global_scope.py -> PaintWorkletGlobalScope.registerPaint{tuple(args)} -> method')
