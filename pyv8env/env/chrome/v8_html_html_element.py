from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLHtmlElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLHtmlElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("version", "get_version", "set_version", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_version(self):
        val = self._attr.get('version')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_html_element.py -> HTMLHtmlElement.version -> get attr')

    def set_version(self, val):
        self._attr['version'] = val
