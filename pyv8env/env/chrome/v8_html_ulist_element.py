from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLUListElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLUListElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("compact", "get_compact", "set_compact", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_compact(self):
        val = self._attr.get('compact')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_ulist_element.py -> HTMLUListElement.compact -> get attr')

    def set_compact(self, val):
        self._attr['compact'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_ulist_element.py -> HTMLUListElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val
