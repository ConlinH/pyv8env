from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTitleElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTitleElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("text", "get_text", "set_text", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_title_element.py -> HTMLTitleElement.text -> get attr')

    def set_text(self, val):
        self._attr['text'] = val
