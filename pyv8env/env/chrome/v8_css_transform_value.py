from .flags import *
from .v8_css_style_value import CSSStyleValue


@construct_1113101
class CSSTransformValue(CSSStyleValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSTransformValue, self).__init__(*args, **kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_css_transform_value.py -> CSSTransformValue.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_css_transform_value.py -> CSSTransformValue.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_css_transform_value.py -> CSSTransformValue.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_css_transform_value.py -> CSSTransformValue.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_css_transform_value.py -> CSSTransformValue.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_css_transform_value.py -> CSSTransformValue.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("is2D", "get_is2D", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toMatrix", "fn_toMatrix", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_transform_value.py -> CSSTransformValue.length -> get attr')

    def get_is2D(self):
        val = self._attr.get('is2D')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_transform_value.py -> CSSTransformValue.is2D -> get attr')

    def fn_toMatrix(self, *args):
        logger.debug(f'patch -> v8_css_transform_value.py -> CSSTransformValue.toMatrix{tuple(args)} -> method')
