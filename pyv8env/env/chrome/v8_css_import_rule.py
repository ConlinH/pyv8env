from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSImportRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSImportRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),
        ("styleSheet", "get_styleSheet", None, 0, 1, 0, 0, 0, 0, 1),
        ("layerName", "get_layerName", None, 0, 1, 0, 0, 0, 0, 1),
        ("supportsText", "get_supportsText", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_import_rule.py -> CSSImportRule.href -> get attr')

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_import_rule.py -> CSSImportRule.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val

    def get_styleSheet(self):
        val = self._attr.get('styleSheet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_import_rule.py -> CSSImportRule.styleSheet -> get attr')

    def get_layerName(self):
        val = self._attr.get('layerName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_import_rule.py -> CSSImportRule.layerName -> get attr')

    def get_supportsText(self):
        val = self._attr.get('supportsText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_import_rule.py -> CSSImportRule.supportsText -> get attr')
