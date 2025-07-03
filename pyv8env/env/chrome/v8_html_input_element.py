from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLInputElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLInputElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("accept", "get_accept", "set_accept", 0, 1, 0, 0, 0, 0, 1),
        ("alt", "get_alt", "set_alt", 0, 1, 0, 0, 0, 0, 1),
        ("autocomplete", "get_autocomplete", "set_autocomplete", 0, 1, 0, 0, 0, 0, 1),
        ("defaultChecked", "get_defaultChecked", "set_defaultChecked", 0, 1, 0, 0, 0, 0, 1),
        ("checked", "get_checked", "set_checked", 0, 1, 0, 0, 0, 0, 1),
        ("dirName", "get_dirName", "set_dirName", 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("files", "get_files", "set_files", 0, 1, 0, 0, 0, 0, 1),
        ("formAction", "get_formAction", "set_formAction", 0, 1, 0, 0, 0, 0, 1),
        ("formEnctype", "get_formEnctype", "set_formEnctype", 0, 1, 0, 0, 0, 0, 1),
        ("formMethod", "get_formMethod", "set_formMethod", 0, 1, 0, 0, 0, 0, 1),
        ("formNoValidate", "get_formNoValidate", "set_formNoValidate", 0, 1, 0, 0, 0, 0, 1),
        ("formTarget", "get_formTarget", "set_formTarget", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("indeterminate", "get_indeterminate", "set_indeterminate", 0, 1, 0, 0, 0, 0, 1),
        ("list", "get_list", None, 0, 1, 0, 0, 0, 0, 1),
        ("max", "get_max", "set_max", 0, 1, 0, 0, 0, 0, 1),
        ("maxLength", "get_maxLength", "set_maxLength", 0, 1, 0, 0, 0, 0, 1),
        ("min", "get_min", "set_min", 0, 1, 0, 0, 0, 0, 1),
        ("minLength", "get_minLength", "set_minLength", 0, 1, 0, 0, 0, 0, 1),
        ("multiple", "get_multiple", "set_multiple", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("pattern", "get_pattern", "set_pattern", 0, 1, 0, 0, 0, 0, 1),
        ("placeholder", "get_placeholder", "set_placeholder", 0, 1, 0, 0, 0, 0, 1),
        ("readOnly", "get_readOnly", "set_readOnly", 0, 1, 0, 0, 0, 0, 1),
        ("required", "get_required", "set_required", 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", "set_size", 0, 1, 0, 0, 0, 0, 1),
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("step", "get_step", "set_step", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("defaultValue", "get_defaultValue", "set_defaultValue", 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("valueAsDate", "get_valueAsDate", "set_valueAsDate", 0, 1, 0, 0, 0, 0, 1),
        ("valueAsNumber", "get_valueAsNumber", "set_valueAsNumber", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("willValidate", "get_willValidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("validity", "get_validity", None, 0, 1, 0, 0, 0, 0, 1),
        ("validationMessage", "get_validationMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectionStart", "get_selectionStart", "set_selectionStart", 0, 1, 0, 0, 0, 0, 1),
        ("selectionEnd", "get_selectionEnd", "set_selectionEnd", 0, 1, 0, 0, 0, 0, 1),
        ("selectionDirection", "get_selectionDirection", "set_selectionDirection", 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("useMap", "get_useMap", "set_useMap", 0, 1, 0, 0, 0, 0, 1),
        ("webkitdirectory", "get_webkitdirectory", "set_webkitdirectory", 0, 1, 0, 0, 0, 0, 1),
        ("incremental", "get_incremental", "set_incremental", 0, 1, 0, 0, 0, 0, 1),
        ("popoverTargetElement", "get_popoverTargetElement", "set_popoverTargetElement", 0, 1, 0, 0, 0, 0, 1),
        ("popoverTargetAction", "get_popoverTargetAction", "set_popoverTargetAction", 0, 1, 0, 0, 0, 0, 1),
        ("capture", "get_capture", "set_capture", 0, 1, 0, 0, 0, 0, 1),
        ("webkitEntries", "get_webkitEntries", None, 0, 1, 0, 0, 0, 0, 1),
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
        ("select", "fn_select", 0, 0, 1, 0, 0, 0, 0),
        ("setCustomValidity", "fn_setCustomValidity", 1, 0, 1, 0, 0, 0, 0),
        ("setRangeText", "fn_setRangeText", 1, 0, 1, 0, 0, 0, 0),
        ("setSelectionRange", "fn_setSelectionRange", 2, 0, 1, 0, 0, 0, 0),
        ("showPicker", "fn_showPicker", 0, 0, 1, 0, 0, 0, 0),
        ("stepDown", "fn_stepDown", 0, 0, 1, 0, 0, 0, 0),
        ("stepUp", "fn_stepUp", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_accept(self):
        val = self._attr.get('accept')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.accept -> get attr')

    def set_accept(self, val):
        self._attr['accept'] = val

    def get_alt(self):
        val = self._attr.get('alt')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.alt -> get attr')

    def set_alt(self, val):
        self._attr['alt'] = val

    def get_autocomplete(self):
        val = self._attr.get('autocomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.autocomplete -> get attr')

    def set_autocomplete(self, val):
        self._attr['autocomplete'] = val

    def get_defaultChecked(self):
        val = self._attr.get('defaultChecked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.defaultChecked -> get attr')

    def set_defaultChecked(self, val):
        self._attr['defaultChecked'] = val

    def get_checked(self):
        val = self._attr.get('checked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.checked -> get attr')

    def set_checked(self, val):
        self._attr['checked'] = val

    def get_dirName(self):
        val = self._attr.get('dirName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.dirName -> get attr')

    def set_dirName(self, val):
        self._attr['dirName'] = val

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.form -> get attr')

    def get_files(self):
        val = self._attr.get('files')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.files -> get attr')

    def set_files(self, val):
        self._attr['files'] = val

    def get_formAction(self):
        val = self._attr.get('formAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.formAction -> get attr')

    def set_formAction(self, val):
        self._attr['formAction'] = val

    def get_formEnctype(self):
        val = self._attr.get('formEnctype')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.formEnctype -> get attr')

    def set_formEnctype(self, val):
        self._attr['formEnctype'] = val

    def get_formMethod(self):
        val = self._attr.get('formMethod')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.formMethod -> get attr')

    def set_formMethod(self, val):
        self._attr['formMethod'] = val

    def get_formNoValidate(self):
        val = self._attr.get('formNoValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.formNoValidate -> get attr')

    def set_formNoValidate(self, val):
        self._attr['formNoValidate'] = val

    def get_formTarget(self):
        val = self._attr.get('formTarget')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.formTarget -> get attr')

    def set_formTarget(self, val):
        self._attr['formTarget'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_indeterminate(self):
        val = self._attr.get('indeterminate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.indeterminate -> get attr')

    def set_indeterminate(self, val):
        self._attr['indeterminate'] = val

    def get_list(self):
        val = self._attr.get('list')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.list -> get attr')

    def get_max(self):
        val = self._attr.get('max')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.max -> get attr')

    def set_max(self, val):
        self._attr['max'] = val

    def get_maxLength(self):
        val = self._attr.get('maxLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.maxLength -> get attr')

    def set_maxLength(self, val):
        self._attr['maxLength'] = val

    def get_min(self):
        val = self._attr.get('min')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.min -> get attr')

    def set_min(self, val):
        self._attr['min'] = val

    def get_minLength(self):
        val = self._attr.get('minLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.minLength -> get attr')

    def set_minLength(self, val):
        self._attr['minLength'] = val

    def get_multiple(self):
        val = self._attr.get('multiple')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.multiple -> get attr')

    def set_multiple(self, val):
        self._attr['multiple'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_pattern(self):
        val = self._attr.get('pattern')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.pattern -> get attr')

    def set_pattern(self, val):
        self._attr['pattern'] = val

    def get_placeholder(self):
        val = self._attr.get('placeholder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.placeholder -> get attr')

    def set_placeholder(self, val):
        self._attr['placeholder'] = val

    def get_readOnly(self):
        val = self._attr.get('readOnly')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.readOnly -> get attr')

    def set_readOnly(self, val):
        self._attr['readOnly'] = val

    def get_required(self):
        val = self._attr.get('required')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.required -> get attr')

    def set_required(self, val):
        self._attr['required'] = val

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.size -> get attr')

    def set_size(self, val):
        self._attr['size'] = val

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_step(self):
        val = self._attr.get('step')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.step -> get attr')

    def set_step(self, val):
        self._attr['step'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_defaultValue(self):
        val = self._attr.get('defaultValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.defaultValue -> get attr')

    def set_defaultValue(self, val):
        self._attr['defaultValue'] = val

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_valueAsDate(self):
        val = self._attr.get('valueAsDate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.valueAsDate -> get attr')

    def set_valueAsDate(self, val):
        self._attr['valueAsDate'] = val

    def get_valueAsNumber(self):
        val = self._attr.get('valueAsNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.valueAsNumber -> get attr')

    def set_valueAsNumber(self, val):
        self._attr['valueAsNumber'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.validationMessage -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.labels -> get attr')

    def get_selectionStart(self):
        val = self._attr.get('selectionStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.selectionStart -> get attr')

    def set_selectionStart(self, val):
        self._attr['selectionStart'] = val

    def get_selectionEnd(self):
        val = self._attr.get('selectionEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.selectionEnd -> get attr')

    def set_selectionEnd(self, val):
        self._attr['selectionEnd'] = val

    def get_selectionDirection(self):
        val = self._attr.get('selectionDirection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.selectionDirection -> get attr')

    def set_selectionDirection(self, val):
        self._attr['selectionDirection'] = val

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_useMap(self):
        val = self._attr.get('useMap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.useMap -> get attr')

    def set_useMap(self, val):
        self._attr['useMap'] = val

    def get_webkitdirectory(self):
        val = self._attr.get('webkitdirectory')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.webkitdirectory -> get attr')

    def set_webkitdirectory(self, val):
        self._attr['webkitdirectory'] = val

    def get_incremental(self):
        val = self._attr.get('incremental')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.incremental -> get attr')

    def set_incremental(self, val):
        self._attr['incremental'] = val

    def get_popoverTargetElement(self):
        val = self._attr.get('popoverTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.popoverTargetElement -> get attr')

    def set_popoverTargetElement(self, val):
        self._attr['popoverTargetElement'] = val

    def get_popoverTargetAction(self):
        val = self._attr.get('popoverTargetAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.popoverTargetAction -> get attr')

    def set_popoverTargetAction(self, val):
        self._attr['popoverTargetAction'] = val

    def get_capture(self):
        val = self._attr.get('capture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.capture -> get attr')

    def set_capture(self, val):
        self._attr['capture'] = val

    def get_webkitEntries(self):
        val = self._attr.get('webkitEntries')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.webkitEntries -> get attr')

    def get_invokeTargetElement(self):
        val = self._attr.get('invokeTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.invokeTargetElement -> get attr')

    def set_invokeTargetElement(self, val):
        self._attr['invokeTargetElement'] = val

    def get_invokeAction(self):
        val = self._attr.get('invokeAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.invokeAction -> get attr')

    def set_invokeAction(self, val):
        self._attr['invokeAction'] = val

    def get_interestTargetElement(self):
        val = self._attr.get('interestTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.interestTargetElement -> get attr')

    def set_interestTargetElement(self, val):
        self._attr['interestTargetElement'] = val

    def get_interestAction(self):
        val = self._attr.get('interestAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.interestAction -> get attr')

    def set_interestAction(self, val):
        self._attr['interestAction'] = val

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.checkValidity{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.reportValidity{tuple(args)} -> method')

    def fn_select(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.select{tuple(args)} -> method')

    def fn_setCustomValidity(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.setCustomValidity{tuple(args)} -> method')

    def fn_setRangeText(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.setRangeText{tuple(args)} -> method')

    def fn_setSelectionRange(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.setSelectionRange{tuple(args)} -> method')

    def fn_showPicker(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.showPicker{tuple(args)} -> method')

    def fn_stepDown(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.stepDown{tuple(args)} -> method')

    def fn_stepUp(self, *args):
        logger.debug(f'patch -> v8_html_input_element.py -> HTMLInputElement.stepUp{tuple(args)} -> method')
