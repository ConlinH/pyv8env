from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGStyleElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGStyleElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),
        ("title", "get_title", "set_title", 0, 1, 0, 0, 0, 0, 1),
        ("sheet", "get_sheet", None, 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_style_element.py -> SVGStyleElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_style_element.py -> SVGStyleElement.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val

    def get_title(self):
        val = self._attr.get('title')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_style_element.py -> SVGStyleElement.title -> get attr')

    def set_title(self, val):
        self._attr['title'] = val

    def get_sheet(self):
        val = self._attr.get('sheet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_style_element.py -> SVGStyleElement.sheet -> get attr')

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_style_element.py -> SVGStyleElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val
