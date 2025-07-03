from .flags import *


@construct_000000
class ANGLEInstancedArrays:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE = 35070

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("drawArraysInstancedANGLE", "fn_drawArraysInstancedANGLE", 4, 0, 1, 0, 0, 0, 0),
        ("drawElementsInstancedANGLE", "fn_drawElementsInstancedANGLE", 5, 0, 1, 0, 0, 0, 0),
        ("vertexAttribDivisorANGLE", "fn_vertexAttribDivisorANGLE", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_drawArraysInstancedANGLE(self, *args):
        logger.debug(f'patch -> v8_angle_instanced_arrays.py -> ANGLEInstancedArrays.drawArraysInstancedANGLE{tuple(args)} -> method')

    def fn_drawElementsInstancedANGLE(self, *args):
        logger.debug(f'patch -> v8_angle_instanced_arrays.py -> ANGLEInstancedArrays.drawElementsInstancedANGLE{tuple(args)} -> method')

    def fn_vertexAttribDivisorANGLE(self, *args):
        logger.debug(f'patch -> v8_angle_instanced_arrays.py -> ANGLEInstancedArrays.vertexAttribDivisorANGLE{tuple(args)} -> method')
