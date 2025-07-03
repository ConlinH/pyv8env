from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSNamespaceRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSNamespaceRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("namespaceURI", "get_namespaceURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("prefix", "get_prefix", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_namespaceURI(self):
        val = self._attr.get('namespaceURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_namespace_rule.py -> CSSNamespaceRule.namespaceURI -> get attr')

    def get_prefix(self):
        val = self._attr.get('prefix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_namespace_rule.py -> CSSNamespaceRule.prefix -> get attr')
