from .flags import *


@construct_000000
class WebGLProvokingVertex:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    FIRST_VERTEX_CONVENTION_WEBGL = 36429
    LAST_VERTEX_CONVENTION_WEBGL = 36430
    PROVOKING_VERTEX_WEBGL = 36431

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("provokingVertexWEBGL", "fn_provokingVertexWEBGL", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_provokingVertexWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_provoking_vertex.py -> WebGLProvokingVertex.provokingVertexWEBGL{tuple(args)} -> method')
