from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTableElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTableElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("caption", "get_caption", "set_caption", 0, 1, 0, 0, 0, 0, 1),
        ("tHead", "get_tHead", "set_tHead", 0, 1, 0, 0, 0, 0, 1),
        ("tFoot", "get_tFoot", "set_tFoot", 0, 1, 0, 0, 0, 0, 1),
        ("tBodies", "get_tBodies", None, 0, 1, 0, 0, 0, 0, 1),
        ("rows", "get_rows", None, 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("border", "get_border", "set_border", 0, 1, 0, 0, 0, 0, 1),
        ("frame", "get_frame", "set_frame", 0, 1, 0, 0, 0, 0, 1),
        ("rules", "get_rules", "set_rules", 0, 1, 0, 0, 0, 0, 1),
        ("summary", "get_summary", "set_summary", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("bgColor", "get_bgColor", "set_bgColor", 0, 1, 0, 0, 0, 0, 1),
        ("cellPadding", "get_cellPadding", "set_cellPadding", 0, 1, 0, 0, 0, 0, 1),
        ("cellSpacing", "get_cellSpacing", "set_cellSpacing", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createCaption", "fn_createCaption", 0, 0, 1, 0, 0, 0, 0),
        ("createTBody", "fn_createTBody", 0, 0, 1, 0, 0, 0, 0),
        ("createTFoot", "fn_createTFoot", 0, 0, 1, 0, 0, 0, 0),
        ("createTHead", "fn_createTHead", 0, 0, 1, 0, 0, 0, 0),
        ("deleteCaption", "fn_deleteCaption", 0, 0, 1, 0, 0, 0, 0),
        ("deleteRow", "fn_deleteRow", 1, 0, 1, 0, 0, 0, 0),
        ("deleteTFoot", "fn_deleteTFoot", 0, 0, 1, 0, 0, 0, 0),
        ("deleteTHead", "fn_deleteTHead", 0, 0, 1, 0, 0, 0, 0),
        ("insertRow", "fn_insertRow", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_caption(self):
        val = self._attr.get('caption')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.caption -> get attr')

    def set_caption(self, val):
        self._attr['caption'] = val

    def get_tHead(self):
        val = self._attr.get('tHead')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.tHead -> get attr')

    def set_tHead(self, val):
        self._attr['tHead'] = val

    def get_tFoot(self):
        val = self._attr.get('tFoot')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.tFoot -> get attr')

    def set_tFoot(self, val):
        self._attr['tFoot'] = val

    def get_tBodies(self):
        val = self._attr.get('tBodies')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.tBodies -> get attr')

    def get_rows(self):
        val = self._attr.get('rows')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.rows -> get attr')

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_border(self):
        val = self._attr.get('border')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.border -> get attr')

    def set_border(self, val):
        self._attr['border'] = val

    def get_frame(self):
        val = self._attr.get('frame')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.frame -> get attr')

    def set_frame(self, val):
        self._attr['frame'] = val

    def get_rules(self):
        val = self._attr.get('rules')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.rules -> get attr')

    def set_rules(self, val):
        self._attr['rules'] = val

    def get_summary(self):
        val = self._attr.get('summary')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.summary -> get attr')

    def set_summary(self, val):
        self._attr['summary'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_bgColor(self):
        val = self._attr.get('bgColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.bgColor -> get attr')

    def set_bgColor(self, val):
        self._attr['bgColor'] = val

    def get_cellPadding(self):
        val = self._attr.get('cellPadding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.cellPadding -> get attr')

    def set_cellPadding(self, val):
        self._attr['cellPadding'] = val

    def get_cellSpacing(self):
        val = self._attr.get('cellSpacing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.cellSpacing -> get attr')

    def set_cellSpacing(self, val):
        self._attr['cellSpacing'] = val

    def fn_createCaption(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.createCaption{tuple(args)} -> method')

    def fn_createTBody(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.createTBody{tuple(args)} -> method')

    def fn_createTFoot(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.createTFoot{tuple(args)} -> method')

    def fn_createTHead(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.createTHead{tuple(args)} -> method')

    def fn_deleteCaption(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.deleteCaption{tuple(args)} -> method')

    def fn_deleteRow(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.deleteRow{tuple(args)} -> method')

    def fn_deleteTFoot(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.deleteTFoot{tuple(args)} -> method')

    def fn_deleteTHead(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.deleteTHead{tuple(args)} -> method')

    def fn_insertRow(self, *args):
        logger.debug(f'patch -> v8_html_table_element.py -> HTMLTableElement.insertRow{tuple(args)} -> method')
