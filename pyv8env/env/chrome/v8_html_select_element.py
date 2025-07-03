from .flags import *
from .v8_html_element import HTMLElement


@construct_110101
class HTMLSelectElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLSelectElement, self).__init__(*args, **kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_html_select_element.py -> HTMLSelectElement.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_html_select_element.py -> HTMLSelectElement.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_html_select_element.py -> HTMLSelectElement.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_html_select_element.py -> HTMLSelectElement.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_html_select_element.py -> HTMLSelectElement.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_html_select_element.py -> HTMLSelectElement.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("autocomplete", "get_autocomplete", "set_autocomplete", 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("multiple", "get_multiple", "set_multiple", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("required", "get_required", "set_required", 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", "set_size", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("options", "get_options", None, 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", "set_length", 0, 1, 0, 0, 0, 0, 1),
        ("selectedOptions", "get_selectedOptions", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectedIndex", "get_selectedIndex", "set_selectedIndex", 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("willValidate", "get_willValidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("validity", "get_validity", None, 0, 1, 0, 0, 0, 0, 1),
        ("validationMessage", "get_validationMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 0, 0, 0),
        ("checkValidity", "fn_checkValidity", 0, 0, 1, 0, 0, 0, 0),
        ("item", "fn_item", 1, 0, 1, 0, 0, 0, 0),
        ("namedItem", "fn_namedItem", 1, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 0, 0, 1, 0, 0, 0, 0),
        ("reportValidity", "fn_reportValidity", 0, 0, 1, 0, 0, 0, 0),
        ("setCustomValidity", "fn_setCustomValidity", 1, 0, 1, 0, 0, 0, 0),
        ("showPicker", "fn_showPicker", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_autocomplete(self):
        val = self._attr.get('autocomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.autocomplete -> get attr')

    def set_autocomplete(self, val):
        self._attr['autocomplete'] = val

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.form -> get attr')

    def get_multiple(self):
        val = self._attr.get('multiple')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.multiple -> get attr')

    def set_multiple(self, val):
        self._attr['multiple'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_required(self):
        val = self._attr.get('required')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.required -> get attr')

    def set_required(self, val):
        self._attr['required'] = val

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.size -> get attr')

    def set_size(self, val):
        self._attr['size'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.type -> get attr')

    def get_options(self):
        val = self._attr.get('options')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.options -> get attr')

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.length -> get attr')

    def set_length(self, val):
        self._attr['length'] = val

    def get_selectedOptions(self):
        val = self._attr.get('selectedOptions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.selectedOptions -> get attr')

    def get_selectedIndex(self):
        val = self._attr.get('selectedIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.selectedIndex -> get attr')

    def set_selectedIndex(self, val):
        self._attr['selectedIndex'] = val

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.validationMessage -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.labels -> get attr')

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.add{tuple(args)} -> method')

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.checkValidity{tuple(args)} -> method')

    def fn_item(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.item{tuple(args)} -> method')

    def fn_namedItem(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.namedItem{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.remove{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.reportValidity{tuple(args)} -> method')

    def fn_setCustomValidity(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.setCustomValidity{tuple(args)} -> method')

    def fn_showPicker(self, *args):
        logger.debug(f'patch -> v8_html_select_element.py -> HTMLSelectElement.showPicker{tuple(args)} -> method')
