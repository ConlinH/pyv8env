from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSPropertyRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSPropertyRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("syntax", "get_syntax", None, 0, 1, 0, 0, 0, 0, 1),
        ("inherits", "get_inherits", None, 0, 1, 0, 0, 0, 0, 1),
        ("initialValue", "get_initialValue", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_property_rule.py -> CSSPropertyRule.name -> get attr')

    def get_syntax(self):
        val = self._attr.get('syntax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_property_rule.py -> CSSPropertyRule.syntax -> get attr')

    def get_inherits(self):
        val = self._attr.get('inherits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_property_rule.py -> CSSPropertyRule.inherits -> get attr')

    def get_initialValue(self):
        val = self._attr.get('initialValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_property_rule.py -> CSSPropertyRule.initialValue -> get attr')
