from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLDetailsElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLDetailsElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("open", "get_open", "set_open", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_open(self):
        val = self._attr.get('open')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_details_element.py -> HTMLDetailsElement.open -> get attr')

    def set_open(self, val):
        self._attr['open'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_details_element.py -> HTMLDetailsElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val
