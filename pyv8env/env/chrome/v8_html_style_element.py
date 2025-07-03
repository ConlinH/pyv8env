from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLStyleElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLStyleElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("sheet", "get_sheet", None, 0, 1, 0, 0, 0, 0, 1),
        ("blocking", "get_blocking", "set_blocking", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_style_element.py -> HTMLStyleElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_style_element.py -> HTMLStyleElement.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_style_element.py -> HTMLStyleElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_sheet(self):
        val = self._attr.get('sheet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_style_element.py -> HTMLStyleElement.sheet -> get attr')

    def get_blocking(self):
        val = self._attr.get('blocking')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_style_element.py -> HTMLStyleElement.blocking -> get attr')

    def set_blocking(self, val):
        self._attr['blocking'] = val
