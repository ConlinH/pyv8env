from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSFontPaletteValuesRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSFontPaletteValuesRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontFamily", "get_fontFamily", None, 0, 1, 0, 0, 0, 0, 1),
        ("basePalette", "get_basePalette", None, 0, 1, 0, 0, 0, 0, 1),
        ("overrideColors", "get_overrideColors", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_palette_values_rule.py -> CSSFontPaletteValuesRule.name -> get attr')

    def get_fontFamily(self):
        val = self._attr.get('fontFamily')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_palette_values_rule.py -> CSSFontPaletteValuesRule.fontFamily -> get attr')

    def get_basePalette(self):
        val = self._attr.get('basePalette')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_palette_values_rule.py -> CSSFontPaletteValuesRule.basePalette -> get attr')

    def get_overrideColors(self):
        val = self._attr.get('overrideColors')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_palette_values_rule.py -> CSSFontPaletteValuesRule.overrideColors -> get attr')
