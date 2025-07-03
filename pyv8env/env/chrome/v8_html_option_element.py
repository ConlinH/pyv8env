from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLOptionElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLOptionElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),
        ("defaultSelected", "get_defaultSelected", "set_defaultSelected", 0, 1, 0, 0, 0, 0, 1),
        ("selected", "get_selected", "set_selected", 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("text", "get_text", "set_text", 0, 1, 0, 0, 0, 0, 1),
        ("index", "get_index", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.form -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def get_defaultSelected(self):
        val = self._attr.get('defaultSelected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.defaultSelected -> get attr')

    def set_defaultSelected(self, val):
        self._attr['defaultSelected'] = val

    def get_selected(self):
        val = self._attr.get('selected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.selected -> get attr')

    def set_selected(self, val):
        self._attr['selected'] = val

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.text -> get attr')

    def set_text(self, val):
        self._attr['text'] = val

    def get_index(self):
        val = self._attr.get('index')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_option_element.py -> HTMLOptionElement.index -> get attr')
