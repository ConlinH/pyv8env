from .flags import *


@construct_100101
class CSSStyleDeclaration:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_name_set__')
            
    def __v8_name_query__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_name_query__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_name_del__')
            
    def __v8_name_enum__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_name_enum__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("cssText", "get_cssText", "set_cssText", 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("parentRule", "get_parentRule", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssFloat", "get_cssFloat", "set_cssFloat", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPropertyPriority", "fn_getPropertyPriority", 1, 0, 1, 0, 0, 0, 0),
        ("getPropertyValue", "fn_getPropertyValue", 1, 0, 1, 0, 0, 0, 0),
        ("item", "fn_item", 1, 0, 1, 0, 0, 0, 1),
        ("removeProperty", "fn_removeProperty", 1, 0, 1, 0, 0, 0, 0),
        ("setProperty", "fn_setProperty", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_cssText(self):
        val = self._attr.get('cssText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.cssText -> get attr')

    def set_cssText(self, val):
        self._attr['cssText'] = val

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.length -> get attr')

    def get_parentRule(self):
        val = self._attr.get('parentRule')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.parentRule -> get attr')

    def get_cssFloat(self):
        val = self._attr.get('cssFloat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.cssFloat -> get attr')

    def set_cssFloat(self, val):
        self._attr['cssFloat'] = val

    def fn_getPropertyPriority(self, *args):
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.getPropertyPriority{tuple(args)} -> method')

    def fn_getPropertyValue(self, *args):
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.getPropertyValue{tuple(args)} -> method')

    def fn_item(self, *args):
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.item{tuple(args)} -> method')

    def fn_removeProperty(self, *args):
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.removeProperty{tuple(args)} -> method')

    def fn_setProperty(self, *args):
        logger.debug(f'patch -> v8_css_style_declaration.py -> CSSStyleDeclaration.setProperty{tuple(args)} -> method')
