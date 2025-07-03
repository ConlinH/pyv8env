from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSLayerStatementRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSLayerStatementRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("nameList", "get_nameList", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_nameList(self):
        val = self._attr.get('nameList')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_layer_statement_rule.py -> CSSLayerStatementRule.nameList -> get attr')
