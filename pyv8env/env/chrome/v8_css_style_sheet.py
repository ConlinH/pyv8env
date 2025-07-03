from .flags import *
from .v8_style_sheet import StyleSheet


@construct_110001
class CSSStyleSheet(StyleSheet):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSStyleSheet, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("ownerRule", "get_ownerRule", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssRules", "get_cssRules", None, 0, 1, 0, 0, 0, 0, 1),
        ("rules", "get_rules", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addRule", "fn_addRule", 0, 0, 1, 0, 0, 0, 0),
        ("deleteRule", "fn_deleteRule", 1, 0, 1, 0, 0, 0, 0),
        ("insertRule", "fn_insertRule", 1, 0, 1, 0, 0, 0, 0),
        ("removeRule", "fn_removeRule", 0, 0, 1, 0, 0, 0, 0),
        ("replace", "fn_replace", 1, 0, 1, 0, 1, 0, 0),
        ("replaceSync", "fn_replaceSync", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_ownerRule(self):
        val = self._attr.get('ownerRule')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.ownerRule -> get attr')

    def get_cssRules(self):
        val = self._attr.get('cssRules')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.cssRules -> get attr')

    def get_rules(self):
        val = self._attr.get('rules')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.rules -> get attr')

    def fn_addRule(self, *args):
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.addRule{tuple(args)} -> method')

    def fn_deleteRule(self, *args):
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.deleteRule{tuple(args)} -> method')

    def fn_insertRule(self, *args):
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.insertRule{tuple(args)} -> method')

    def fn_removeRule(self, *args):
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.removeRule{tuple(args)} -> method')

    def fn_replace(self, *args):
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.replace{tuple(args)} -> method')

    def fn_replaceSync(self, *args):
        logger.debug(f'patch -> v8_css_style_sheet.py -> CSSStyleSheet.replaceSync{tuple(args)} -> method')
