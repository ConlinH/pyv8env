from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLSelectListElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLSelectListElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("open", "get_open", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectedOption", "get_selectedOption", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("required", "get_required", "set_required", 0, 1, 0, 0, 0, 0, 1),
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

    def get_open(self):
        val = self._attr.get('open')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.open -> get attr')

    def get_selectedOption(self):
        val = self._attr.get('selectedOption')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.selectedOption -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.form -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.type -> get attr')

    def get_required(self):
        val = self._attr.get('required')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.required -> get attr')

    def set_required(self, val):
        self._attr['required'] = val

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.validationMessage -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.labels -> get attr')

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.checkValidity{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.reportValidity{tuple(args)} -> method')

    def fn_setCustomValidity(self, *args):
        logger.debug(f'patch -> v8_html_select_list_element.py -> HTMLSelectListElement.setCustomValidity{tuple(args)} -> method')
