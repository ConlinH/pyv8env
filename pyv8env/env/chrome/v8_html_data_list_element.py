from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLDataListElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLDataListElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("options", "get_options", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_options(self):
        val = self._attr.get('options')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_data_list_element.py -> HTMLDataListElement.options -> get attr')
