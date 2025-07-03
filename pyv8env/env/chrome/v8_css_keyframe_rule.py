from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSKeyframeRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSKeyframeRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("keyText", "get_keyText", "set_keyText", 0, 1, 0, 0, 0, 0, 1),
        ("style", "get_style", "set_style", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_keyText(self):
        val = self._attr.get('keyText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_keyframe_rule.py -> CSSKeyframeRule.keyText -> get attr')

    def set_keyText(self, val):
        self._attr['keyText'] = val

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_keyframe_rule.py -> CSSKeyframeRule.style -> get attr')

    def set_style(self, val):
        self._attr['style'] = val
