from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLPreElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLPreElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_pre_element.py -> HTMLPreElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val
