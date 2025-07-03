from .flags import *


@construct_000000
class WebGLDebugShaders:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getTranslatedShaderSource", "fn_getTranslatedShaderSource", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_getTranslatedShaderSource(self, *args):
        logger.debug(f'patch -> v8_webgl_debug_shaders.py -> WebGLDebugShaders.getTranslatedShaderSource{tuple(args)} -> method')
