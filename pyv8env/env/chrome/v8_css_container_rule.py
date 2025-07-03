from .flags import *
from .v8_css_condition_rule import CSSConditionRule


@construct_100001
class CSSContainerRule(CSSConditionRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSContainerRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("containerName", "get_containerName", None, 0, 1, 0, 0, 0, 0, 1),
        ("containerQuery", "get_containerQuery", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_containerName(self):
        val = self._attr.get('containerName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_container_rule.py -> CSSContainerRule.containerName -> get attr')

    def get_containerQuery(self):
        val = self._attr.get('containerQuery')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_container_rule.py -> CSSContainerRule.containerQuery -> get attr')
