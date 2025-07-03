from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLDListElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLDListElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("compact", "get_compact", "set_compact", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_compact(self):
        val = self._attr.get('compact')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_dlist_element.py -> HTMLDListElement.compact -> get attr')

    def set_compact(self, val):
        self._attr['compact'] = val
