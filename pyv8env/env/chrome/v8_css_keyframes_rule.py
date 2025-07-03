from .flags import *
from .v8_css_rule import CSSRule


@construct_100101
class CSSKeyframesRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSKeyframesRule, self).__init__(*args, **kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("cssRules", "get_cssRules", None, 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("appendRule", "fn_appendRule", 1, 0, 1, 0, 0, 0, 0),
        ("deleteRule", "fn_deleteRule", 1, 0, 1, 0, 0, 0, 0),
        ("findRule", "fn_findRule", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_cssRules(self):
        val = self._attr.get('cssRules')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.cssRules -> get attr')

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.length -> get attr')

    def fn_appendRule(self, *args):
        logger.debug(f'patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.appendRule{tuple(args)} -> method')

    def fn_deleteRule(self, *args):
        logger.debug(f'patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.deleteRule{tuple(args)} -> method')

    def fn_findRule(self, *args):
        logger.debug(f'patch -> v8_css_keyframes_rule.py -> CSSKeyframesRule.findRule{tuple(args)} -> method')
