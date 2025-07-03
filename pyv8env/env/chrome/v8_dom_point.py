from .flags import *
from .v8_dom_point_read_only import DOMPointReadOnly


@construct_110001
class DOMPoint(DOMPointReadOnly):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DOMPoint, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", "set_x", 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", "set_y", 0, 1, 0, 0, 0, 0, 1),
        ("z", "get_z", "set_z", 0, 1, 0, 0, 0, 0, 1),
        ("w", "get_w", "set_w", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("fromPoint", "fn_fromPoint", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point.py -> DOMPoint.x -> get attr')

    def set_x(self, val):
        self._attr['x'] = val

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point.py -> DOMPoint.y -> get attr')

    def set_y(self, val):
        self._attr['y'] = val

    def get_z(self):
        val = self._attr.get('z')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point.py -> DOMPoint.z -> get attr')

    def set_z(self, val):
        self._attr['z'] = val

    def get_w(self):
        val = self._attr.get('w')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_point.py -> DOMPoint.w -> get attr')

    def set_w(self, val):
        self._attr['w'] = val

    @classmethod
    def fn_fromPoint(cls, *args):
        logger.debug(f'patch -> v8_dom_point.py -> DOMPoint.fromPoint{tuple(args)} -> method')
