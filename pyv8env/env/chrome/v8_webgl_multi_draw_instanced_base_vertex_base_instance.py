from .flags import *


@construct_000000
class WebGLMultiDrawInstancedBaseVertexBaseInstance:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("multiDrawArraysInstancedBaseInstanceWEBGL", "fn_multiDrawArraysInstancedBaseInstanceWEBGL", 10, 0, 1, 0, 0, 0, 0),
        ("multiDrawElementsInstancedBaseVertexBaseInstanceWEBGL", "fn_multiDrawElementsInstancedBaseVertexBaseInstanceWEBGL", 13, 0, 1, 0, 0, 0, 0),

    )

    def fn_multiDrawArraysInstancedBaseInstanceWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_multi_draw_instanced_base_vertex_base_instance.py -> WebGLMultiDrawInstancedBaseVertexBaseInstance.multiDrawArraysInstancedBaseInstanceWEBGL{tuple(args)} -> method')

    def fn_multiDrawElementsInstancedBaseVertexBaseInstanceWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_multi_draw_instanced_base_vertex_base_instance.py -> WebGLMultiDrawInstancedBaseVertexBaseInstance.multiDrawElementsInstancedBaseVertexBaseInstanceWEBGL{tuple(args)} -> method')
