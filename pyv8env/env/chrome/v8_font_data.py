from .flags import *


@construct_100001
class FontData:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("postscriptName", "get_postscriptName", None, 0, 1, 0, 0, 0, 0, 1),
        ("fullName", "get_fullName", None, 0, 1, 0, 0, 0, 0, 1),
        ("family", "get_family", None, 0, 1, 0, 0, 0, 0, 1),
        ("style", "get_style", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("blob", "fn_blob", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_postscriptName(self):
        val = self._attr.get('postscriptName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_data.py -> FontData.postscriptName -> get attr')

    def get_fullName(self):
        val = self._attr.get('fullName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_data.py -> FontData.fullName -> get attr')

    def get_family(self):
        val = self._attr.get('family')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_data.py -> FontData.family -> get attr')

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_data.py -> FontData.style -> get attr')

    def fn_blob(self, *args):
        logger.debug(f'patch -> v8_font_data.py -> FontData.blob{tuple(args)} -> method')
