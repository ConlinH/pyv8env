from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSFontFaceRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSFontFaceRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("style", "get_style", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_face_rule.py -> CSSFontFaceRule.style -> get attr')
