from .flags import *


@construct_100001
class CSSTransformComponent:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("is2D", "get_is2D", "set_is2D", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toMatrix", "fn_toMatrix", 0, 0, 1, 0, 0, 0, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_is2D(self):
        val = self._attr.get('is2D')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_transform_component.py -> CSSTransformComponent.is2D -> get attr')

    def set_is2D(self, val):
        self._attr['is2D'] = val

    def fn_toMatrix(self, *args):
        logger.debug(f'patch -> v8_css_transform_component.py -> CSSTransformComponent.toMatrix{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_css_transform_component.py -> CSSTransformComponent.toString{tuple(args)} -> method')
