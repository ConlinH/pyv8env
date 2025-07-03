from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSStyleRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSStyleRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("selectorText", "get_selectorText", "set_selectorText", 0, 1, 0, 0, 0, 0, 1),
        ("style", "get_style", "set_style", 0, 1, 0, 0, 0, 0, 1),
        ("styleMap", "get_styleMap", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssRules", "get_cssRules", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("deleteRule", "fn_deleteRule", 1, 0, 1, 0, 0, 0, 0),
        ("insertRule", "fn_insertRule", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_selectorText(self):
        val = self._attr.get('selectorText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_rule.py -> CSSStyleRule.selectorText -> get attr')

    def set_selectorText(self, val):
        self._attr['selectorText'] = val

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_rule.py -> CSSStyleRule.style -> get attr')

    def set_style(self, val):
        self._attr['style'] = val

    def get_styleMap(self):
        val = self._attr.get('styleMap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_rule.py -> CSSStyleRule.styleMap -> get attr')

    def get_cssRules(self):
        val = self._attr.get('cssRules')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_rule.py -> CSSStyleRule.cssRules -> get attr')

    def fn_deleteRule(self, *args):
        logger.debug(f'patch -> v8_css_style_rule.py -> CSSStyleRule.deleteRule{tuple(args)} -> method')

    def fn_insertRule(self, *args):
        logger.debug(f'patch -> v8_css_style_rule.py -> CSSStyleRule.insertRule{tuple(args)} -> method')
