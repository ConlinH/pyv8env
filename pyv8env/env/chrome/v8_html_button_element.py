from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLButtonElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLButtonElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("formAction", "get_formAction", "set_formAction", 0, 1, 0, 0, 0, 0, 1),
        ("formEnctype", "get_formEnctype", "set_formEnctype", 0, 1, 0, 0, 0, 0, 1),
        ("formMethod", "get_formMethod", "set_formMethod", 0, 1, 0, 0, 0, 0, 1),
        ("formNoValidate", "get_formNoValidate", "set_formNoValidate", 0, 1, 0, 0, 0, 0, 1),
        ("formTarget", "get_formTarget", "set_formTarget", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("willValidate", "get_willValidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("validity", "get_validity", None, 0, 1, 0, 0, 0, 0, 1),
        ("validationMessage", "get_validationMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),
        ("popoverTargetElement", "get_popoverTargetElement", "set_popoverTargetElement", 0, 1, 0, 0, 0, 0, 1),
        ("popoverTargetAction", "get_popoverTargetAction", "set_popoverTargetAction", 0, 1, 0, 0, 0, 0, 1),
        ("invokeTargetElement", "get_invokeTargetElement", "set_invokeTargetElement", 0, 1, 0, 0, 0, 0, 1),
        ("invokeAction", "get_invokeAction", "set_invokeAction", 0, 1, 0, 0, 0, 0, 1),
        ("interestTargetElement", "get_interestTargetElement", "set_interestTargetElement", 0, 1, 0, 0, 0, 0, 1),
        ("interestAction", "get_interestAction", "set_interestAction", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("checkValidity", "fn_checkValidity", 0, 0, 1, 0, 0, 0, 0),
        ("reportValidity", "fn_reportValidity", 0, 0, 1, 0, 0, 0, 0),
        ("setCustomValidity", "fn_setCustomValidity", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.form -> get attr')

    def get_formAction(self):
        val = self._attr.get('formAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.formAction -> get attr')

    def set_formAction(self, val):
        self._attr['formAction'] = val

    def get_formEnctype(self):
        val = self._attr.get('formEnctype')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.formEnctype -> get attr')

    def set_formEnctype(self, val):
        self._attr['formEnctype'] = val

    def get_formMethod(self):
        val = self._attr.get('formMethod')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.formMethod -> get attr')

    def set_formMethod(self, val):
        self._attr['formMethod'] = val

    def get_formNoValidate(self):
        val = self._attr.get('formNoValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.formNoValidate -> get attr')

    def set_formNoValidate(self, val):
        self._attr['formNoValidate'] = val

    def get_formTarget(self):
        val = self._attr.get('formTarget')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.formTarget -> get attr')

    def set_formTarget(self, val):
        self._attr['formTarget'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.validationMessage -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.labels -> get attr')

    def get_popoverTargetElement(self):
        val = self._attr.get('popoverTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.popoverTargetElement -> get attr')

    def set_popoverTargetElement(self, val):
        self._attr['popoverTargetElement'] = val

    def get_popoverTargetAction(self):
        val = self._attr.get('popoverTargetAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.popoverTargetAction -> get attr')

    def set_popoverTargetAction(self, val):
        self._attr['popoverTargetAction'] = val

    def get_invokeTargetElement(self):
        val = self._attr.get('invokeTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.invokeTargetElement -> get attr')

    def set_invokeTargetElement(self, val):
        self._attr['invokeTargetElement'] = val

    def get_invokeAction(self):
        val = self._attr.get('invokeAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.invokeAction -> get attr')

    def set_invokeAction(self, val):
        self._attr['invokeAction'] = val

    def get_interestTargetElement(self):
        val = self._attr.get('interestTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.interestTargetElement -> get attr')

    def set_interestTargetElement(self, val):
        self._attr['interestTargetElement'] = val

    def get_interestAction(self):
        val = self._attr.get('interestAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.interestAction -> get attr')

    def set_interestAction(self, val):
        self._attr['interestAction'] = val

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.checkValidity{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.reportValidity{tuple(args)} -> method')

    def fn_setCustomValidity(self, *args):
        logger.debug(f'patch -> v8_html_button_element.py -> HTMLButtonElement.setCustomValidity{tuple(args)} -> method')
