from .flags import *


@construct_100001
class LayoutChild:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("styleMap", "get_styleMap", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("intrinsicSizes", "fn_intrinsicSizes", 0, 0, 1, 0, 1, 0, 0),
        ("layoutNextFragment", "fn_layoutNextFragment", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_styleMap(self):
        val = self._attr.get('styleMap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_child.py -> LayoutChild.styleMap -> get attr')

    def fn_intrinsicSizes(self, *args):
        logger.debug(f'patch -> v8_layout_child.py -> LayoutChild.intrinsicSizes{tuple(args)} -> method')

    def fn_layoutNextFragment(self, *args):
        logger.debug(f'patch -> v8_layout_child.py -> LayoutChild.layoutNextFragment{tuple(args)} -> method')
