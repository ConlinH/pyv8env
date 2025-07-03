from .flags import *


@construct_110001
class DOMMatrixReadOnly:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("a", "get_a", None, 0, 1, 0, 0, 0, 0, 1),
        ("b", "get_b", None, 0, 1, 0, 0, 0, 0, 1),
        ("c", "get_c", None, 0, 1, 0, 0, 0, 0, 1),
        ("d", "get_d", None, 0, 1, 0, 0, 0, 0, 1),
        ("e", "get_e", None, 0, 1, 0, 0, 0, 0, 1),
        ("f", "get_f", None, 0, 1, 0, 0, 0, 0, 1),
        ("m11", "get_m11", None, 0, 1, 0, 0, 0, 0, 1),
        ("m12", "get_m12", None, 0, 1, 0, 0, 0, 0, 1),
        ("m13", "get_m13", None, 0, 1, 0, 0, 0, 0, 1),
        ("m14", "get_m14", None, 0, 1, 0, 0, 0, 0, 1),
        ("m21", "get_m21", None, 0, 1, 0, 0, 0, 0, 1),
        ("m22", "get_m22", None, 0, 1, 0, 0, 0, 0, 1),
        ("m23", "get_m23", None, 0, 1, 0, 0, 0, 0, 1),
        ("m24", "get_m24", None, 0, 1, 0, 0, 0, 0, 1),
        ("m31", "get_m31", None, 0, 1, 0, 0, 0, 0, 1),
        ("m32", "get_m32", None, 0, 1, 0, 0, 0, 0, 1),
        ("m33", "get_m33", None, 0, 1, 0, 0, 0, 0, 1),
        ("m34", "get_m34", None, 0, 1, 0, 0, 0, 0, 1),
        ("m41", "get_m41", None, 0, 1, 0, 0, 0, 0, 1),
        ("m42", "get_m42", None, 0, 1, 0, 0, 0, 0, 1),
        ("m43", "get_m43", None, 0, 1, 0, 0, 0, 0, 1),
        ("m44", "get_m44", None, 0, 1, 0, 0, 0, 0, 1),
        ("is2D", "get_is2D", None, 0, 1, 0, 0, 0, 0, 1),
        ("isIdentity", "get_isIdentity", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("flipX", "fn_flipX", 0, 0, 1, 0, 0, 0, 0),
        ("flipY", "fn_flipY", 0, 0, 1, 0, 0, 0, 0),
        ("inverse", "fn_inverse", 0, 0, 1, 0, 0, 0, 0),
        ("multiply", "fn_multiply", 0, 0, 1, 0, 0, 0, 0),
        ("rotate", "fn_rotate", 0, 0, 1, 0, 0, 0, 0),
        ("rotateAxisAngle", "fn_rotateAxisAngle", 0, 0, 1, 0, 0, 0, 0),
        ("rotateFromVector", "fn_rotateFromVector", 0, 0, 1, 0, 0, 0, 0),
        ("scale", "fn_scale", 0, 0, 1, 0, 0, 0, 0),
        ("scale3d", "fn_scale3d", 0, 0, 1, 0, 0, 0, 0),
        ("scaleNonUniform", "fn_scaleNonUniform", 0, 0, 1, 0, 0, 0, 0),
        ("skewX", "fn_skewX", 0, 0, 1, 0, 0, 0, 0),
        ("skewY", "fn_skewY", 0, 0, 1, 0, 0, 0, 0),
        ("toFloat32Array", "fn_toFloat32Array", 0, 0, 1, 0, 0, 0, 0),
        ("toFloat64Array", "fn_toFloat64Array", 0, 0, 1, 0, 0, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("transformPoint", "fn_transformPoint", 0, 0, 1, 0, 0, 0, 0),
        ("translate", "fn_translate", 0, 0, 1, 0, 0, 0, 0),
        ("fromFloat32Array", "fn_fromFloat32Array", 1, 0, 2, 0, 1, 1, 0),
        ("fromFloat64Array", "fn_fromFloat64Array", 1, 0, 2, 0, 1, 1, 0),
        ("fromMatrix", "fn_fromMatrix", 0, 0, 2, 0, 1, 1, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_a(self):
        val = self._attr.get('a')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.a -> get attr')

    def get_b(self):
        val = self._attr.get('b')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.b -> get attr')

    def get_c(self):
        val = self._attr.get('c')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.c -> get attr')

    def get_d(self):
        val = self._attr.get('d')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.d -> get attr')

    def get_e(self):
        val = self._attr.get('e')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.e -> get attr')

    def get_f(self):
        val = self._attr.get('f')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.f -> get attr')

    def get_m11(self):
        val = self._attr.get('m11')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m11 -> get attr')

    def get_m12(self):
        val = self._attr.get('m12')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m12 -> get attr')

    def get_m13(self):
        val = self._attr.get('m13')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m13 -> get attr')

    def get_m14(self):
        val = self._attr.get('m14')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m14 -> get attr')

    def get_m21(self):
        val = self._attr.get('m21')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m21 -> get attr')

    def get_m22(self):
        val = self._attr.get('m22')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m22 -> get attr')

    def get_m23(self):
        val = self._attr.get('m23')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m23 -> get attr')

    def get_m24(self):
        val = self._attr.get('m24')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m24 -> get attr')

    def get_m31(self):
        val = self._attr.get('m31')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m31 -> get attr')

    def get_m32(self):
        val = self._attr.get('m32')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m32 -> get attr')

    def get_m33(self):
        val = self._attr.get('m33')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m33 -> get attr')

    def get_m34(self):
        val = self._attr.get('m34')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m34 -> get attr')

    def get_m41(self):
        val = self._attr.get('m41')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m41 -> get attr')

    def get_m42(self):
        val = self._attr.get('m42')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m42 -> get attr')

    def get_m43(self):
        val = self._attr.get('m43')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m43 -> get attr')

    def get_m44(self):
        val = self._attr.get('m44')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.m44 -> get attr')

    def get_is2D(self):
        val = self._attr.get('is2D')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.is2D -> get attr')

    def get_isIdentity(self):
        val = self._attr.get('isIdentity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.isIdentity -> get attr')

    def fn_flipX(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.flipX{tuple(args)} -> method')

    def fn_flipY(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.flipY{tuple(args)} -> method')

    def fn_inverse(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.inverse{tuple(args)} -> method')

    def fn_multiply(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.multiply{tuple(args)} -> method')

    def fn_rotate(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.rotate{tuple(args)} -> method')

    def fn_rotateAxisAngle(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.rotateAxisAngle{tuple(args)} -> method')

    def fn_rotateFromVector(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.rotateFromVector{tuple(args)} -> method')

    def fn_scale(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.scale{tuple(args)} -> method')

    def fn_scale3d(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.scale3d{tuple(args)} -> method')

    def fn_scaleNonUniform(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.scaleNonUniform{tuple(args)} -> method')

    def fn_skewX(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.skewX{tuple(args)} -> method')

    def fn_skewY(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.skewY{tuple(args)} -> method')

    def fn_toFloat32Array(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.toFloat32Array{tuple(args)} -> method')

    def fn_toFloat64Array(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.toFloat64Array{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.toJSON{tuple(args)} -> method')

    def fn_transformPoint(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.transformPoint{tuple(args)} -> method')

    def fn_translate(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.translate{tuple(args)} -> method')

    @classmethod
    def fn_fromFloat32Array(cls, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.fromFloat32Array{tuple(args)} -> method')

    @classmethod
    def fn_fromFloat64Array(cls, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.fromFloat64Array{tuple(args)} -> method')

    @classmethod
    def fn_fromMatrix(cls, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.fromMatrix{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_dom_matrix_read_only.py -> DOMMatrixReadOnly.toString{tuple(args)} -> method')
