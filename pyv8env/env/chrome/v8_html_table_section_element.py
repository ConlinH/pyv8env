from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTableSectionElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTableSectionElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rows", "get_rows", None, 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("ch", "get_ch", "set_ch", 0, 1, 0, 0, 0, 0, 1),
        ("chOff", "get_chOff", "set_chOff", 0, 1, 0, 0, 0, 0, 1),
        ("vAlign", "get_vAlign", "set_vAlign", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("deleteRow", "fn_deleteRow", 1, 0, 1, 0, 0, 0, 0),
        ("insertRow", "fn_insertRow", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_rows(self):
        val = self._attr.get('rows')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_section_element.py -> HTMLTableSectionElement.rows -> get attr')

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_section_element.py -> HTMLTableSectionElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_ch(self):
        val = self._attr.get('ch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_section_element.py -> HTMLTableSectionElement.ch -> get attr')

    def set_ch(self, val):
        self._attr['ch'] = val

    def get_chOff(self):
        val = self._attr.get('chOff')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_section_element.py -> HTMLTableSectionElement.chOff -> get attr')

    def set_chOff(self, val):
        self._attr['chOff'] = val

    def get_vAlign(self):
        val = self._attr.get('vAlign')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_section_element.py -> HTMLTableSectionElement.vAlign -> get attr')

    def set_vAlign(self, val):
        self._attr['vAlign'] = val

    def fn_deleteRow(self, *args):
        logger.debug(f'patch -> v8_html_table_section_element.py -> HTMLTableSectionElement.deleteRow{tuple(args)} -> method')

    def fn_insertRow(self, *args):
        logger.debug(f'patch -> v8_html_table_section_element.py -> HTMLTableSectionElement.insertRow{tuple(args)} -> method')
