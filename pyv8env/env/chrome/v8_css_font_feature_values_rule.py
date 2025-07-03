from .flags import *
from .v8_css_rule import CSSRule


@construct_000001
class CSSFontFeatureValuesRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSFontFeatureValuesRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("fontFamily", "get_fontFamily", "set_fontFamily", 0, 1, 0, 0, 0, 0, 1),
        ("annotation", "get_annotation", None, 0, 1, 0, 0, 0, 0, 1),
        ("ornaments", "get_ornaments", None, 0, 1, 0, 0, 0, 0, 1),
        ("stylistic", "get_stylistic", None, 0, 1, 0, 0, 0, 0, 1),
        ("swash", "get_swash", None, 0, 1, 0, 0, 0, 0, 1),
        ("characterVariant", "get_characterVariant", None, 0, 1, 0, 0, 0, 0, 1),
        ("styleset", "get_styleset", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_fontFamily(self):
        val = self._attr.get('fontFamily')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_rule.py -> CSSFontFeatureValuesRule.fontFamily -> get attr')

    def set_fontFamily(self, val):
        self._attr['fontFamily'] = val

    def get_annotation(self):
        val = self._attr.get('annotation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_rule.py -> CSSFontFeatureValuesRule.annotation -> get attr')

    def get_ornaments(self):
        val = self._attr.get('ornaments')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_rule.py -> CSSFontFeatureValuesRule.ornaments -> get attr')

    def get_stylistic(self):
        val = self._attr.get('stylistic')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_rule.py -> CSSFontFeatureValuesRule.stylistic -> get attr')

    def get_swash(self):
        val = self._attr.get('swash')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_rule.py -> CSSFontFeatureValuesRule.swash -> get attr')

    def get_characterVariant(self):
        val = self._attr.get('characterVariant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_rule.py -> CSSFontFeatureValuesRule.characterVariant -> get attr')

    def get_styleset(self):
        val = self._attr.get('styleset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_rule.py -> CSSFontFeatureValuesRule.styleset -> get attr')
