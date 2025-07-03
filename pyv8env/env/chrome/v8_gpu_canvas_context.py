from .flags import *


@construct_100001
class GPUCanvasContext:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("canvas", "get_canvas", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("configure", "fn_configure", 1, 0, 1, 0, 0, 0, 0),
        ("getCurrentTexture", "fn_getCurrentTexture", 0, 0, 1, 0, 0, 0, 0),
        ("unconfigure", "fn_unconfigure", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_canvas(self):
        val = self._attr.get('canvas')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_canvas_context.py -> GPUCanvasContext.canvas -> get attr')

    def fn_configure(self, *args):
        logger.debug(f'patch -> v8_gpu_canvas_context.py -> GPUCanvasContext.configure{tuple(args)} -> method')

    def fn_getCurrentTexture(self, *args):
        logger.debug(f'patch -> v8_gpu_canvas_context.py -> GPUCanvasContext.getCurrentTexture{tuple(args)} -> method')

    def fn_unconfigure(self, *args):
        logger.debug(f'patch -> v8_gpu_canvas_context.py -> GPUCanvasContext.unconfigure{tuple(args)} -> method')
