from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSViewTransitionRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSViewTransitionRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("navigation", "get_navigation", None, 0, 1, 0, 0, 0, 0, 1),
        ("types", "get_types", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_navigation(self):
        val = self._attr.get('navigation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_view_transition_rule.py -> CSSViewTransitionRule.navigation -> get attr')

    def get_types(self):
        val = self._attr.get('types')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_view_transition_rule.py -> CSSViewTransitionRule.types -> get attr')
