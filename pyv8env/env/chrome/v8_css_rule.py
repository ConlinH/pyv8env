from .flags import *


@construct_100001
class CSSRule:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    STYLE_RULE = 1
    CHARSET_RULE = 2
    IMPORT_RULE = 3
    MEDIA_RULE = 4
    FONT_FACE_RULE = 5
    PAGE_RULE = 6
    NAMESPACE_RULE = 10
    KEYFRAMES_RULE = 7
    KEYFRAME_RULE = 8
    COUNTER_STYLE_RULE = 11
    FONT_FEATURE_VALUES_RULE = 14
    SUPPORTS_RULE = 12

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssText", "get_cssText", "set_cssText", 0, 1, 0, 0, 0, 0, 1),
        ("parentRule", "get_parentRule", None, 0, 1, 0, 0, 0, 0, 1),
        ("parentStyleSheet", "get_parentStyleSheet", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rule.py -> CSSRule.type -> get attr')

    def get_cssText(self):
        val = self._attr.get('cssText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rule.py -> CSSRule.cssText -> get attr')

    def set_cssText(self, val):
        self._attr['cssText'] = val

    def get_parentRule(self):
        val = self._attr.get('parentRule')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rule.py -> CSSRule.parentRule -> get attr')

    def get_parentStyleSheet(self):
        val = self._attr.get('parentStyleSheet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_rule.py -> CSSRule.parentStyleSheet -> get attr')
