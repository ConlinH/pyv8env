from .flags import *
from .v8_css_grouping_rule import CSSGroupingRule


@construct_100001
class CSSConditionRule(CSSGroupingRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSConditionRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("conditionText", "get_conditionText", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_conditionText(self):
        val = self._attr.get('conditionText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_condition_rule.py -> CSSConditionRule.conditionText -> get attr')
