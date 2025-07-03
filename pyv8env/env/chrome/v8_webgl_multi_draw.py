from .flags import *


@construct_000000
class WebGLMultiDraw:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("multiDrawArraysInstancedWEBGL", "fn_multiDrawArraysInstancedWEBGL", 8, 0, 1, 0, 0, 0, 0),
        ("multiDrawArraysWEBGL", "fn_multiDrawArraysWEBGL", 6, 0, 1, 0, 0, 0, 0),
        ("multiDrawElementsInstancedWEBGL", "fn_multiDrawElementsInstancedWEBGL", 9, 0, 1, 0, 0, 0, 0),
        ("multiDrawElementsWEBGL", "fn_multiDrawElementsWEBGL", 7, 0, 1, 0, 0, 0, 0),

    )

    def fn_multiDrawArraysInstancedWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_multi_draw.py -> WebGLMultiDraw.multiDrawArraysInstancedWEBGL{tuple(args)} -> method')

    def fn_multiDrawArraysWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_multi_draw.py -> WebGLMultiDraw.multiDrawArraysWEBGL{tuple(args)} -> method')

    def fn_multiDrawElementsInstancedWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_multi_draw.py -> WebGLMultiDraw.multiDrawElementsInstancedWEBGL{tuple(args)} -> method')

    def fn_multiDrawElementsWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_multi_draw.py -> WebGLMultiDraw.multiDrawElementsWEBGL{tuple(args)} -> method')
