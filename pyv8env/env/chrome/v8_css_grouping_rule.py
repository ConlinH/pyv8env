from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSGroupingRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSGroupingRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("cssRules", "get_cssRules", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("deleteRule", "fn_deleteRule", 1, 0, 1, 0, 0, 0, 0),
        ("insertRule", "fn_insertRule", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_cssRules(self):
        val = self._attr.get('cssRules')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_grouping_rule.py -> CSSGroupingRule.cssRules -> get attr')

    def fn_deleteRule(self, *args):
        logger.debug(f'patch -> v8_css_grouping_rule.py -> CSSGroupingRule.deleteRule{tuple(args)} -> method')

    def fn_insertRule(self, *args):
        logger.debug(f'patch -> v8_css_grouping_rule.py -> CSSGroupingRule.insertRule{tuple(args)} -> method')
