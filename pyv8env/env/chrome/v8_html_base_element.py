from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLBaseElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLBaseElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("href", "get_href", "set_href", 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", "set_target", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_base_element.py -> HTMLBaseElement.href -> get attr')

    def set_href(self, val):
        self._attr['href'] = val

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_base_element.py -> HTMLBaseElement.target -> get attr')

    def set_target(self, val):
        self._attr['target'] = val
