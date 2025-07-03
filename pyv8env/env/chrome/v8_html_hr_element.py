from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLHRElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLHRElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("color", "get_color", "set_color", 0, 1, 0, 0, 0, 0, 1),
        ("noShade", "get_noShade", "set_noShade", 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", "set_size", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_hr_element.py -> HTMLHRElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_color(self):
        val = self._attr.get('color')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_hr_element.py -> HTMLHRElement.color -> get attr')

    def set_color(self, val):
        self._attr['color'] = val

    def get_noShade(self):
        val = self._attr.get('noShade')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_hr_element.py -> HTMLHRElement.noShade -> get attr')

    def set_noShade(self, val):
        self._attr['noShade'] = val

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_hr_element.py -> HTMLHRElement.size -> get attr')

    def set_size(self, val):
        self._attr['size'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_hr_element.py -> HTMLHRElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val
