from .flags import *


@construct_000001
class CSSFontFeatureValuesMap:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("set", "fn_set", 2, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 0, 0, 0),
        ("entries", "fn_entries", 0, 0, 1, 0, 0, 0, 0),
        ("forEach", "fn_forEach", 1, 0, 1, 0, 0, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 0, 0, 0),
        ("has", "fn_has", 1, 0, 1, 0, 0, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 0, 0, 0),
        ("values", "fn_values", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.size -> get attr')

    def fn_set(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.set{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.clear{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.delete{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.entries{tuple(args)} -> method')

    def fn_forEach(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.forEach{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.get{tuple(args)} -> method')

    def fn_has(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.has{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.keys{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_css_font_feature_values_map.py -> CSSFontFeatureValuesMap.values{tuple(args)} -> method')
