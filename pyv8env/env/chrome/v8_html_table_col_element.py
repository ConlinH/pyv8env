from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTableColElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTableColElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("span", "get_span", "set_span", 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("ch", "get_ch", "set_ch", 0, 1, 0, 0, 0, 0, 1),
        ("chOff", "get_chOff", "set_chOff", 0, 1, 0, 0, 0, 0, 1),
        ("vAlign", "get_vAlign", "set_vAlign", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_span(self):
        val = self._attr.get('span')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_col_element.py -> HTMLTableColElement.span -> get attr')

    def set_span(self, val):
        self._attr['span'] = val

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_col_element.py -> HTMLTableColElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_ch(self):
        val = self._attr.get('ch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_col_element.py -> HTMLTableColElement.ch -> get attr')

    def set_ch(self, val):
        self._attr['ch'] = val

    def get_chOff(self):
        val = self._attr.get('chOff')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_col_element.py -> HTMLTableColElement.chOff -> get attr')

    def set_chOff(self, val):
        self._attr['chOff'] = val

    def get_vAlign(self):
        val = self._attr.get('vAlign')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_col_element.py -> HTMLTableColElement.vAlign -> get attr')

    def set_vAlign(self, val):
        self._attr['vAlign'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_col_element.py -> HTMLTableColElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val
