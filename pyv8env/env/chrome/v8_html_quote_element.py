from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLQuoteElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLQuoteElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("cite", "get_cite", "set_cite", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_cite(self):
        val = self._attr.get('cite')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_quote_element.py -> HTMLQuoteElement.cite -> get attr')

    def set_cite(self, val):
        self._attr['cite'] = val
