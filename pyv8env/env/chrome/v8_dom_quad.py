from .flags import *


@construct_110001
class DOMQuad:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("p1", "get_p1", None, 0, 1, 0, 0, 0, 0, 1),
        ("p2", "get_p2", None, 0, 1, 0, 0, 0, 0, 1),
        ("p3", "get_p3", None, 0, 1, 0, 0, 0, 0, 1),
        ("p4", "get_p4", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getBounds", "fn_getBounds", 0, 0, 1, 0, 0, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("fromQuad", "fn_fromQuad", 0, 0, 2, 0, 1, 1, 0),
        ("fromRect", "fn_fromRect", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_p1(self):
        val = self._attr.get('p1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.p1 -> get attr')

    def get_p2(self):
        val = self._attr.get('p2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.p2 -> get attr')

    def get_p3(self):
        val = self._attr.get('p3')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.p3 -> get attr')

    def get_p4(self):
        val = self._attr.get('p4')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.p4 -> get attr')

    def fn_getBounds(self, *args):
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.getBounds{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.toJSON{tuple(args)} -> method')

    @classmethod
    def fn_fromQuad(cls, *args):
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.fromQuad{tuple(args)} -> method')

    @classmethod
    def fn_fromRect(cls, *args):
        logger.debug(f'patch -> v8_dom_quad.py -> DOMQuad.fromRect{tuple(args)} -> method')
