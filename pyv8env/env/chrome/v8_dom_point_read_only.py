from .flags import *


@construct_110001
class DOMPointReadOnly:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("z", "get_z", None, 0, 1, 0, 0, 0, 0, 1),
        ("w", "get_w", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("matrixTransform", "fn_matrixTransform", 0, 0, 1, 0, 0, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("fromPoint", "fn_fromPoint", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point_read_only.py -> DOMPointReadOnly.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point_read_only.py -> DOMPointReadOnly.y -> get attr')

    def get_z(self):
        val = self._attr.get('z')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point_read_only.py -> DOMPointReadOnly.z -> get attr')

    def get_w(self):
        val = self._attr.get('w')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point_read_only.py -> DOMPointReadOnly.w -> get attr')

    def fn_matrixTransform(self, *args):
        logger.debug(f'patch -> v8_dom_point_read_only.py -> DOMPointReadOnly.matrixTransform{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_dom_point_read_only.py -> DOMPointReadOnly.toJSON{tuple(args)} -> method')

    @classmethod
    def fn_fromPoint(cls, *args):
        logger.debug(f'patch -> v8_dom_point_read_only.py -> DOMPointReadOnly.fromPoint{tuple(args)} -> method')
