from .flags import *
from .v8_node import Node


@construct_100001
class Element(Node):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Element, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("namespaceURI", "get_namespaceURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("prefix", "get_prefix", None, 0, 1, 0, 0, 0, 0, 1),
        ("localName", "get_localName", None, 0, 1, 0, 0, 0, 0, 1),
        ("tagName", "get_tagName", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", "set_id", 0, 1, 0, 0, 0, 0, 1),
        ("className", "get_className", "set_className", 0, 1, 0, 0, 0, 0, 1),
        ("classList", "get_classList", "set_classList", 0, 1, 0, 0, 0, 0, 1),
        ("slot", "get_slot", "set_slot", 0, 1, 0, 0, 0, 0, 1),
        ("attributes", "get_attributes", None, 0, 1, 0, 0, 0, 0, 1),
        ("shadowRoot", "get_shadowRoot", None, 0, 1, 0, 0, 0, 0, 1),
        ("part", "get_part", "set_part", 0, 1, 0, 0, 0, 0, 1),
        ("assignedSlot", "get_assignedSlot", None, 0, 1, 0, 0, 0, 0, 1),
        ("innerHTML", "get_innerHTML", "set_innerHTML", 0, 1, 0, 0, 0, 0, 1),
        ("outerHTML", "get_outerHTML", "set_outerHTML", 0, 1, 0, 0, 0, 0, 1),
        ("scrollTop", "get_scrollTop", "set_scrollTop", 0, 1, 0, 0, 0, 0, 1),
        ("scrollLeft", "get_scrollLeft", "set_scrollLeft", 0, 1, 0, 0, 0, 0, 1),
        ("scrollWidth", "get_scrollWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollHeight", "get_scrollHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientTop", "get_clientTop", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientLeft", "get_clientLeft", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientWidth", "get_clientWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientHeight", "get_clientHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("onbeforecopy", "get_onbeforecopy", "set_onbeforecopy", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforecut", "get_onbeforecut", "set_onbeforecut", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforepaste", "get_onbeforepaste", "set_onbeforepaste", 0, 1, 0, 0, 0, 0, 1),
        ("onsearch", "get_onsearch", "set_onsearch", 0, 1, 0, 0, 0, 0, 1),
        ("elementTiming", "get_elementTiming", "set_elementTiming", 0, 1, 0, 0, 0, 0, 1),
        ("onfullscreenchange", "get_onfullscreenchange", "set_onfullscreenchange", 0, 1, 0, 0, 0, 0, 1),
        ("onfullscreenerror", "get_onfullscreenerror", "set_onfullscreenerror", 0, 1, 0, 0, 0, 0, 1),
        ("onwebkitfullscreenchange", "get_onwebkitfullscreenchange", "set_onwebkitfullscreenchange", 0, 1, 0, 0, 0, 0, 1),
        ("onwebkitfullscreenerror", "get_onwebkitfullscreenerror", "set_onwebkitfullscreenerror", 0, 1, 0, 0, 0, 0, 1),
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
        ("children", "get_children", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstElementChild", "get_firstElementChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastElementChild", "get_lastElementChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("childElementCount", "get_childElementCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("previousElementSibling", "get_previousElementSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextElementSibling", "get_nextElementSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("anchorElement", "get_anchorElement", "set_anchorElement", 0, 1, 0, 0, 0, 0, 1),
        ("computedRole", "get_computedRole", None, 0, 1, 0, 0, 0, 0, 1),
        ("computedName", "get_computedName", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibleNode", "get_accessibleNode", None, 0, 1, 0, 0, 0, 0, 1),
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
        ("after", "fn_after", 0, 0, 1, 0, 0, 0, 0),
        ("animate", "fn_animate", 1, 0, 1, 0, 0, 0, 0),
        ("append", "fn_append", 0, 0, 1, 0, 0, 0, 0),
        ("attachShadow", "fn_attachShadow", 1, 0, 1, 0, 0, 0, 0),
        ("before", "fn_before", 0, 0, 1, 0, 0, 0, 0),
        ("checkVisibility", "fn_checkVisibility", 0, 0, 1, 0, 0, 0, 0),
        ("closest", "fn_closest", 1, 0, 1, 0, 0, 0, 0),
        ("computedStyleMap", "fn_computedStyleMap", 0, 0, 1, 0, 0, 0, 0),
        ("getAnimations", "fn_getAnimations", 0, 0, 1, 0, 0, 0, 0),
        ("getAttribute", "fn_getAttribute", 1, 0, 1, 0, 0, 0, 1),
        ("getAttributeNS", "fn_getAttributeNS", 2, 0, 1, 0, 0, 0, 1),
        ("getAttributeNames", "fn_getAttributeNames", 0, 0, 1, 0, 0, 0, 1),
        ("getAttributeNode", "fn_getAttributeNode", 1, 0, 1, 0, 0, 0, 0),
        ("getAttributeNodeNS", "fn_getAttributeNodeNS", 2, 0, 1, 0, 0, 0, 0),
        ("getBoundingClientRect", "fn_getBoundingClientRect", 0, 0, 1, 0, 0, 0, 1),
        ("getClientRects", "fn_getClientRects", 0, 0, 1, 0, 0, 0, 0),
        ("getElementsByClassName", "fn_getElementsByClassName", 1, 0, 1, 0, 0, 0, 1),
        ("getElementsByTagName", "fn_getElementsByTagName", 1, 0, 1, 0, 0, 0, 1),
        ("getElementsByTagNameNS", "fn_getElementsByTagNameNS", 2, 0, 1, 0, 0, 0, 1),
        ("getHTML", "fn_getHTML", 0, 0, 1, 0, 0, 0, 1),
        ("hasAttribute", "fn_hasAttribute", 1, 0, 1, 0, 0, 0, 1),
        ("hasAttributeNS", "fn_hasAttributeNS", 2, 0, 1, 0, 0, 0, 1),
        ("hasAttributes", "fn_hasAttributes", 0, 0, 1, 0, 0, 0, 1),
        ("hasPointerCapture", "fn_hasPointerCapture", 1, 0, 1, 0, 0, 0, 0),
        ("insertAdjacentElement", "fn_insertAdjacentElement", 2, 0, 1, 0, 0, 0, 0),
        ("insertAdjacentHTML", "fn_insertAdjacentHTML", 2, 0, 1, 0, 0, 0, 0),
        ("insertAdjacentText", "fn_insertAdjacentText", 2, 0, 1, 0, 0, 0, 0),
        ("matches", "fn_matches", 1, 0, 1, 0, 0, 0, 0),
        ("prepend", "fn_prepend", 0, 0, 1, 0, 0, 0, 0),
        ("querySelector", "fn_querySelector", 1, 0, 1, 0, 0, 0, 1),
        ("querySelectorAll", "fn_querySelectorAll", 1, 0, 1, 0, 0, 0, 1),
        ("releasePointerCapture", "fn_releasePointerCapture", 1, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 0, 0, 1, 0, 0, 0, 0),
        ("removeAttribute", "fn_removeAttribute", 1, 0, 1, 0, 0, 0, 0),
        ("removeAttributeNS", "fn_removeAttributeNS", 2, 0, 1, 0, 0, 0, 0),
        ("removeAttributeNode", "fn_removeAttributeNode", 1, 0, 1, 0, 0, 0, 0),
        ("replaceChildren", "fn_replaceChildren", 0, 0, 1, 0, 0, 0, 0),
        ("replaceWith", "fn_replaceWith", 0, 0, 1, 0, 0, 0, 0),
        ("requestFullscreen", "fn_requestFullscreen", 0, 0, 1, 0, 1, 0, 0),
        ("requestPointerLock", "fn_requestPointerLock", 0, 0, 1, 0, 0, 0, 0),
        ("scroll", "fn_scroll", 0, 0, 1, 0, 0, 0, 0),
        ("scrollBy", "fn_scrollBy", 0, 0, 1, 0, 0, 0, 0),
        ("scrollIntoView", "fn_scrollIntoView", 0, 0, 1, 0, 0, 0, 0),
        ("scrollIntoViewIfNeeded", "fn_scrollIntoViewIfNeeded", 0, 0, 1, 0, 0, 0, 0),
        ("scrollTo", "fn_scrollTo", 0, 0, 1, 0, 0, 0, 0),
        ("setAttribute", "fn_setAttribute", 2, 0, 1, 0, 0, 0, 0),
        ("setAttributeNS", "fn_setAttributeNS", 3, 0, 1, 0, 0, 0, 0),
        ("setAttributeNode", "fn_setAttributeNode", 1, 0, 1, 0, 0, 0, 0),
        ("setAttributeNodeNS", "fn_setAttributeNodeNS", 1, 0, 1, 0, 0, 0, 0),
        ("setPointerCapture", "fn_setPointerCapture", 1, 0, 1, 0, 0, 0, 0),
        ("toggleAttribute", "fn_toggleAttribute", 1, 0, 1, 0, 0, 0, 0),
        ("webkitMatchesSelector", "fn_webkitMatchesSelector", 1, 0, 1, 0, 0, 0, 0),
        ("webkitRequestFullScreen", "fn_webkitRequestFullScreen", 0, 0, 1, 0, 0, 0, 0),
        ("webkitRequestFullscreen", "fn_webkitRequestFullscreen", 0, 0, 1, 0, 0, 0, 0),
        ("ariaNotify", "fn_ariaNotify", 1, 0, 1, 0, 0, 0, 0),
        ("getInnerHTML", "fn_getInnerHTML", 0, 0, 1, 0, 0, 0, 1),
        ("setHTMLUnsafe", "fn_setHTMLUnsafe", 1, 0, 1, 0, 0, 0, 0),
        ("setHTML", "fn_setHTML", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_namespaceURI(self):
        val = self._attr.get('namespaceURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.namespaceURI -> get attr')

    def get_prefix(self):
        val = self._attr.get('prefix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.prefix -> get attr')

    def get_localName(self):
        val = self._attr.get('localName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.localName -> get attr')

    def get_tagName(self):
        val = self._attr.get('tagName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.tagName -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.id -> get attr')

    def set_id(self, val):
        self._attr['id'] = val

    def get_className(self):
        val = self._attr.get('className')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.className -> get attr')

    def set_className(self, val):
        self._attr['className'] = val

    def get_classList(self):
        val = self._attr.get('classList')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.classList -> get attr')

    def set_classList(self, val):
        self._attr['classList'] = val

    def get_slot(self):
        val = self._attr.get('slot')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.slot -> get attr')

    def set_slot(self, val):
        self._attr['slot'] = val

    def get_attributes(self):
        val = self._attr.get('attributes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.attributes -> get attr')

    def get_shadowRoot(self):
        val = self._attr.get('shadowRoot')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.shadowRoot -> get attr')

    def get_part(self):
        val = self._attr.get('part')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.part -> get attr')

    def set_part(self, val):
        self._attr['part'] = val

    def get_assignedSlot(self):
        val = self._attr.get('assignedSlot')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.assignedSlot -> get attr')

    def get_innerHTML(self):
        val = self._attr.get('innerHTML')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.innerHTML -> get attr')

    def set_innerHTML(self, val):
        self._attr['innerHTML'] = val

    def get_outerHTML(self):
        val = self._attr.get('outerHTML')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.outerHTML -> get attr')

    def set_outerHTML(self, val):
        self._attr['outerHTML'] = val

    def get_scrollTop(self):
        val = self._attr.get('scrollTop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.scrollTop -> get attr')

    def set_scrollTop(self, val):
        self._attr['scrollTop'] = val

    def get_scrollLeft(self):
        val = self._attr.get('scrollLeft')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.scrollLeft -> get attr')

    def set_scrollLeft(self, val):
        self._attr['scrollLeft'] = val

    def get_scrollWidth(self):
        val = self._attr.get('scrollWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.scrollWidth -> get attr')

    def get_scrollHeight(self):
        val = self._attr.get('scrollHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.scrollHeight -> get attr')

    def get_clientTop(self):
        val = self._attr.get('clientTop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.clientTop -> get attr')

    def get_clientLeft(self):
        val = self._attr.get('clientLeft')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.clientLeft -> get attr')

    def get_clientWidth(self):
        val = self._attr.get('clientWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.clientWidth -> get attr')

    def get_clientHeight(self):
        val = self._attr.get('clientHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.clientHeight -> get attr')

    def get_onbeforecopy(self):
        val = self._attr.get('onbeforecopy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onbeforecopy -> get attr')

    def set_onbeforecopy(self, val):
        self._attr['onbeforecopy'] = val

    def get_onbeforecut(self):
        val = self._attr.get('onbeforecut')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onbeforecut -> get attr')

    def set_onbeforecut(self, val):
        self._attr['onbeforecut'] = val

    def get_onbeforepaste(self):
        val = self._attr.get('onbeforepaste')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onbeforepaste -> get attr')

    def set_onbeforepaste(self, val):
        self._attr['onbeforepaste'] = val

    def get_onsearch(self):
        val = self._attr.get('onsearch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onsearch -> get attr')

    def set_onsearch(self, val):
        self._attr['onsearch'] = val

    def get_elementTiming(self):
        val = self._attr.get('elementTiming')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.elementTiming -> get attr')

    def set_elementTiming(self, val):
        self._attr['elementTiming'] = val

    def get_onfullscreenchange(self):
        val = self._attr.get('onfullscreenchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onfullscreenchange -> get attr')

    def set_onfullscreenchange(self, val):
        self._attr['onfullscreenchange'] = val

    def get_onfullscreenerror(self):
        val = self._attr.get('onfullscreenerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onfullscreenerror -> get attr')

    def set_onfullscreenerror(self, val):
        self._attr['onfullscreenerror'] = val

    def get_onwebkitfullscreenchange(self):
        val = self._attr.get('onwebkitfullscreenchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onwebkitfullscreenchange -> get attr')

    def set_onwebkitfullscreenchange(self, val):
        self._attr['onwebkitfullscreenchange'] = val

    def get_onwebkitfullscreenerror(self):
        val = self._attr.get('onwebkitfullscreenerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.onwebkitfullscreenerror -> get attr')

    def set_onwebkitfullscreenerror(self, val):
        self._attr['onwebkitfullscreenerror'] = val

    def get_role(self):
        val = self._attr.get('role')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.role -> get attr')

    def set_role(self, val):
        self._attr['role'] = val

    def get_ariaAtomic(self):
        val = self._attr.get('ariaAtomic')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaAtomic -> get attr')

    def set_ariaAtomic(self, val):
        self._attr['ariaAtomic'] = val

    def get_ariaAutoComplete(self):
        val = self._attr.get('ariaAutoComplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaAutoComplete -> get attr')

    def set_ariaAutoComplete(self, val):
        self._attr['ariaAutoComplete'] = val

    def get_ariaBusy(self):
        val = self._attr.get('ariaBusy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaBusy -> get attr')

    def set_ariaBusy(self, val):
        self._attr['ariaBusy'] = val

    def get_ariaBrailleLabel(self):
        val = self._attr.get('ariaBrailleLabel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaBrailleLabel -> get attr')

    def set_ariaBrailleLabel(self, val):
        self._attr['ariaBrailleLabel'] = val

    def get_ariaBrailleRoleDescription(self):
        val = self._attr.get('ariaBrailleRoleDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaBrailleRoleDescription -> get attr')

    def set_ariaBrailleRoleDescription(self, val):
        self._attr['ariaBrailleRoleDescription'] = val

    def get_ariaChecked(self):
        val = self._attr.get('ariaChecked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaChecked -> get attr')

    def set_ariaChecked(self, val):
        self._attr['ariaChecked'] = val

    def get_ariaColCount(self):
        val = self._attr.get('ariaColCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaColCount -> get attr')

    def set_ariaColCount(self, val):
        self._attr['ariaColCount'] = val

    def get_ariaColIndex(self):
        val = self._attr.get('ariaColIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaColIndex -> get attr')

    def set_ariaColIndex(self, val):
        self._attr['ariaColIndex'] = val

    def get_ariaColSpan(self):
        val = self._attr.get('ariaColSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaColSpan -> get attr')

    def set_ariaColSpan(self, val):
        self._attr['ariaColSpan'] = val

    def get_ariaCurrent(self):
        val = self._attr.get('ariaCurrent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaCurrent -> get attr')

    def set_ariaCurrent(self, val):
        self._attr['ariaCurrent'] = val

    def get_ariaDescription(self):
        val = self._attr.get('ariaDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaDescription -> get attr')

    def set_ariaDescription(self, val):
        self._attr['ariaDescription'] = val

    def get_ariaDisabled(self):
        val = self._attr.get('ariaDisabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaDisabled -> get attr')

    def set_ariaDisabled(self, val):
        self._attr['ariaDisabled'] = val

    def get_ariaExpanded(self):
        val = self._attr.get('ariaExpanded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaExpanded -> get attr')

    def set_ariaExpanded(self, val):
        self._attr['ariaExpanded'] = val

    def get_ariaHasPopup(self):
        val = self._attr.get('ariaHasPopup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaHasPopup -> get attr')

    def set_ariaHasPopup(self, val):
        self._attr['ariaHasPopup'] = val

    def get_ariaHidden(self):
        val = self._attr.get('ariaHidden')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaHidden -> get attr')

    def set_ariaHidden(self, val):
        self._attr['ariaHidden'] = val

    def get_ariaInvalid(self):
        val = self._attr.get('ariaInvalid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaInvalid -> get attr')

    def set_ariaInvalid(self, val):
        self._attr['ariaInvalid'] = val

    def get_ariaKeyShortcuts(self):
        val = self._attr.get('ariaKeyShortcuts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaKeyShortcuts -> get attr')

    def set_ariaKeyShortcuts(self, val):
        self._attr['ariaKeyShortcuts'] = val

    def get_ariaLabel(self):
        val = self._attr.get('ariaLabel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaLabel -> get attr')

    def set_ariaLabel(self, val):
        self._attr['ariaLabel'] = val

    def get_ariaLevel(self):
        val = self._attr.get('ariaLevel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaLevel -> get attr')

    def set_ariaLevel(self, val):
        self._attr['ariaLevel'] = val

    def get_ariaLive(self):
        val = self._attr.get('ariaLive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaLive -> get attr')

    def set_ariaLive(self, val):
        self._attr['ariaLive'] = val

    def get_ariaModal(self):
        val = self._attr.get('ariaModal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaModal -> get attr')

    def set_ariaModal(self, val):
        self._attr['ariaModal'] = val

    def get_ariaMultiLine(self):
        val = self._attr.get('ariaMultiLine')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaMultiLine -> get attr')

    def set_ariaMultiLine(self, val):
        self._attr['ariaMultiLine'] = val

    def get_ariaMultiSelectable(self):
        val = self._attr.get('ariaMultiSelectable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaMultiSelectable -> get attr')

    def set_ariaMultiSelectable(self, val):
        self._attr['ariaMultiSelectable'] = val

    def get_ariaOrientation(self):
        val = self._attr.get('ariaOrientation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaOrientation -> get attr')

    def set_ariaOrientation(self, val):
        self._attr['ariaOrientation'] = val

    def get_ariaPlaceholder(self):
        val = self._attr.get('ariaPlaceholder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaPlaceholder -> get attr')

    def set_ariaPlaceholder(self, val):
        self._attr['ariaPlaceholder'] = val

    def get_ariaPosInSet(self):
        val = self._attr.get('ariaPosInSet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaPosInSet -> get attr')

    def set_ariaPosInSet(self, val):
        self._attr['ariaPosInSet'] = val

    def get_ariaPressed(self):
        val = self._attr.get('ariaPressed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaPressed -> get attr')

    def set_ariaPressed(self, val):
        self._attr['ariaPressed'] = val

    def get_ariaReadOnly(self):
        val = self._attr.get('ariaReadOnly')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaReadOnly -> get attr')

    def set_ariaReadOnly(self, val):
        self._attr['ariaReadOnly'] = val

    def get_ariaRelevant(self):
        val = self._attr.get('ariaRelevant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaRelevant -> get attr')

    def set_ariaRelevant(self, val):
        self._attr['ariaRelevant'] = val

    def get_ariaRequired(self):
        val = self._attr.get('ariaRequired')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaRequired -> get attr')

    def set_ariaRequired(self, val):
        self._attr['ariaRequired'] = val

    def get_ariaRoleDescription(self):
        val = self._attr.get('ariaRoleDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaRoleDescription -> get attr')

    def set_ariaRoleDescription(self, val):
        self._attr['ariaRoleDescription'] = val

    def get_ariaRowCount(self):
        val = self._attr.get('ariaRowCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaRowCount -> get attr')

    def set_ariaRowCount(self, val):
        self._attr['ariaRowCount'] = val

    def get_ariaRowIndex(self):
        val = self._attr.get('ariaRowIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaRowIndex -> get attr')

    def set_ariaRowIndex(self, val):
        self._attr['ariaRowIndex'] = val

    def get_ariaRowSpan(self):
        val = self._attr.get('ariaRowSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaRowSpan -> get attr')

    def set_ariaRowSpan(self, val):
        self._attr['ariaRowSpan'] = val

    def get_ariaSelected(self):
        val = self._attr.get('ariaSelected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaSelected -> get attr')

    def set_ariaSelected(self, val):
        self._attr['ariaSelected'] = val

    def get_ariaSetSize(self):
        val = self._attr.get('ariaSetSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaSetSize -> get attr')

    def set_ariaSetSize(self, val):
        self._attr['ariaSetSize'] = val

    def get_ariaSort(self):
        val = self._attr.get('ariaSort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaSort -> get attr')

    def set_ariaSort(self, val):
        self._attr['ariaSort'] = val

    def get_ariaValueMax(self):
        val = self._attr.get('ariaValueMax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaValueMax -> get attr')

    def set_ariaValueMax(self, val):
        self._attr['ariaValueMax'] = val

    def get_ariaValueMin(self):
        val = self._attr.get('ariaValueMin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaValueMin -> get attr')

    def set_ariaValueMin(self, val):
        self._attr['ariaValueMin'] = val

    def get_ariaValueNow(self):
        val = self._attr.get('ariaValueNow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaValueNow -> get attr')

    def set_ariaValueNow(self, val):
        self._attr['ariaValueNow'] = val

    def get_ariaValueText(self):
        val = self._attr.get('ariaValueText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaValueText -> get attr')

    def set_ariaValueText(self, val):
        self._attr['ariaValueText'] = val

    def get_children(self):
        val = self._attr.get('children')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.children -> get attr')

    def get_firstElementChild(self):
        val = self._attr.get('firstElementChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.firstElementChild -> get attr')

    def get_lastElementChild(self):
        val = self._attr.get('lastElementChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.lastElementChild -> get attr')

    def get_childElementCount(self):
        val = self._attr.get('childElementCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.childElementCount -> get attr')

    def get_previousElementSibling(self):
        val = self._attr.get('previousElementSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.previousElementSibling -> get attr')

    def get_nextElementSibling(self):
        val = self._attr.get('nextElementSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.nextElementSibling -> get attr')

    def get_anchorElement(self):
        val = self._attr.get('anchorElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.anchorElement -> get attr')

    def set_anchorElement(self, val):
        self._attr['anchorElement'] = val

    def get_computedRole(self):
        val = self._attr.get('computedRole')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.computedRole -> get attr')

    def get_computedName(self):
        val = self._attr.get('computedName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.computedName -> get attr')

    def get_accessibleNode(self):
        val = self._attr.get('accessibleNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.accessibleNode -> get attr')

    def get_ariaVirtualContent(self):
        val = self._attr.get('ariaVirtualContent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaVirtualContent -> get attr')

    def set_ariaVirtualContent(self, val):
        self._attr['ariaVirtualContent'] = val

    def get_ariaActiveDescendantElement(self):
        val = self._attr.get('ariaActiveDescendantElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaActiveDescendantElement -> get attr')

    def set_ariaActiveDescendantElement(self, val):
        self._attr['ariaActiveDescendantElement'] = val

    def get_ariaControlsElements(self):
        val = self._attr.get('ariaControlsElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaControlsElements -> get attr')

    def set_ariaControlsElements(self, val):
        self._attr['ariaControlsElements'] = val

    def get_ariaDescribedByElements(self):
        val = self._attr.get('ariaDescribedByElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaDescribedByElements -> get attr')

    def set_ariaDescribedByElements(self, val):
        self._attr['ariaDescribedByElements'] = val

    def get_ariaDetailsElements(self):
        val = self._attr.get('ariaDetailsElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaDetailsElements -> get attr')

    def set_ariaDetailsElements(self, val):
        self._attr['ariaDetailsElements'] = val

    def get_ariaErrorMessageElements(self):
        val = self._attr.get('ariaErrorMessageElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaErrorMessageElements -> get attr')

    def set_ariaErrorMessageElements(self, val):
        self._attr['ariaErrorMessageElements'] = val

    def get_ariaFlowToElements(self):
        val = self._attr.get('ariaFlowToElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaFlowToElements -> get attr')

    def set_ariaFlowToElements(self, val):
        self._attr['ariaFlowToElements'] = val

    def get_ariaLabelledByElements(self):
        val = self._attr.get('ariaLabelledByElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaLabelledByElements -> get attr')

    def set_ariaLabelledByElements(self, val):
        self._attr['ariaLabelledByElements'] = val

    def get_ariaOwnsElements(self):
        val = self._attr.get('ariaOwnsElements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_element.py -> Element.ariaOwnsElements -> get attr')

    def set_ariaOwnsElements(self, val):
        self._attr['ariaOwnsElements'] = val

    def fn_after(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.after{tuple(args)} -> method')

    def fn_animate(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.animate{tuple(args)} -> method')

    def fn_append(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.append{tuple(args)} -> method')

    def fn_attachShadow(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.attachShadow{tuple(args)} -> method')

    def fn_before(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.before{tuple(args)} -> method')

    def fn_checkVisibility(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.checkVisibility{tuple(args)} -> method')

    def fn_closest(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.closest{tuple(args)} -> method')

    def fn_computedStyleMap(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.computedStyleMap{tuple(args)} -> method')

    def fn_getAnimations(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getAnimations{tuple(args)} -> method')

    def fn_getAttribute(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getAttribute{tuple(args)} -> method')

    def fn_getAttributeNS(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getAttributeNS{tuple(args)} -> method')

    def fn_getAttributeNames(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getAttributeNames{tuple(args)} -> method')

    def fn_getAttributeNode(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getAttributeNode{tuple(args)} -> method')

    def fn_getAttributeNodeNS(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getAttributeNodeNS{tuple(args)} -> method')

    def fn_getBoundingClientRect(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getBoundingClientRect{tuple(args)} -> method')

    def fn_getClientRects(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getClientRects{tuple(args)} -> method')

    def fn_getElementsByClassName(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getElementsByClassName{tuple(args)} -> method')

    def fn_getElementsByTagName(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getElementsByTagName{tuple(args)} -> method')

    def fn_getElementsByTagNameNS(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getElementsByTagNameNS{tuple(args)} -> method')

    def fn_getHTML(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getHTML{tuple(args)} -> method')

    def fn_hasAttribute(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.hasAttribute{tuple(args)} -> method')

    def fn_hasAttributeNS(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.hasAttributeNS{tuple(args)} -> method')

    def fn_hasAttributes(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.hasAttributes{tuple(args)} -> method')

    def fn_hasPointerCapture(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.hasPointerCapture{tuple(args)} -> method')

    def fn_insertAdjacentElement(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.insertAdjacentElement{tuple(args)} -> method')

    def fn_insertAdjacentHTML(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.insertAdjacentHTML{tuple(args)} -> method')

    def fn_insertAdjacentText(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.insertAdjacentText{tuple(args)} -> method')

    def fn_matches(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.matches{tuple(args)} -> method')

    def fn_prepend(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.prepend{tuple(args)} -> method')

    def fn_querySelector(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.querySelector{tuple(args)} -> method')

    def fn_querySelectorAll(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.querySelectorAll{tuple(args)} -> method')

    def fn_releasePointerCapture(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.releasePointerCapture{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.remove{tuple(args)} -> method')

    def fn_removeAttribute(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.removeAttribute{tuple(args)} -> method')

    def fn_removeAttributeNS(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.removeAttributeNS{tuple(args)} -> method')

    def fn_removeAttributeNode(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.removeAttributeNode{tuple(args)} -> method')

    def fn_replaceChildren(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.replaceChildren{tuple(args)} -> method')

    def fn_replaceWith(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.replaceWith{tuple(args)} -> method')

    def fn_requestFullscreen(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.requestFullscreen{tuple(args)} -> method')

    def fn_requestPointerLock(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.requestPointerLock{tuple(args)} -> method')

    def fn_scroll(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.scroll{tuple(args)} -> method')

    def fn_scrollBy(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.scrollBy{tuple(args)} -> method')

    def fn_scrollIntoView(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.scrollIntoView{tuple(args)} -> method')

    def fn_scrollIntoViewIfNeeded(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.scrollIntoViewIfNeeded{tuple(args)} -> method')

    def fn_scrollTo(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.scrollTo{tuple(args)} -> method')

    def fn_setAttribute(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.setAttribute{tuple(args)} -> method')

    def fn_setAttributeNS(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.setAttributeNS{tuple(args)} -> method')

    def fn_setAttributeNode(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.setAttributeNode{tuple(args)} -> method')

    def fn_setAttributeNodeNS(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.setAttributeNodeNS{tuple(args)} -> method')

    def fn_setPointerCapture(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.setPointerCapture{tuple(args)} -> method')

    def fn_toggleAttribute(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.toggleAttribute{tuple(args)} -> method')

    def fn_webkitMatchesSelector(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.webkitMatchesSelector{tuple(args)} -> method')

    def fn_webkitRequestFullScreen(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.webkitRequestFullScreen{tuple(args)} -> method')

    def fn_webkitRequestFullscreen(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.webkitRequestFullscreen{tuple(args)} -> method')

    def fn_ariaNotify(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.ariaNotify{tuple(args)} -> method')

    def fn_getInnerHTML(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.getInnerHTML{tuple(args)} -> method')

    def fn_setHTMLUnsafe(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.setHTMLUnsafe{tuple(args)} -> method')

    def fn_setHTML(self, *args):
        logger.debug(f'patch -> v8_element.py -> Element.setHTML{tuple(args)} -> method')
