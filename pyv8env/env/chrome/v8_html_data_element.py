from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLDataElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLDataElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_data_element.py -> HTMLDataElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val
