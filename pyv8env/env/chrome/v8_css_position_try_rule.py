from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSPositionTryRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSPositionTryRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("style", "get_style", "set_style", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_rule.py -> CSSPositionTryRule.name -> get attr')

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_rule.py -> CSSPositionTryRule.style -> get attr')

    def set_style(self, val):
        self._attr['style'] = val
