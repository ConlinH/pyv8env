from .flags import *


@construct_000000
class WebGLDrawInstancedBaseVertexBaseInstance:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("drawArraysInstancedBaseInstanceWEBGL", "fn_drawArraysInstancedBaseInstanceWEBGL", 5, 0, 1, 0, 0, 0, 0),
        ("drawElementsInstancedBaseVertexBaseInstanceWEBGL", "fn_drawElementsInstancedBaseVertexBaseInstanceWEBGL", 7, 0, 1, 0, 0, 0, 0),

    )

    def fn_drawArraysInstancedBaseInstanceWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_draw_instanced_base_vertex_base_instance.py -> WebGLDrawInstancedBaseVertexBaseInstance.drawArraysInstancedBaseInstanceWEBGL{tuple(args)} -> method')

    def fn_drawElementsInstancedBaseVertexBaseInstanceWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_draw_instanced_base_vertex_base_instance.py -> WebGLDrawInstancedBaseVertexBaseInstance.drawElementsInstancedBaseVertexBaseInstanceWEBGL{tuple(args)} -> method')
