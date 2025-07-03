from .flags import *
from .v8_css_grouping_rule import CSSGroupingRule


@construct_100001
class CSSPageRule(CSSGroupingRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSPageRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("selectorText", "get_selectorText", "set_selectorText", 0, 1, 0, 0, 0, 0, 1),
        ("style", "get_style", "set_style", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_selectorText(self):
        val = self._attr.get('selectorText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_page_rule.py -> CSSPageRule.selectorText -> get attr')

    def set_selectorText(self, val):
        self._attr['selectorText'] = val

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_page_rule.py -> CSSPageRule.style -> get attr')

    def set_style(self, val):
        self._attr['style'] = val
