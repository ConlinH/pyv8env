from .flags import *


@construct_110001
class DOMRectReadOnly:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("top", "get_top", None, 0, 1, 0, 0, 0, 0, 1),
        ("right", "get_right", None, 0, 1, 0, 0, 0, 0, 1),
        ("bottom", "get_bottom", None, 0, 1, 0, 0, 0, 0, 1),
        ("left", "get_left", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("fromRect", "fn_fromRect", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.height -> get attr')

    def get_top(self):
        val = self._attr.get('top')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.top -> get attr')

    def get_right(self):
        val = self._attr.get('right')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.right -> get attr')

    def get_bottom(self):
        val = self._attr.get('bottom')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.bottom -> get attr')

    def get_left(self):
        val = self._attr.get('left')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.left -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.toJSON{tuple(args)} -> method')

    @classmethod
    def fn_fromRect(cls, *args):
        logger.debug(f'patch -> v8_dom_rect_read_only.py -> DOMRectReadOnly.fromRect{tuple(args)} -> method')
