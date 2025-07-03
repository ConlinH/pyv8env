from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLFontElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLFontElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("color", "get_color", "set_color", 0, 1, 0, 0, 0, 0, 1),
        ("face", "get_face", "set_face", 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", "set_size", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_color(self):
        val = self._attr.get('color')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_font_element.py -> HTMLFontElement.color -> get attr')

    def set_color(self, val):
        self._attr['color'] = val

    def get_face(self):
        val = self._attr.get('face')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_font_element.py -> HTMLFontElement.face -> get attr')

    def set_face(self, val):
        self._attr['face'] = val

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_font_element.py -> HTMLFontElement.size -> get attr')

    def set_size(self, val):
        self._attr['size'] = val
