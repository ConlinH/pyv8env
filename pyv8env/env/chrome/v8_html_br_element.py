from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLBRElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLBRElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("clear", "get_clear", "set_clear", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_clear(self):
        val = self._attr.get('clear')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_br_element.py -> HTMLBRElement.clear -> get attr')

    def set_clear(self, val):
        self._attr['clear'] = val
