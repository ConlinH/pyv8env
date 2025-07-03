from .flags import *
from .v8_dom_matrix_read_only import DOMMatrixReadOnly


@construct_110001
class DOMMatrix(DOMMatrixReadOnly):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DOMMatrix, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("a", "get_a", "set_a", 0, 1, 0, 0, 0, 0, 1),
        ("b", "get_b", "set_b", 0, 1, 0, 0, 0, 0, 1),
        ("c", "get_c", "set_c", 0, 1, 0, 0, 0, 0, 1),
        ("d", "get_d", "set_d", 0, 1, 0, 0, 0, 0, 1),
        ("e", "get_e", "set_e", 0, 1, 0, 0, 0, 0, 1),
        ("f", "get_f", "set_f", 0, 1, 0, 0, 0, 0, 1),
        ("m11", "get_m11", "set_m11", 0, 1, 0, 0, 0, 0, 1),
        ("m12", "get_m12", "set_m12", 0, 1, 0, 0, 0, 0, 1),
        ("m13", "get_m13", "set_m13", 0, 1, 0, 0, 0, 0, 1),
        ("m14", "get_m14", "set_m14", 0, 1, 0, 0, 0, 0, 1),
        ("m21", "get_m21", "set_m21", 0, 1, 0, 0, 0, 0, 1),
        ("m22", "get_m22", "set_m22", 0, 1, 0, 0, 0, 0, 1),
        ("m23", "get_m23", "set_m23", 0, 1, 0, 0, 0, 0, 1),
        ("m24", "get_m24", "set_m24", 0, 1, 0, 0, 0, 0, 1),
        ("m31", "get_m31", "set_m31", 0, 1, 0, 0, 0, 0, 1),
        ("m32", "get_m32", "set_m32", 0, 1, 0, 0, 0, 0, 1),
        ("m33", "get_m33", "set_m33", 0, 1, 0, 0, 0, 0, 1),
        ("m34", "get_m34", "set_m34", 0, 1, 0, 0, 0, 0, 1),
        ("m41", "get_m41", "set_m41", 0, 1, 0, 0, 0, 0, 1),
        ("m42", "get_m42", "set_m42", 0, 1, 0, 0, 0, 0, 1),
        ("m43", "get_m43", "set_m43", 0, 1, 0, 0, 0, 0, 1),
        ("m44", "get_m44", "set_m44", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("invertSelf", "fn_invertSelf", 0, 0, 1, 0, 0, 0, 0),
        ("multiplySelf", "fn_multiplySelf", 0, 0, 1, 0, 0, 0, 0),
        ("preMultiplySelf", "fn_preMultiplySelf", 0, 0, 1, 0, 0, 0, 0),
        ("rotateAxisAngleSelf", "fn_rotateAxisAngleSelf", 0, 0, 1, 0, 0, 0, 0),
        ("rotateFromVectorSelf", "fn_rotateFromVectorSelf", 0, 0, 1, 0, 0, 0, 0),
        ("rotateSelf", "fn_rotateSelf", 0, 0, 1, 0, 0, 0, 0),
        ("scale3dSelf", "fn_scale3dSelf", 0, 0, 1, 0, 0, 0, 0),
        ("scaleSelf", "fn_scaleSelf", 0, 0, 1, 0, 0, 0, 0),
        ("skewXSelf", "fn_skewXSelf", 0, 0, 1, 0, 0, 0, 0),
        ("skewYSelf", "fn_skewYSelf", 0, 0, 1, 0, 0, 0, 0),
        ("translateSelf", "fn_translateSelf", 0, 0, 1, 0, 0, 0, 0),
        ("fromFloat32Array", "fn_fromFloat32Array", 1, 0, 2, 0, 1, 1, 0),
        ("fromFloat64Array", "fn_fromFloat64Array", 1, 0, 2, 0, 1, 1, 0),
        ("fromMatrix", "fn_fromMatrix", 0, 0, 2, 0, 1, 1, 0),
        ("setMatrixValue", "fn_setMatrixValue", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_a(self):
        val = self._attr.get('a')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.a -> get attr')

    def set_a(self, val):
        self._attr['a'] = val

    def get_b(self):
        val = self._attr.get('b')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.b -> get attr')

    def set_b(self, val):
        self._attr['b'] = val

    def get_c(self):
        val = self._attr.get('c')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.c -> get attr')

    def set_c(self, val):
        self._attr['c'] = val

    def get_d(self):
        val = self._attr.get('d')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.d -> get attr')

    def set_d(self, val):
        self._attr['d'] = val

    def get_e(self):
        val = self._attr.get('e')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.e -> get attr')

    def set_e(self, val):
        self._attr['e'] = val

    def get_f(self):
        val = self._attr.get('f')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.f -> get attr')

    def set_f(self, val):
        self._attr['f'] = val

    def get_m11(self):
        val = self._attr.get('m11')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m11 -> get attr')

    def set_m11(self, val):
        self._attr['m11'] = val

    def get_m12(self):
        val = self._attr.get('m12')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m12 -> get attr')

    def set_m12(self, val):
        self._attr['m12'] = val

    def get_m13(self):
        val = self._attr.get('m13')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m13 -> get attr')

    def set_m13(self, val):
        self._attr['m13'] = val

    def get_m14(self):
        val = self._attr.get('m14')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m14 -> get attr')

    def set_m14(self, val):
        self._attr['m14'] = val

    def get_m21(self):
        val = self._attr.get('m21')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m21 -> get attr')

    def set_m21(self, val):
        self._attr['m21'] = val

    def get_m22(self):
        val = self._attr.get('m22')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m22 -> get attr')

    def set_m22(self, val):
        self._attr['m22'] = val

    def get_m23(self):
        val = self._attr.get('m23')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m23 -> get attr')

    def set_m23(self, val):
        self._attr['m23'] = val

    def get_m24(self):
        val = self._attr.get('m24')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m24 -> get attr')

    def set_m24(self, val):
        self._attr['m24'] = val

    def get_m31(self):
        val = self._attr.get('m31')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m31 -> get attr')

    def set_m31(self, val):
        self._attr['m31'] = val

    def get_m32(self):
        val = self._attr.get('m32')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m32 -> get attr')

    def set_m32(self, val):
        self._attr['m32'] = val

    def get_m33(self):
        val = self._attr.get('m33')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m33 -> get attr')

    def set_m33(self, val):
        self._attr['m33'] = val

    def get_m34(self):
        val = self._attr.get('m34')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m34 -> get attr')

    def set_m34(self, val):
        self._attr['m34'] = val

    def get_m41(self):
        val = self._attr.get('m41')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m41 -> get attr')

    def set_m41(self, val):
        self._attr['m41'] = val

    def get_m42(self):
        val = self._attr.get('m42')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m42 -> get attr')

    def set_m42(self, val):
        self._attr['m42'] = val

    def get_m43(self):
        val = self._attr.get('m43')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m43 -> get attr')

    def set_m43(self, val):
        self._attr['m43'] = val

    def get_m44(self):
        val = self._attr.get('m44')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.m44 -> get attr')

    def set_m44(self, val):
        self._attr['m44'] = val

    def fn_invertSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.invertSelf{tuple(args)} -> method')

    def fn_multiplySelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.multiplySelf{tuple(args)} -> method')

    def fn_preMultiplySelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.preMultiplySelf{tuple(args)} -> method')

    def fn_rotateAxisAngleSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.rotateAxisAngleSelf{tuple(args)} -> method')

    def fn_rotateFromVectorSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.rotateFromVectorSelf{tuple(args)} -> method')

    def fn_rotateSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.rotateSelf{tuple(args)} -> method')

    def fn_scale3dSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.scale3dSelf{tuple(args)} -> method')

    def fn_scaleSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.scaleSelf{tuple(args)} -> method')

    def fn_skewXSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.skewXSelf{tuple(args)} -> method')

    def fn_skewYSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.skewYSelf{tuple(args)} -> method')

    def fn_translateSelf(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.translateSelf{tuple(args)} -> method')

    @classmethod
    def fn_fromFloat32Array(cls, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.fromFloat32Array{tuple(args)} -> method')

    @classmethod
    def fn_fromFloat64Array(cls, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.fromFloat64Array{tuple(args)} -> method')

    @classmethod
    def fn_fromMatrix(cls, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.fromMatrix{tuple(args)} -> method')

    def fn_setMatrixValue(self, *args):
        logger.debug(f'patch -> v8_dom_matrix.py -> DOMMatrix.setMatrixValue{tuple(args)} -> method')
