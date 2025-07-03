from .flags import *


@construct_100001
class SVGMatrix:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("a", "get_a", "set_a", 0, 1, 0, 0, 0, 0, 1),
        ("b", "get_b", "set_b", 0, 1, 0, 0, 0, 0, 1),
        ("c", "get_c", "set_c", 0, 1, 0, 0, 0, 0, 1),
        ("d", "get_d", "set_d", 0, 1, 0, 0, 0, 0, 1),
        ("e", "get_e", "set_e", 0, 1, 0, 0, 0, 0, 1),
        ("f", "get_f", "set_f", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("flipX", "fn_flipX", 0, 0, 1, 0, 0, 0, 0),
        ("flipY", "fn_flipY", 0, 0, 1, 0, 0, 0, 0),
        ("inverse", "fn_inverse", 0, 0, 1, 0, 0, 0, 0),
        ("multiply", "fn_multiply", 1, 0, 1, 0, 0, 0, 0),
        ("rotate", "fn_rotate", 1, 0, 1, 0, 0, 0, 0),
        ("rotateFromVector", "fn_rotateFromVector", 2, 0, 1, 0, 0, 0, 0),
        ("scale", "fn_scale", 1, 0, 1, 0, 0, 0, 0),
        ("scaleNonUniform", "fn_scaleNonUniform", 2, 0, 1, 0, 0, 0, 0),
        ("skewX", "fn_skewX", 1, 0, 1, 0, 0, 0, 0),
        ("skewY", "fn_skewY", 1, 0, 1, 0, 0, 0, 0),
        ("translate", "fn_translate", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_a(self):
        val = self._attr.get('a')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.a -> get attr')

    def set_a(self, val):
        self._attr['a'] = val

    def get_b(self):
        val = self._attr.get('b')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.b -> get attr')

    def set_b(self, val):
        self._attr['b'] = val

    def get_c(self):
        val = self._attr.get('c')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.c -> get attr')

    def set_c(self, val):
        self._attr['c'] = val

    def get_d(self):
        val = self._attr.get('d')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.d -> get attr')

    def set_d(self, val):
        self._attr['d'] = val

    def get_e(self):
        val = self._attr.get('e')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.e -> get attr')

    def set_e(self, val):
        self._attr['e'] = val

    def get_f(self):
        val = self._attr.get('f')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.f -> get attr')

    def set_f(self, val):
        self._attr['f'] = val

    def fn_flipX(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.flipX{tuple(args)} -> method')

    def fn_flipY(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.flipY{tuple(args)} -> method')

    def fn_inverse(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.inverse{tuple(args)} -> method')

    def fn_multiply(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.multiply{tuple(args)} -> method')

    def fn_rotate(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.rotate{tuple(args)} -> method')

    def fn_rotateFromVector(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.rotateFromVector{tuple(args)} -> method')

    def fn_scale(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.scale{tuple(args)} -> method')

    def fn_scaleNonUniform(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.scaleNonUniform{tuple(args)} -> method')

    def fn_skewX(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.skewX{tuple(args)} -> method')

    def fn_skewY(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.skewY{tuple(args)} -> method')

    def fn_translate(self, *args):
        logger.debug(f'patch -> v8_svg_matrix.py -> SVGMatrix.translate{tuple(args)} -> method')
