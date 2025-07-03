from .flags import *


@construct_100001
class StyleSheet:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),
        ("ownerNode", "get_ownerNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("parentStyleSheet", "get_parentStyleSheet", None, 0, 1, 0, 0, 0, 0, 1),
        ("title", "get_title", None, 0, 1, 0, 0, 0, 0, 1),
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_style_sheet.py -> StyleSheet.type -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_style_sheet.py -> StyleSheet.href -> get attr')

    def get_ownerNode(self):
        val = self._attr.get('ownerNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_style_sheet.py -> StyleSheet.ownerNode -> get attr')

    def get_parentStyleSheet(self):
        val = self._attr.get('parentStyleSheet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_style_sheet.py -> StyleSheet.parentStyleSheet -> get attr')

    def get_title(self):
        val = self._attr.get('title')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_style_sheet.py -> StyleSheet.title -> get attr')

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_style_sheet.py -> StyleSheet.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_style_sheet.py -> StyleSheet.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val
