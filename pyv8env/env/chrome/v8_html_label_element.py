from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLLabelElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLLabelElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlFor", "get_htmlFor", "set_htmlFor", 0, 1, 0, 0, 0, 0, 1),
        ("control", "get_control", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_label_element.py -> HTMLLabelElement.form -> get attr')

    def get_htmlFor(self):
        val = self._attr.get('htmlFor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_label_element.py -> HTMLLabelElement.htmlFor -> get attr')

    def set_htmlFor(self, val):
        self._attr['htmlFor'] = val

    def get_control(self):
        val = self._attr.get('control')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_label_element.py -> HTMLLabelElement.control -> get attr')
