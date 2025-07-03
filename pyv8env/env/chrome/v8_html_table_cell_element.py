from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTableCellElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTableCellElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("colSpan", "get_colSpan", "set_colSpan", 0, 1, 0, 0, 0, 0, 1),
        ("rowSpan", "get_rowSpan", "set_rowSpan", 0, 1, 0, 0, 0, 0, 1),
        ("headers", "get_headers", "set_headers", 0, 1, 0, 0, 0, 0, 1),
        ("cellIndex", "get_cellIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("axis", "get_axis", "set_axis", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("ch", "get_ch", "set_ch", 0, 1, 0, 0, 0, 0, 1),
        ("chOff", "get_chOff", "set_chOff", 0, 1, 0, 0, 0, 0, 1),
        ("noWrap", "get_noWrap", "set_noWrap", 0, 1, 0, 0, 0, 0, 1),
        ("vAlign", "get_vAlign", "set_vAlign", 0, 1, 0, 0, 0, 0, 1),
        ("bgColor", "get_bgColor", "set_bgColor", 0, 1, 0, 0, 0, 0, 1),
        ("abbr", "get_abbr", "set_abbr", 0, 1, 0, 0, 0, 0, 1),
        ("scope", "get_scope", "set_scope", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_colSpan(self):
        val = self._attr.get('colSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.colSpan -> get attr')

    def set_colSpan(self, val):
        self._attr['colSpan'] = val

    def get_rowSpan(self):
        val = self._attr.get('rowSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.rowSpan -> get attr')

    def set_rowSpan(self, val):
        self._attr['rowSpan'] = val

    def get_headers(self):
        val = self._attr.get('headers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.headers -> get attr')

    def set_headers(self, val):
        self._attr['headers'] = val

    def get_cellIndex(self):
        val = self._attr.get('cellIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.cellIndex -> get attr')

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_axis(self):
        val = self._attr.get('axis')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.axis -> get attr')

    def set_axis(self, val):
        self._attr['axis'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_ch(self):
        val = self._attr.get('ch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.ch -> get attr')

    def set_ch(self, val):
        self._attr['ch'] = val

    def get_chOff(self):
        val = self._attr.get('chOff')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.chOff -> get attr')

    def set_chOff(self, val):
        self._attr['chOff'] = val

    def get_noWrap(self):
        val = self._attr.get('noWrap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.noWrap -> get attr')

    def set_noWrap(self, val):
        self._attr['noWrap'] = val

    def get_vAlign(self):
        val = self._attr.get('vAlign')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.vAlign -> get attr')

    def set_vAlign(self, val):
        self._attr['vAlign'] = val

    def get_bgColor(self):
        val = self._attr.get('bgColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.bgColor -> get attr')

    def set_bgColor(self, val):
        self._attr['bgColor'] = val

    def get_abbr(self):
        val = self._attr.get('abbr')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.abbr -> get attr')

    def set_abbr(self, val):
        self._attr['abbr'] = val

    def get_scope(self):
        val = self._attr.get('scope')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_cell_element.py -> HTMLTableCellElement.scope -> get attr')

    def set_scope(self, val):
        self._attr['scope'] = val
