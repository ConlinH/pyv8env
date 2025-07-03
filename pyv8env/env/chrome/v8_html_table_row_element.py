from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTableRowElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTableRowElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rowIndex", "get_rowIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("sectionRowIndex", "get_sectionRowIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("cells", "get_cells", None, 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("ch", "get_ch", "set_ch", 0, 1, 0, 0, 0, 0, 1),
        ("chOff", "get_chOff", "set_chOff", 0, 1, 0, 0, 0, 0, 1),
        ("vAlign", "get_vAlign", "set_vAlign", 0, 1, 0, 0, 0, 0, 1),
        ("bgColor", "get_bgColor", "set_bgColor", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("deleteCell", "fn_deleteCell", 1, 0, 1, 0, 0, 0, 0),
        ("insertCell", "fn_insertCell", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_rowIndex(self):
        val = self._attr.get('rowIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.rowIndex -> get attr')

    def get_sectionRowIndex(self):
        val = self._attr.get('sectionRowIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.sectionRowIndex -> get attr')

    def get_cells(self):
        val = self._attr.get('cells')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.cells -> get attr')

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_ch(self):
        val = self._attr.get('ch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.ch -> get attr')

    def set_ch(self, val):
        self._attr['ch'] = val

    def get_chOff(self):
        val = self._attr.get('chOff')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.chOff -> get attr')

    def set_chOff(self, val):
        self._attr['chOff'] = val

    def get_vAlign(self):
        val = self._attr.get('vAlign')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.vAlign -> get attr')

    def set_vAlign(self, val):
        self._attr['vAlign'] = val

    def get_bgColor(self):
        val = self._attr.get('bgColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.bgColor -> get attr')

    def set_bgColor(self, val):
        self._attr['bgColor'] = val

    def fn_deleteCell(self, *args):
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.deleteCell{tuple(args)} -> method')

    def fn_insertCell(self, *args):
        logger.debug(f'patch -> v8_html_table_row_element.py -> HTMLTableRowElement.insertCell{tuple(args)} -> method')
