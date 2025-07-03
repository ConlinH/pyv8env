from .flags import *


@construct_100001
class ElementInternals:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("willValidate", "get_willValidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("validity", "get_validity", None, 0, 1, 0, 0, 0, 0, 1),
        ("validationMessage", "get_validationMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),
        ("states", "get_states", None, 0, 1, 0, 0, 0, 0, 1),
        ("shadowRoot", "get_shadowRoot", None, 0, 1, 0, 0, 0, 0, 1),
        ("role", "get_role", "set_role", 0, 1, 0, 0, 0, 0, 1),
        ("ariaAtomic", "get_ariaAtomic", "set_ariaAtomic", 0, 1, 0, 0, 0, 0, 1),
        ("ariaAutoComplete", "get_ariaAutoComplete", "set_ariaAutoComplete", 0, 1, 0, 0, 0, 0, 1),
        ("ariaBusy", "get_ariaBusy", "set_ariaBusy", 0, 1, 0, 0, 0, 0, 1),
        ("ariaBrailleLabel", "get_ariaBrailleLabel", "set_ariaBrailleLabel", 0, 1, 0, 0, 0, 0, 1),
        ("ariaBrailleRoleDescription", "get_ariaBrailleRoleDescription", "set_ariaBrailleRoleDescription", 0, 1, 0, 0, 0, 0, 1),
        ("ariaChecked", "get_ariaChecked", "set_ariaChecked", 0, 1, 0, 0, 0, 0, 1),
        ("ariaColCount", "get_ariaColCount", "set_ariaColCount", 0, 1, 0, 0, 0, 0, 1),
        ("ariaColIndex", "get_ariaColIndex", "set_ariaColIndex", 0, 1, 0, 0, 0, 0, 1),
        ("ariaColSpan", "get_ariaColSpan", "set_ariaColSpan", 0, 1, 0, 0, 0, 0, 1),
        ("ariaCurrent", "get_ariaCurrent", "set_ariaCurrent", 0, 1, 0, 0, 0, 0, 1),
        ("ariaDescription", "get_ariaDescription", "set_ariaDescription", 0, 1, 0, 0, 0, 0, 1),
        ("ariaDisabled", "get_ariaDisabled", "set_ariaDisabled", 0, 1, 0, 0, 0, 0, 1),
        ("ariaExpanded", "get_ariaExpanded", "set_ariaExpanded", 0, 1, 0, 0, 0, 0, 1),
        ("ariaHasPopup", "get_ariaHasPopup", "set_ariaHasPopup", 0, 1, 0, 0, 0, 0, 1),
        ("ariaHidden", "get_ariaHidden", "set_ariaHidden", 0, 1, 0, 0, 0, 0, 1),
        ("ariaInvalid", "get_ariaInvalid", "set_ariaInvalid", 0, 1, 0, 0, 0, 0, 1),
        ("ariaKeyShortcuts", "get_ariaKeyShortcuts", "set_ariaKeyShortcuts", 0, 1, 0, 0, 0, 0, 1),
        ("ariaLabel", "get_ariaLabel", "set_ariaLabel", 0, 1, 0, 0, 0, 0, 1),
        ("ariaLevel", "get_ariaLevel", "set_ariaLevel", 0, 1, 0, 0, 0, 0, 1),
        ("ariaLive", "get_ariaLive", "set_ariaLive", 0, 1, 0, 0, 0, 0, 1),
        ("ariaModal", "get_ariaModal", "set_ariaModal", 0, 1, 0, 0, 0, 0, 1),
        ("ariaMultiLine", "get_ariaMultiLine", "set_ariaMultiLine", 0, 1, 0, 0, 0, 0, 1),
        ("ariaMultiSelectable", "get_ariaMultiSelectable", "set_ariaMultiSelectable", 0, 1, 0, 0, 0, 0, 1),
        ("ariaOrientation", "get_ariaOrientation", "set_ariaOrientation", 0, 1, 0, 0, 0, 0, 1),
        ("ariaPlaceholder", "get_ariaPlaceholder", "set_ariaPlaceholder", 0, 1, 0, 0, 0, 0, 1),
        ("ariaPosInSet", "get_ariaPosInSet", "set_ariaPosInSet", 0, 1, 0, 0, 0, 0, 1),
        ("ariaPressed", "get_ariaPressed", "set_ariaPressed", 0, 1, 0, 0, 0, 0, 1),
        ("ariaReadOnly", "get_ariaReadOnly", "set_ariaReadOnly", 0, 1, 0, 0, 0, 0, 1),
        ("ariaRelevant", "get_ariaRelevant", "set_ariaRelevant", 0, 1, 0, 0, 0, 0, 1),
        ("ariaRequired", "get_ariaRequired", "set_ariaRequired", 0, 1, 0, 0, 0, 0, 1),
        ("ariaRoleDescription", "get_ariaRoleDescription", "set_ariaRoleDescription", 0, 1, 0, 0, 0, 0, 1),
        ("ariaRowCount", "get_ariaRowCount", "set_ariaRowCount", 0, 1, 0, 0, 0, 0, 1),
        ("ariaRowIndex", "get_ariaRowIndex", "set_ariaRowIndex", 0, 1, 0, 0, 0, 0, 1),
        ("ariaRowSpan", "get_ariaRowSpan", "set_ariaRowSpan", 0, 1, 0, 0, 0, 0, 1),
        ("ariaSelected", "get_ariaSelected", "set_ariaSelected", 0, 1, 0, 0, 0, 0, 1),
        ("ariaSetSize", "get_ariaSetSize", "set_ariaSetSize", 0, 1, 0, 0, 0, 0, 1),
        ("ariaSort", "get_ariaSort", "set_ariaSort", 0, 1, 0, 0, 0, 0, 1),
        ("ariaValueMax", "get_ariaValueMax", "set_ariaValueMax", 0, 1, 0, 0, 0, 0, 1),
        ("ariaValueMin", "get_ariaValueMin", "set_ariaValueMin", 0, 1, 0, 0, 0, 0, 1),
        ("ariaValueNow", "get_ariaValueNow", "set_ariaValueNow", 0, 1, 0, 0, 0, 0, 1),
        ("ariaValueText", "get_ariaValueText", "set_ariaValueText", 0, 1, 0, 0, 0, 0, 1),
        ("ariaVirtualContent", "get_ariaVirtualContent", "set_ariaVirtualContent", 0, 1, 0, 0, 0, 0, 1),
        ("ariaActiveDescendantElement", "get_ariaActiveDescendantElement", "set_ariaActiveDescendantElement", 0, 1, 0, 0, 0, 0, 1),
        ("ariaControlsElements", "get_ariaControlsElements", "set_ariaControlsElements", 0, 1, 0, 0, 0, 0, 1),
        ("ariaDescribedByElements", "get_ariaDescribedByElements", "set_ariaDescribedByElements", 0, 1, 0, 0, 0, 0, 1),
        ("ariaDetailsElements", "get_ariaDetailsElements", "set_ariaDetailsElements", 0, 1, 0, 0, 0, 0, 1),
        ("ariaErrorMessageElements", "get_ariaErrorMessageElements", "set_ariaErrorMessageElements", 0, 1, 0, 0, 0, 0, 1),
        ("ariaFlowToElements", "get_ariaFlowToElements", "set_ariaFlowToElements", 0, 1, 0, 0, 0, 0, 1),
        ("ariaLabelledByElements", "get_ariaLabelledByElements", "set_ariaLabelledByElements", 0, 1, 0, 0, 0, 0, 1),
        ("ariaOwnsElements", "get_ariaOwnsElements", "set_ariaOwnsElements", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("checkValidity", "fn_checkValidity", 0, 0, 1, 0, 0, 0, 0),
        ("reportValidity", "fn_reportValidity", 0, 0, 1, 0, 0, 0, 0),
        ("setFormValue", "fn_setFormValue", 1, 0, 1, 0, 0, 0, 0),
        ("setValidity", "fn_setValidity", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.form -> get attr')

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.validationMessage -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.labels -> get attr')

    def get_states(self):
        val = self._attr.get('states')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.states -> get attr')

    def get_shadowRoot(self):
        val = self._attr.get('shadowRoot')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.shadowRoot -> get attr')

    def get_role(self):
        val = self._attr.get('role')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.role -> get attr')

    def set_role(self, val):
        self._attr['role'] = val

    def get_ariaAtomic(self):
        val = self._attr.get('ariaAtomic')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaAtomic -> get attr')

    def set_ariaAtomic(self, val):
        self._attr['ariaAtomic'] = val

    def get_ariaAutoComplete(self):
        val = self._attr.get('ariaAutoComplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaAutoComplete -> get attr')

    def set_ariaAutoComplete(self, val):
        self._attr['ariaAutoComplete'] = val

    def get_ariaBusy(self):
        val = self._attr.get('ariaBusy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaBusy -> get attr')

    def set_ariaBusy(self, val):
        self._attr['ariaBusy'] = val

    def get_ariaBrailleLabel(self):
        val = self._attr.get('ariaBrailleLabel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaBrailleLabel -> get attr')

    def set_ariaBrailleLabel(self, val):
        self._attr['ariaBrailleLabel'] = val

    def get_ariaBrailleRoleDescription(self):
        val = self._attr.get('ariaBrailleRoleDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaBrailleRoleDescription -> get attr')

    def set_ariaBrailleRoleDescription(self, val):
        self._attr['ariaBrailleRoleDescription'] = val

    def get_ariaChecked(self):
        val = self._attr.get('ariaChecked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaChecked -> get attr')

    def set_ariaChecked(self, val):
        self._attr['ariaChecked'] = val

    def get_ariaColCount(self):
        val = self._attr.get('ariaColCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaColCount -> get attr')

    def set_ariaColCount(self, val):
        self._attr['ariaColCount'] = val

    def get_ariaColIndex(self):
        val = self._attr.get('ariaColIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaColIndex -> get attr')

    def set_ariaColIndex(self, val):
        self._attr['ariaColIndex'] = val

    def get_ariaColSpan(self):
        val = self._attr.get('ariaColSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaColSpan -> get attr')

    def set_ariaColSpan(self, val):
        self._attr['ariaColSpan'] = val

    def get_ariaCurrent(self):
        val = self._attr.get('ariaCurrent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaCurrent -> get attr')

    def set_ariaCurrent(self, val):
        self._attr['ariaCurrent'] = val

    def get_ariaDescription(self):
        val = self._attr.get('ariaDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaDescription -> get attr')

    def set_ariaDescription(self, val):
        self._attr['ariaDescription'] = val

    def get_ariaDisabled(self):
        val = self._attr.get('ariaDisabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaDisabled -> get attr')

    def set_ariaDisabled(self, val):
        self._attr['ariaDisabled'] = val

    def get_ariaExpanded(self):
        val = self._attr.get('ariaExpanded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaExpanded -> get attr')

    def set_ariaExpanded(self, val):
        self._attr['ariaExpanded'] = val

    def get_ariaHasPopup(self):
        val = self._attr.get('ariaHasPopup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaHasPopup -> get attr')

    def set_ariaHasPopup(self, val):
        self._attr['ariaHasPopup'] = val

    def get_ariaHidden(self):
        val = self._attr.get('ariaHidden')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaHidden -> get attr')

    def set_ariaHidden(self, val):
        self._attr['ariaHidden'] = val

    def get_ariaInvalid(self):
        val = self._attr.get('ariaInvalid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaInvalid -> get attr')

    def set_ariaInvalid(self, val):
        self._attr['ariaInvalid'] = val

    def get_ariaKeyShortcuts(self):
        val = self._attr.get('ariaKeyShortcuts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaKeyShortcuts -> get attr')

    def set_ariaKeyShortcuts(self, val):
        self._attr['ariaKeyShortcuts'] = val

    def get_ariaLabel(self):
        val = self._attr.get('ariaLabel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaLabel -> get attr')

    def set_ariaLabel(self, val):
        self._attr['ariaLabel'] = val

    def get_ariaLevel(self):
        val = self._attr.get('ariaLevel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaLevel -> get attr')

    def set_ariaLevel(self, val):
        self._attr['ariaLevel'] = val

    def get_ariaLive(self):
        val = self._attr.get('ariaLive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaLive -> get attr')

    def set_ariaLive(self, val):
        self._attr['ariaLive'] = val

    def get_ariaModal(self):
        val = self._attr.get('ariaModal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaModal -> get attr')

    def set_ariaModal(self, val):
        self._attr['ariaModal'] = val

    def get_ariaMultiLine(self):
        val = self._attr.get('ariaMultiLine')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaMultiLine -> get attr')

    def set_ariaMultiLine(self, val):
        self._attr['ariaMultiLine'] = val

    def get_ariaMultiSelectable(self):
        val = self._attr.get('ariaMultiSelectable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaMultiSelectable -> get attr')

    def set_ariaMultiSelectable(self, val):
        self._attr['ariaMultiSelectable'] = val

    def get_ariaOrientation(self):
        val = self._attr.get('ariaOrientation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaOrientation -> get attr')

    def set_ariaOrientation(self, val):
        self._attr['ariaOrientation'] = val

    def get_ariaPlaceholder(self):
        val = self._attr.get('ariaPlaceholder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaPlaceholder -> get attr')

    def set_ariaPlaceholder(self, val):
        self._attr['ariaPlaceholder'] = val

    def get_ariaPosInSet(self):
        val = self._attr.get('ariaPosInSet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaPosInSet -> get attr')

    def set_ariaPosInSet(self, val):
        self._attr['ariaPosInSet'] = val

    def get_ariaPressed(self):
        val = self._attr.get('ariaPressed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaPressed -> get attr')

    def set_ariaPressed(self, val):
        self._attr['ariaPressed'] = val

    def get_ariaReadOnly(self):
        val = self._attr.get('ariaReadOnly')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaReadOnly -> get attr')

    def set_ariaReadOnly(self, val):
        self._attr['ariaReadOnly'] = val

    def get_ariaRelevant(self):
        val = self._attr.get('ariaRelevant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaRelevant -> get attr')

    def set_ariaRelevant(self, val):
        self._attr['ariaRelevant'] = val

    def get_ariaRequired(self):
        val = self._attr.get('ariaRequired')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaRequired -> get attr')

    def set_ariaRequired(self, val):
        self._attr['ariaRequired'] = val

    def get_ariaRoleDescription(self):
        val = self._attr.get('ariaRoleDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaRoleDescription -> get attr')

    def set_ariaRoleDescription(self, val):
        self._attr['ariaRoleDescription'] = val

    def get_ariaRowCount(self):
        val = self._attr.get('ariaRowCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaRowCount -> get attr')

    def set_ariaRowCount(self, val):
        self._attr['ariaRowCount'] = val

    def get_ariaRowIndex(self):
        val = self._attr.get('ariaRowIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaRowIndex -> get attr')

    def set_ariaRowIndex(self, val):
        self._attr['ariaRowIndex'] = val

    def get_ariaRowSpan(self):
        val = self._attr.get('ariaRowSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaRowSpan -> get attr')

    def set_ariaRowSpan(self, val):
        self._attr['ariaRowSpan'] = val

    def get_ariaSelected(self):
        val = self._attr.get('ariaSelected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaSelected -> get attr')

    def set_ariaSelected(self, val):
        self._attr['ariaSelected'] = val

    def get_ariaSetSize(self):
        val = self._attr.get('ariaSetSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaSetSize -> get attr')

    def set_ariaSetSize(self, val):
        self._attr['ariaSetSize'] = val

    def get_ariaSort(self):
        val = self._attr.get('ariaSort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaSort -> get attr')

    def set_ariaSort(self, val):
        self._attr['ariaSort'] = val

    def get_ariaValueMax(self):
        val = self._attr.get('ariaValueMax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaValueMax -> get attr')

    def set_ariaValueMax(self, val):
        self._attr['ariaValueMax'] = val

    def get_ariaValueMin(self):
        val = self._attr.get('ariaValueMin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaValueMin -> get attr')

    def set_ariaValueMin(self, val):
        self._attr['ariaValueMin'] = val

    def get_ariaValueNow(self):
        val = self._attr.get('ariaValueNow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaValueNow -> get attr')

    def set_ariaValueNow(self, val):
        self._attr['ariaValueNow'] = val

    def get_ariaValueText(self):
        val = self._attr.get('ariaValueText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaValueText -> get attr')

    def set_ariaValueText(self, val):
        self._attr['ariaValueText'] = val

    def get_ariaVirtualContent(self):
        val = self._attr.get('ariaVirtualContent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaVirtualContent -> get attr')

    def set_ariaVirtualContent(self, val):
        self._attr['ariaVirtualContent'] = val

    def get_ariaActiveDescendantElement(self):
        val = self._attr.get('ariaActiveDescendantElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaActiveDescendantElement -> get attr')

    def set_ariaActiveDescendantElement(self, val):
        self._attr['ariaActiveDescendantElement'] = val

    def get_ariaControlsElements(self):
        val = self._attr.get('ariaControlsElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaControlsElements -> get attr')

    def set_ariaControlsElements(self, val):
        self._attr['ariaControlsElements'] = val

    def get_ariaDescribedByElements(self):
        val = self._attr.get('ariaDescribedByElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaDescribedByElements -> get attr')

    def set_ariaDescribedByElements(self, val):
        self._attr['ariaDescribedByElements'] = val

    def get_ariaDetailsElements(self):
        val = self._attr.get('ariaDetailsElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaDetailsElements -> get attr')

    def set_ariaDetailsElements(self, val):
        self._attr['ariaDetailsElements'] = val

    def get_ariaErrorMessageElements(self):
        val = self._attr.get('ariaErrorMessageElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaErrorMessageElements -> get attr')

    def set_ariaErrorMessageElements(self, val):
        self._attr['ariaErrorMessageElements'] = val

    def get_ariaFlowToElements(self):
        val = self._attr.get('ariaFlowToElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaFlowToElements -> get attr')

    def set_ariaFlowToElements(self, val):
        self._attr['ariaFlowToElements'] = val

    def get_ariaLabelledByElements(self):
        val = self._attr.get('ariaLabelledByElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaLabelledByElements -> get attr')

    def set_ariaLabelledByElements(self, val):
        self._attr['ariaLabelledByElements'] = val

    def get_ariaOwnsElements(self):
        val = self._attr.get('ariaOwnsElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.ariaOwnsElements -> get attr')

    def set_ariaOwnsElements(self, val):
        self._attr['ariaOwnsElements'] = val

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.checkValidity{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.reportValidity{tuple(args)} -> method')

    def fn_setFormValue(self, *args):
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.setFormValue{tuple(args)} -> method')

    def fn_setValidity(self, *args):
        logger.debug(f'patch -> v8_element_internals.py -> ElementInternals.setValidity{tuple(args)} -> method')
