from .flags import *


@construct_000000
class OESVertexArrayObject:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    VERTEX_ARRAY_BINDING_OES = 34229

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("bindVertexArrayOES", "fn_bindVertexArrayOES", 0, 0, 1, 0, 0, 0, 0),
        ("createVertexArrayOES", "fn_createVertexArrayOES", 0, 0, 1, 0, 0, 0, 0),
        ("deleteVertexArrayOES", "fn_deleteVertexArrayOES", 0, 0, 1, 0, 0, 0, 0),
        ("isVertexArrayOES", "fn_isVertexArrayOES", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_bindVertexArrayOES(self, *args):
        logger.debug(f'patch -> v8_oes_vertex_array_object.py -> OESVertexArrayObject.bindVertexArrayOES{tuple(args)} -> method')

    def fn_createVertexArrayOES(self, *args):
        logger.debug(f'patch -> v8_oes_vertex_array_object.py -> OESVertexArrayObject.createVertexArrayOES{tuple(args)} -> method')

    def fn_deleteVertexArrayOES(self, *args):
        logger.debug(f'patch -> v8_oes_vertex_array_object.py -> OESVertexArrayObject.deleteVertexArrayOES{tuple(args)} -> method')

    def fn_isVertexArrayOES(self, *args):
        logger.debug(f'patch -> v8_oes_vertex_array_object.py -> OESVertexArrayObject.isVertexArrayOES{tuple(args)} -> method')
