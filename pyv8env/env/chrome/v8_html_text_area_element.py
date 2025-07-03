from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTextAreaElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTextAreaElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("autocomplete", "get_autocomplete", "set_autocomplete", 0, 1, 0, 0, 0, 0, 1),
        ("cols", "get_cols", "set_cols", 0, 1, 0, 0, 0, 0, 1),
        ("dirName", "get_dirName", "set_dirName", 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxLength", "get_maxLength", "set_maxLength", 0, 1, 0, 0, 0, 0, 1),
        ("minLength", "get_minLength", "set_minLength", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("placeholder", "get_placeholder", "set_placeholder", 0, 1, 0, 0, 0, 0, 1),
        ("readOnly", "get_readOnly", "set_readOnly", 0, 1, 0, 0, 0, 0, 1),
        ("required", "get_required", "set_required", 0, 1, 0, 0, 0, 0, 1),
        ("rows", "get_rows", "set_rows", 0, 1, 0, 0, 0, 0, 1),
        ("wrap", "get_wrap", "set_wrap", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("defaultValue", "get_defaultValue", "set_defaultValue", 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("textLength", "get_textLength", None, 0, 1, 0, 0, 0, 0, 1),
        ("willValidate", "get_willValidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("validity", "get_validity", None, 0, 1, 0, 0, 0, 0, 1),
        ("validationMessage", "get_validationMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectionStart", "get_selectionStart", "set_selectionStart", 0, 1, 0, 0, 0, 0, 1),
        ("selectionEnd", "get_selectionEnd", "set_selectionEnd", 0, 1, 0, 0, 0, 0, 1),
        ("selectionDirection", "get_selectionDirection", "set_selectionDirection", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("checkValidity", "fn_checkValidity", 0, 0, 1, 0, 0, 0, 0),
        ("reportValidity", "fn_reportValidity", 0, 0, 1, 0, 0, 0, 0),
        ("select", "fn_select", 0, 0, 1, 0, 0, 0, 0),
        ("setCustomValidity", "fn_setCustomValidity", 1, 0, 1, 0, 0, 0, 0),
        ("setRangeText", "fn_setRangeText", 1, 0, 1, 0, 0, 0, 0),
        ("setSelectionRange", "fn_setSelectionRange", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_autocomplete(self):
        val = self._attr.get('autocomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.autocomplete -> get attr')

    def set_autocomplete(self, val):
        self._attr['autocomplete'] = val

    def get_cols(self):
        val = self._attr.get('cols')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.cols -> get attr')

    def set_cols(self, val):
        self._attr['cols'] = val

    def get_dirName(self):
        val = self._attr.get('dirName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.dirName -> get attr')

    def set_dirName(self, val):
        self._attr['dirName'] = val

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.form -> get attr')

    def get_maxLength(self):
        val = self._attr.get('maxLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.maxLength -> get attr')

    def set_maxLength(self, val):
        self._attr['maxLength'] = val

    def get_minLength(self):
        val = self._attr.get('minLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.minLength -> get attr')

    def set_minLength(self, val):
        self._attr['minLength'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_placeholder(self):
        val = self._attr.get('placeholder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.placeholder -> get attr')

    def set_placeholder(self, val):
        self._attr['placeholder'] = val

    def get_readOnly(self):
        val = self._attr.get('readOnly')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.readOnly -> get attr')

    def set_readOnly(self, val):
        self._attr['readOnly'] = val

    def get_required(self):
        val = self._attr.get('required')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.required -> get attr')

    def set_required(self, val):
        self._attr['required'] = val

    def get_rows(self):
        val = self._attr.get('rows')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.rows -> get attr')

    def set_rows(self, val):
        self._attr['rows'] = val

    def get_wrap(self):
        val = self._attr.get('wrap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.wrap -> get attr')

    def set_wrap(self, val):
        self._attr['wrap'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.type -> get attr')

    def get_defaultValue(self):
        val = self._attr.get('defaultValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.defaultValue -> get attr')

    def set_defaultValue(self, val):
        self._attr['defaultValue'] = val

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_textLength(self):
        val = self._attr.get('textLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.textLength -> get attr')

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.validationMessage -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.labels -> get attr')

    def get_selectionStart(self):
        val = self._attr.get('selectionStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.selectionStart -> get attr')

    def set_selectionStart(self, val):
        self._attr['selectionStart'] = val

    def get_selectionEnd(self):
        val = self._attr.get('selectionEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.selectionEnd -> get attr')

    def set_selectionEnd(self, val):
        self._attr['selectionEnd'] = val

    def get_selectionDirection(self):
        val = self._attr.get('selectionDirection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.selectionDirection -> get attr')

    def set_selectionDirection(self, val):
        self._attr['selectionDirection'] = val

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.checkValidity{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.reportValidity{tuple(args)} -> method')

    def fn_select(self, *args):
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.select{tuple(args)} -> method')

    def fn_setCustomValidity(self, *args):
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.setCustomValidity{tuple(args)} -> method')

    def fn_setRangeText(self, *args):
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.setRangeText{tuple(args)} -> method')

    def fn_setSelectionRange(self, *args):
        logger.debug(f'patch -> v8_html_text_area_element.py -> HTMLTextAreaElement.setSelectionRange{tuple(args)} -> method')
