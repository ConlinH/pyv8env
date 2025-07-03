from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLOListElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLOListElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("reversed", "get_reversed", "set_reversed", 0, 1, 0, 0, 0, 0, 1),
        ("start", "get_start", "set_start", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("compact", "get_compact", "set_compact", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_reversed(self):
        val = self._attr.get('reversed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_olist_element.py -> HTMLOListElement.reversed -> get attr')

    def set_reversed(self, val):
        self._attr['reversed'] = val

    def get_start(self):
        val = self._attr.get('start')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_olist_element.py -> HTMLOListElement.start -> get attr')

    def set_start(self, val):
        self._attr['start'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_olist_element.py -> HTMLOListElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_compact(self):
        val = self._attr.get('compact')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_olist_element.py -> HTMLOListElement.compact -> get attr')

    def set_compact(self, val):
        self._attr['compact'] = val
