from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLOutputElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLOutputElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("htmlFor", "get_htmlFor", "set_htmlFor", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("defaultValue", "get_defaultValue", "set_defaultValue", 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("willValidate", "get_willValidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("validity", "get_validity", None, 0, 1, 0, 0, 0, 0, 1),
        ("validationMessage", "get_validationMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("checkValidity", "fn_checkValidity", 0, 0, 1, 0, 0, 0, 0),
        ("reportValidity", "fn_reportValidity", 0, 0, 1, 0, 0, 0, 0),
        ("setCustomValidity", "fn_setCustomValidity", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_htmlFor(self):
        val = self._attr.get('htmlFor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.htmlFor -> get attr')

    def set_htmlFor(self, val):
        self._attr['htmlFor'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.form -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.type -> get attr')

    def get_defaultValue(self):
        val = self._attr.get('defaultValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.defaultValue -> get attr')

    def set_defaultValue(self, val):
        self._attr['defaultValue'] = val

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.validationMessage -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.labels -> get attr')

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.checkValidity{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.reportValidity{tuple(args)} -> method')

    def fn_setCustomValidity(self, *args):
        logger.debug(f'patch -> v8_html_output_element.py -> HTMLOutputElement.setCustomValidity{tuple(args)} -> method')
