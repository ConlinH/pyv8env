from .flags import *


@construct_000000
class WebGLLoseContext:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("loseContext", "fn_loseContext", 0, 0, 1, 0, 0, 0, 0),
        ("restoreContext", "fn_restoreContext", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_loseContext(self, *args):
        logger.debug(f'patch -> v8_webgl_lose_context.py -> WebGLLoseContext.loseContext{tuple(args)} -> method')

    def fn_restoreContext(self, *args):
        logger.debug(f'patch -> v8_webgl_lose_context.py -> WebGLLoseContext.restoreContext{tuple(args)} -> method')
