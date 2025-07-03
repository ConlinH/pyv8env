from .flags import *
from .v8_element import Element


@construct_100001
class MathMLElement(Element):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MathMLElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onbeforexrselect", "get_onbeforexrselect", "set_onbeforexrselect", 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforeinput", "get_onbeforeinput", "set_onbeforeinput", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforematch", "get_onbeforematch", "set_onbeforematch", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforetoggle", "get_onbeforetoggle", "set_onbeforetoggle", 0, 1, 0, 0, 0, 0, 1),
        ("onblur", "get_onblur", "set_onblur", 0, 1, 0, 0, 0, 0, 1),
        ("oncancel", "get_oncancel", "set_oncancel", 0, 1, 0, 0, 0, 0, 1),
        ("oncanplay", "get_oncanplay", "set_oncanplay", 0, 1, 0, 0, 0, 0, 1),
        ("oncanplaythrough", "get_oncanplaythrough", "set_oncanplaythrough", 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),
        ("onclick", "get_onclick", "set_onclick", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),
        ("oncontentvisibilityautostatechange", "get_oncontentvisibilityautostatechange", "set_oncontentvisibilityautostatechange", 0, 1, 0, 0, 0, 0, 1),
        ("oncontextlost", "get_oncontextlost", "set_oncontextlost", 0, 1, 0, 0, 0, 0, 1),
        ("oncontextmenu", "get_oncontextmenu", "set_oncontextmenu", 0, 1, 0, 0, 0, 0, 1),
        ("oncontextrestored", "get_oncontextrestored", "set_oncontextrestored", 0, 1, 0, 0, 0, 0, 1),
        ("oncuechange", "get_oncuechange", "set_oncuechange", 0, 1, 0, 0, 0, 0, 1),
        ("ondblclick", "get_ondblclick", "set_ondblclick", 0, 1, 0, 0, 0, 0, 1),
        ("ondrag", "get_ondrag", "set_ondrag", 0, 1, 0, 0, 0, 0, 1),
        ("ondragend", "get_ondragend", "set_ondragend", 0, 1, 0, 0, 0, 0, 1),
        ("ondragenter", "get_ondragenter", "set_ondragenter", 0, 1, 0, 0, 0, 0, 1),
        ("ondragleave", "get_ondragleave", "set_ondragleave", 0, 1, 0, 0, 0, 0, 1),
        ("ondragover", "get_ondragover", "set_ondragover", 0, 1, 0, 0, 0, 0, 1),
        ("ondragstart", "get_ondragstart", "set_ondragstart", 0, 1, 0, 0, 0, 0, 1),
        ("ondrop", "get_ondrop", "set_ondrop", 0, 1, 0, 0, 0, 0, 1),
        ("ondurationchange", "get_ondurationchange", "set_ondurationchange", 0, 1, 0, 0, 0, 0, 1),
        ("onemptied", "get_onemptied", "set_onemptied", 0, 1, 0, 0, 0, 0, 1),
        ("onended", "get_onended", "set_onended", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onfocus", "get_onfocus", "set_onfocus", 0, 1, 0, 0, 0, 0, 1),
        ("onformdata", "get_onformdata", "set_onformdata", 0, 1, 0, 0, 0, 0, 1),
        ("oninput", "get_oninput", "set_oninput", 0, 1, 0, 0, 0, 0, 1),
        ("oninvalid", "get_oninvalid", "set_oninvalid", 0, 1, 0, 0, 0, 0, 1),
        ("onkeydown", "get_onkeydown", "set_onkeydown", 0, 1, 0, 0, 0, 0, 1),
        ("onkeypress", "get_onkeypress", "set_onkeypress", 0, 1, 0, 0, 0, 0, 1),
        ("onkeyup", "get_onkeyup", "set_onkeyup", 0, 1, 0, 0, 0, 0, 1),
        ("onload", "get_onload", "set_onload", 0, 1, 0, 0, 0, 0, 1),
        ("onloadeddata", "get_onloadeddata", "set_onloadeddata", 0, 1, 0, 0, 0, 0, 1),
        ("onloadedmetadata", "get_onloadedmetadata", "set_onloadedmetadata", 0, 1, 0, 0, 0, 0, 1),
        ("onloadstart", "get_onloadstart", "set_onloadstart", 0, 1, 0, 0, 0, 0, 1),
        ("onmousedown", "get_onmousedown", "set_onmousedown", 0, 1, 0, 0, 0, 0, 1),
        ("onmouseenter", "get_onmouseenter", "set_onmouseenter", 0, 1, 0, 1, 0, 0, 1),
        ("onmouseleave", "get_onmouseleave", "set_onmouseleave", 0, 1, 0, 1, 0, 0, 1),
        ("onmousemove", "get_onmousemove", "set_onmousemove", 0, 1, 0, 0, 0, 0, 1),
        ("onmouseout", "get_onmouseout", "set_onmouseout", 0, 1, 0, 0, 0, 0, 1),
        ("onmouseover", "get_onmouseover", "set_onmouseover", 0, 1, 0, 0, 0, 0, 1),
        ("onmouseup", "get_onmouseup", "set_onmouseup", 0, 1, 0, 0, 0, 0, 1),
        ("onmousewheel", "get_onmousewheel", "set_onmousewheel", 0, 1, 0, 0, 0, 0, 1),
        ("onpause", "get_onpause", "set_onpause", 0, 1, 0, 0, 0, 0, 1),
        ("onplay", "get_onplay", "set_onplay", 0, 1, 0, 0, 0, 0, 1),
        ("onplaying", "get_onplaying", "set_onplaying", 0, 1, 0, 0, 0, 0, 1),
        ("onprogress", "get_onprogress", "set_onprogress", 0, 1, 0, 0, 0, 0, 1),
        ("onratechange", "get_onratechange", "set_onratechange", 0, 1, 0, 0, 0, 0, 1),
        ("onreset", "get_onreset", "set_onreset", 0, 1, 0, 0, 0, 0, 1),
        ("onresize", "get_onresize", "set_onresize", 0, 1, 0, 0, 0, 0, 1),
        ("onscroll", "get_onscroll", "set_onscroll", 0, 1, 0, 0, 0, 0, 1),
        ("onsecuritypolicyviolation", "get_onsecuritypolicyviolation", "set_onsecuritypolicyviolation", 0, 1, 0, 0, 0, 0, 1),
        ("onseeked", "get_onseeked", "set_onseeked", 0, 1, 0, 0, 0, 0, 1),
        ("onseeking", "get_onseeking", "set_onseeking", 0, 1, 0, 0, 0, 0, 1),
        ("onselect", "get_onselect", "set_onselect", 0, 1, 0, 0, 0, 0, 1),
        ("onslotchange", "get_onslotchange", "set_onslotchange", 0, 1, 0, 0, 0, 0, 1),
        ("onstalled", "get_onstalled", "set_onstalled", 0, 1, 0, 0, 0, 0, 1),
        ("onsubmit", "get_onsubmit", "set_onsubmit", 0, 1, 0, 0, 0, 0, 1),
        ("onsuspend", "get_onsuspend", "set_onsuspend", 0, 1, 0, 0, 0, 0, 1),
        ("ontimeupdate", "get_ontimeupdate", "set_ontimeupdate", 0, 1, 0, 0, 0, 0, 1),
        ("ontoggle", "get_ontoggle", "set_ontoggle", 0, 1, 0, 0, 0, 0, 1),
        ("onvolumechange", "get_onvolumechange", "set_onvolumechange", 0, 1, 0, 0, 0, 0, 1),
        ("onwaiting", "get_onwaiting", "set_onwaiting", 0, 1, 0, 0, 0, 0, 1),
        ("onwebkitanimationend", "get_onwebkitanimationend", "set_onwebkitanimationend", 0, 1, 0, 0, 0, 0, 1),
        ("onwebkitanimationiteration", "get_onwebkitanimationiteration", "set_onwebkitanimationiteration", 0, 1, 0, 0, 0, 0, 1),
        ("onwebkitanimationstart", "get_onwebkitanimationstart", "set_onwebkitanimationstart", 0, 1, 0, 0, 0, 0, 1),
        ("onwebkittransitionend", "get_onwebkittransitionend", "set_onwebkittransitionend", 0, 1, 0, 0, 0, 0, 1),
        ("onwheel", "get_onwheel", "set_onwheel", 0, 1, 0, 0, 0, 0, 1),
        ("onauxclick", "get_onauxclick", "set_onauxclick", 0, 1, 0, 0, 0, 0, 1),
        ("ongotpointercapture", "get_ongotpointercapture", "set_ongotpointercapture", 0, 1, 0, 0, 0, 0, 1),
        ("onlostpointercapture", "get_onlostpointercapture", "set_onlostpointercapture", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerdown", "get_onpointerdown", "set_onpointerdown", 0, 1, 0, 0, 0, 0, 1),
        ("onpointermove", "get_onpointermove", "set_onpointermove", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerrawupdate", "get_onpointerrawupdate", "set_onpointerrawupdate", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerup", "get_onpointerup", "set_onpointerup", 0, 1, 0, 0, 0, 0, 1),
        ("onpointercancel", "get_onpointercancel", "set_onpointercancel", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerover", "get_onpointerover", "set_onpointerover", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerout", "get_onpointerout", "set_onpointerout", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerenter", "get_onpointerenter", "set_onpointerenter", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerleave", "get_onpointerleave", "set_onpointerleave", 0, 1, 0, 0, 0, 0, 1),
        ("onselectstart", "get_onselectstart", "set_onselectstart", 0, 1, 0, 0, 0, 0, 1),
        ("onselectionchange", "get_onselectionchange", "set_onselectionchange", 0, 1, 0, 0, 0, 0, 1),
        ("onanimationend", "get_onanimationend", "set_onanimationend", 0, 1, 0, 0, 0, 0, 1),
        ("onanimationiteration", "get_onanimationiteration", "set_onanimationiteration", 0, 1, 0, 0, 0, 0, 1),
        ("onanimationstart", "get_onanimationstart", "set_onanimationstart", 0, 1, 0, 0, 0, 0, 1),
        ("ontransitionrun", "get_ontransitionrun", "set_ontransitionrun", 0, 1, 0, 0, 0, 0, 1),
        ("ontransitionstart", "get_ontransitionstart", "set_ontransitionstart", 0, 1, 0, 0, 0, 0, 1),
        ("ontransitionend", "get_ontransitionend", "set_ontransitionend", 0, 1, 0, 0, 0, 0, 1),
        ("ontransitioncancel", "get_ontransitioncancel", "set_ontransitioncancel", 0, 1, 0, 0, 0, 0, 1),
        ("oncopy", "get_oncopy", "set_oncopy", 0, 1, 0, 0, 0, 0, 1),
        ("oncut", "get_oncut", "set_oncut", 0, 1, 0, 0, 0, 0, 1),
        ("onpaste", "get_onpaste", "set_onpaste", 0, 1, 0, 0, 0, 0, 1),
        ("dataset", "get_dataset", None, 0, 1, 0, 0, 0, 0, 1),
        ("nonce", "get_nonce", "set_nonce", 0, 1, 0, 0, 0, 0, 1),
        ("autofocus", "get_autofocus", "set_autofocus", 0, 1, 0, 0, 0, 0, 1),
        ("tabIndex", "get_tabIndex", "set_tabIndex", 0, 1, 0, 0, 0, 0, 1),
        ("style", "get_style", "set_style", 0, 1, 0, 0, 0, 0, 1),
        ("attributeStyleMap", "get_attributeStyleMap", None, 0, 1, 0, 0, 0, 0, 1),
        ("onfencedtreeclick", "get_onfencedtreeclick", "set_onfencedtreeclick", 0, 1, 0, 0, 0, 0, 1),
        ("onoverscroll", "get_onoverscroll", "set_onoverscroll", 0, 1, 0, 0, 0, 0, 1),
        ("onscrollend", "get_onscrollend", "set_onscrollend", 0, 1, 0, 0, 0, 0, 1),
        ("onscrollsnapchange", "get_onscrollsnapchange", "set_onscrollsnapchange", 0, 1, 0, 0, 0, 0, 1),
        ("onscrollsnapchanging", "get_onscrollsnapchanging", "set_onscrollsnapchanging", 0, 1, 0, 0, 0, 0, 1),
        ("ontouchcancel", "get_ontouchcancel", "set_ontouchcancel", 0, 1, 0, 0, 0, 0, 1),
        ("ontouchend", "get_ontouchend", "set_ontouchend", 0, 1, 0, 0, 0, 0, 1),
        ("ontouchmove", "get_ontouchmove", "set_ontouchmove", 0, 1, 0, 0, 0, 0, 1),
        ("ontouchstart", "get_ontouchstart", "set_ontouchstart", 0, 1, 0, 0, 0, 0, 1),
        ("focusgroup", "get_focusgroup", "set_focusgroup", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("blur", "fn_blur", 0, 0, 1, 0, 0, 0, 0),
        ("focus", "fn_focus", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_onbeforexrselect(self):
        val = self._attr.get('onbeforexrselect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onbeforexrselect -> get attr')

    def set_onbeforexrselect(self, val):
        self._attr['onbeforexrselect'] = val

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_onbeforeinput(self):
        val = self._attr.get('onbeforeinput')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onbeforeinput -> get attr')

    def set_onbeforeinput(self, val):
        self._attr['onbeforeinput'] = val

    def get_onbeforematch(self):
        val = self._attr.get('onbeforematch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onbeforematch -> get attr')

    def set_onbeforematch(self, val):
        self._attr['onbeforematch'] = val

    def get_onbeforetoggle(self):
        val = self._attr.get('onbeforetoggle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onbeforetoggle -> get attr')

    def set_onbeforetoggle(self, val):
        self._attr['onbeforetoggle'] = val

    def get_onblur(self):
        val = self._attr.get('onblur')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onblur -> get attr')

    def set_onblur(self, val):
        self._attr['onblur'] = val

    def get_oncancel(self):
        val = self._attr.get('oncancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncancel -> get attr')

    def set_oncancel(self, val):
        self._attr['oncancel'] = val

    def get_oncanplay(self):
        val = self._attr.get('oncanplay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncanplay -> get attr')

    def set_oncanplay(self, val):
        self._attr['oncanplay'] = val

    def get_oncanplaythrough(self):
        val = self._attr.get('oncanplaythrough')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncanplaythrough -> get attr')

    def set_oncanplaythrough(self, val):
        self._attr['oncanplaythrough'] = val

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def get_onclick(self):
        val = self._attr.get('onclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onclick -> get attr')

    def set_onclick(self, val):
        self._attr['onclick'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_oncontentvisibilityautostatechange(self):
        val = self._attr.get('oncontentvisibilityautostatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncontentvisibilityautostatechange -> get attr')

    def set_oncontentvisibilityautostatechange(self, val):
        self._attr['oncontentvisibilityautostatechange'] = val

    def get_oncontextlost(self):
        val = self._attr.get('oncontextlost')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncontextlost -> get attr')

    def set_oncontextlost(self, val):
        self._attr['oncontextlost'] = val

    def get_oncontextmenu(self):
        val = self._attr.get('oncontextmenu')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncontextmenu -> get attr')

    def set_oncontextmenu(self, val):
        self._attr['oncontextmenu'] = val

    def get_oncontextrestored(self):
        val = self._attr.get('oncontextrestored')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncontextrestored -> get attr')

    def set_oncontextrestored(self, val):
        self._attr['oncontextrestored'] = val

    def get_oncuechange(self):
        val = self._attr.get('oncuechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncuechange -> get attr')

    def set_oncuechange(self, val):
        self._attr['oncuechange'] = val

    def get_ondblclick(self):
        val = self._attr.get('ondblclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondblclick -> get attr')

    def set_ondblclick(self, val):
        self._attr['ondblclick'] = val

    def get_ondrag(self):
        val = self._attr.get('ondrag')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondrag -> get attr')

    def set_ondrag(self, val):
        self._attr['ondrag'] = val

    def get_ondragend(self):
        val = self._attr.get('ondragend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondragend -> get attr')

    def set_ondragend(self, val):
        self._attr['ondragend'] = val

    def get_ondragenter(self):
        val = self._attr.get('ondragenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondragenter -> get attr')

    def set_ondragenter(self, val):
        self._attr['ondragenter'] = val

    def get_ondragleave(self):
        val = self._attr.get('ondragleave')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondragleave -> get attr')

    def set_ondragleave(self, val):
        self._attr['ondragleave'] = val

    def get_ondragover(self):
        val = self._attr.get('ondragover')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondragover -> get attr')

    def set_ondragover(self, val):
        self._attr['ondragover'] = val

    def get_ondragstart(self):
        val = self._attr.get('ondragstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondragstart -> get attr')

    def set_ondragstart(self, val):
        self._attr['ondragstart'] = val

    def get_ondrop(self):
        val = self._attr.get('ondrop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondrop -> get attr')

    def set_ondrop(self, val):
        self._attr['ondrop'] = val

    def get_ondurationchange(self):
        val = self._attr.get('ondurationchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ondurationchange -> get attr')

    def set_ondurationchange(self, val):
        self._attr['ondurationchange'] = val

    def get_onemptied(self):
        val = self._attr.get('onemptied')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onemptied -> get attr')

    def set_onemptied(self, val):
        self._attr['onemptied'] = val

    def get_onended(self):
        val = self._attr.get('onended')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onended -> get attr')

    def set_onended(self, val):
        self._attr['onended'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onfocus(self):
        val = self._attr.get('onfocus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onfocus -> get attr')

    def set_onfocus(self, val):
        self._attr['onfocus'] = val

    def get_onformdata(self):
        val = self._attr.get('onformdata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onformdata -> get attr')

    def set_onformdata(self, val):
        self._attr['onformdata'] = val

    def get_oninput(self):
        val = self._attr.get('oninput')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oninput -> get attr')

    def set_oninput(self, val):
        self._attr['oninput'] = val

    def get_oninvalid(self):
        val = self._attr.get('oninvalid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oninvalid -> get attr')

    def set_oninvalid(self, val):
        self._attr['oninvalid'] = val

    def get_onkeydown(self):
        val = self._attr.get('onkeydown')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onkeydown -> get attr')

    def set_onkeydown(self, val):
        self._attr['onkeydown'] = val

    def get_onkeypress(self):
        val = self._attr.get('onkeypress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onkeypress -> get attr')

    def set_onkeypress(self, val):
        self._attr['onkeypress'] = val

    def get_onkeyup(self):
        val = self._attr.get('onkeyup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onkeyup -> get attr')

    def set_onkeyup(self, val):
        self._attr['onkeyup'] = val

    def get_onload(self):
        val = self._attr.get('onload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onload -> get attr')

    def set_onload(self, val):
        self._attr['onload'] = val

    def get_onloadeddata(self):
        val = self._attr.get('onloadeddata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onloadeddata -> get attr')

    def set_onloadeddata(self, val):
        self._attr['onloadeddata'] = val

    def get_onloadedmetadata(self):
        val = self._attr.get('onloadedmetadata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onloadedmetadata -> get attr')

    def set_onloadedmetadata(self, val):
        self._attr['onloadedmetadata'] = val

    def get_onloadstart(self):
        val = self._attr.get('onloadstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onloadstart -> get attr')

    def set_onloadstart(self, val):
        self._attr['onloadstart'] = val

    def get_onmousedown(self):
        val = self._attr.get('onmousedown')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmousedown -> get attr')

    def set_onmousedown(self, val):
        self._attr['onmousedown'] = val

    def get_onmouseenter(self):
        val = self._attr.get('onmouseenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmouseenter -> get attr')

    def set_onmouseenter(self, val):
        self._attr['onmouseenter'] = val

    def get_onmouseleave(self):
        val = self._attr.get('onmouseleave')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmouseleave -> get attr')

    def set_onmouseleave(self, val):
        self._attr['onmouseleave'] = val

    def get_onmousemove(self):
        val = self._attr.get('onmousemove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmousemove -> get attr')

    def set_onmousemove(self, val):
        self._attr['onmousemove'] = val

    def get_onmouseout(self):
        val = self._attr.get('onmouseout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmouseout -> get attr')

    def set_onmouseout(self, val):
        self._attr['onmouseout'] = val

    def get_onmouseover(self):
        val = self._attr.get('onmouseover')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmouseover -> get attr')

    def set_onmouseover(self, val):
        self._attr['onmouseover'] = val

    def get_onmouseup(self):
        val = self._attr.get('onmouseup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmouseup -> get attr')

    def set_onmouseup(self, val):
        self._attr['onmouseup'] = val

    def get_onmousewheel(self):
        val = self._attr.get('onmousewheel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onmousewheel -> get attr')

    def set_onmousewheel(self, val):
        self._attr['onmousewheel'] = val

    def get_onpause(self):
        val = self._attr.get('onpause')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpause -> get attr')

    def set_onpause(self, val):
        self._attr['onpause'] = val

    def get_onplay(self):
        val = self._attr.get('onplay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onplay -> get attr')

    def set_onplay(self, val):
        self._attr['onplay'] = val

    def get_onplaying(self):
        val = self._attr.get('onplaying')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onplaying -> get attr')

    def set_onplaying(self, val):
        self._attr['onplaying'] = val

    def get_onprogress(self):
        val = self._attr.get('onprogress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onprogress -> get attr')

    def set_onprogress(self, val):
        self._attr['onprogress'] = val

    def get_onratechange(self):
        val = self._attr.get('onratechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onratechange -> get attr')

    def set_onratechange(self, val):
        self._attr['onratechange'] = val

    def get_onreset(self):
        val = self._attr.get('onreset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onreset -> get attr')

    def set_onreset(self, val):
        self._attr['onreset'] = val

    def get_onresize(self):
        val = self._attr.get('onresize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onresize -> get attr')

    def set_onresize(self, val):
        self._attr['onresize'] = val

    def get_onscroll(self):
        val = self._attr.get('onscroll')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onscroll -> get attr')

    def set_onscroll(self, val):
        self._attr['onscroll'] = val

    def get_onsecuritypolicyviolation(self):
        val = self._attr.get('onsecuritypolicyviolation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onsecuritypolicyviolation -> get attr')

    def set_onsecuritypolicyviolation(self, val):
        self._attr['onsecuritypolicyviolation'] = val

    def get_onseeked(self):
        val = self._attr.get('onseeked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onseeked -> get attr')

    def set_onseeked(self, val):
        self._attr['onseeked'] = val

    def get_onseeking(self):
        val = self._attr.get('onseeking')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onseeking -> get attr')

    def set_onseeking(self, val):
        self._attr['onseeking'] = val

    def get_onselect(self):
        val = self._attr.get('onselect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onselect -> get attr')

    def set_onselect(self, val):
        self._attr['onselect'] = val

    def get_onslotchange(self):
        val = self._attr.get('onslotchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onslotchange -> get attr')

    def set_onslotchange(self, val):
        self._attr['onslotchange'] = val

    def get_onstalled(self):
        val = self._attr.get('onstalled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onstalled -> get attr')

    def set_onstalled(self, val):
        self._attr['onstalled'] = val

    def get_onsubmit(self):
        val = self._attr.get('onsubmit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onsubmit -> get attr')

    def set_onsubmit(self, val):
        self._attr['onsubmit'] = val

    def get_onsuspend(self):
        val = self._attr.get('onsuspend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onsuspend -> get attr')

    def set_onsuspend(self, val):
        self._attr['onsuspend'] = val

    def get_ontimeupdate(self):
        val = self._attr.get('ontimeupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontimeupdate -> get attr')

    def set_ontimeupdate(self, val):
        self._attr['ontimeupdate'] = val

    def get_ontoggle(self):
        val = self._attr.get('ontoggle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontoggle -> get attr')

    def set_ontoggle(self, val):
        self._attr['ontoggle'] = val

    def get_onvolumechange(self):
        val = self._attr.get('onvolumechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onvolumechange -> get attr')

    def set_onvolumechange(self, val):
        self._attr['onvolumechange'] = val

    def get_onwaiting(self):
        val = self._attr.get('onwaiting')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onwaiting -> get attr')

    def set_onwaiting(self, val):
        self._attr['onwaiting'] = val

    def get_onwebkitanimationend(self):
        val = self._attr.get('onwebkitanimationend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onwebkitanimationend -> get attr')

    def set_onwebkitanimationend(self, val):
        self._attr['onwebkitanimationend'] = val

    def get_onwebkitanimationiteration(self):
        val = self._attr.get('onwebkitanimationiteration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onwebkitanimationiteration -> get attr')

    def set_onwebkitanimationiteration(self, val):
        self._attr['onwebkitanimationiteration'] = val

    def get_onwebkitanimationstart(self):
        val = self._attr.get('onwebkitanimationstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onwebkitanimationstart -> get attr')

    def set_onwebkitanimationstart(self, val):
        self._attr['onwebkitanimationstart'] = val

    def get_onwebkittransitionend(self):
        val = self._attr.get('onwebkittransitionend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onwebkittransitionend -> get attr')

    def set_onwebkittransitionend(self, val):
        self._attr['onwebkittransitionend'] = val

    def get_onwheel(self):
        val = self._attr.get('onwheel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onwheel -> get attr')

    def set_onwheel(self, val):
        self._attr['onwheel'] = val

    def get_onauxclick(self):
        val = self._attr.get('onauxclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onauxclick -> get attr')

    def set_onauxclick(self, val):
        self._attr['onauxclick'] = val

    def get_ongotpointercapture(self):
        val = self._attr.get('ongotpointercapture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ongotpointercapture -> get attr')

    def set_ongotpointercapture(self, val):
        self._attr['ongotpointercapture'] = val

    def get_onlostpointercapture(self):
        val = self._attr.get('onlostpointercapture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onlostpointercapture -> get attr')

    def set_onlostpointercapture(self, val):
        self._attr['onlostpointercapture'] = val

    def get_onpointerdown(self):
        val = self._attr.get('onpointerdown')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointerdown -> get attr')

    def set_onpointerdown(self, val):
        self._attr['onpointerdown'] = val

    def get_onpointermove(self):
        val = self._attr.get('onpointermove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointermove -> get attr')

    def set_onpointermove(self, val):
        self._attr['onpointermove'] = val

    def get_onpointerrawupdate(self):
        val = self._attr.get('onpointerrawupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointerrawupdate -> get attr')

    def set_onpointerrawupdate(self, val):
        self._attr['onpointerrawupdate'] = val

    def get_onpointerup(self):
        val = self._attr.get('onpointerup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointerup -> get attr')

    def set_onpointerup(self, val):
        self._attr['onpointerup'] = val

    def get_onpointercancel(self):
        val = self._attr.get('onpointercancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointercancel -> get attr')

    def set_onpointercancel(self, val):
        self._attr['onpointercancel'] = val

    def get_onpointerover(self):
        val = self._attr.get('onpointerover')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointerover -> get attr')

    def set_onpointerover(self, val):
        self._attr['onpointerover'] = val

    def get_onpointerout(self):
        val = self._attr.get('onpointerout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointerout -> get attr')

    def set_onpointerout(self, val):
        self._attr['onpointerout'] = val

    def get_onpointerenter(self):
        val = self._attr.get('onpointerenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointerenter -> get attr')

    def set_onpointerenter(self, val):
        self._attr['onpointerenter'] = val

    def get_onpointerleave(self):
        val = self._attr.get('onpointerleave')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpointerleave -> get attr')

    def set_onpointerleave(self, val):
        self._attr['onpointerleave'] = val

    def get_onselectstart(self):
        val = self._attr.get('onselectstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onselectstart -> get attr')

    def set_onselectstart(self, val):
        self._attr['onselectstart'] = val

    def get_onselectionchange(self):
        val = self._attr.get('onselectionchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onselectionchange -> get attr')

    def set_onselectionchange(self, val):
        self._attr['onselectionchange'] = val

    def get_onanimationend(self):
        val = self._attr.get('onanimationend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onanimationend -> get attr')

    def set_onanimationend(self, val):
        self._attr['onanimationend'] = val

    def get_onanimationiteration(self):
        val = self._attr.get('onanimationiteration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onanimationiteration -> get attr')

    def set_onanimationiteration(self, val):
        self._attr['onanimationiteration'] = val

    def get_onanimationstart(self):
        val = self._attr.get('onanimationstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onanimationstart -> get attr')

    def set_onanimationstart(self, val):
        self._attr['onanimationstart'] = val

    def get_ontransitionrun(self):
        val = self._attr.get('ontransitionrun')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontransitionrun -> get attr')

    def set_ontransitionrun(self, val):
        self._attr['ontransitionrun'] = val

    def get_ontransitionstart(self):
        val = self._attr.get('ontransitionstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontransitionstart -> get attr')

    def set_ontransitionstart(self, val):
        self._attr['ontransitionstart'] = val

    def get_ontransitionend(self):
        val = self._attr.get('ontransitionend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontransitionend -> get attr')

    def set_ontransitionend(self, val):
        self._attr['ontransitionend'] = val

    def get_ontransitioncancel(self):
        val = self._attr.get('ontransitioncancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontransitioncancel -> get attr')

    def set_ontransitioncancel(self, val):
        self._attr['ontransitioncancel'] = val

    def get_oncopy(self):
        val = self._attr.get('oncopy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncopy -> get attr')

    def set_oncopy(self, val):
        self._attr['oncopy'] = val

    def get_oncut(self):
        val = self._attr.get('oncut')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.oncut -> get attr')

    def set_oncut(self, val):
        self._attr['oncut'] = val

    def get_onpaste(self):
        val = self._attr.get('onpaste')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onpaste -> get attr')

    def set_onpaste(self, val):
        self._attr['onpaste'] = val

    def get_dataset(self):
        val = self._attr.get('dataset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.dataset -> get attr')

    def get_nonce(self):
        val = self._attr.get('nonce')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.nonce -> get attr')

    def set_nonce(self, val):
        self._attr['nonce'] = val

    def get_autofocus(self):
        val = self._attr.get('autofocus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.autofocus -> get attr')

    def set_autofocus(self, val):
        self._attr['autofocus'] = val

    def get_tabIndex(self):
        val = self._attr.get('tabIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.tabIndex -> get attr')

    def set_tabIndex(self, val):
        self._attr['tabIndex'] = val

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.style -> get attr')

    def set_style(self, val):
        self._attr['style'] = val

    def get_attributeStyleMap(self):
        val = self._attr.get('attributeStyleMap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.attributeStyleMap -> get attr')

    def get_onfencedtreeclick(self):
        val = self._attr.get('onfencedtreeclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onfencedtreeclick -> get attr')

    def set_onfencedtreeclick(self, val):
        self._attr['onfencedtreeclick'] = val

    def get_onoverscroll(self):
        val = self._attr.get('onoverscroll')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onoverscroll -> get attr')

    def set_onoverscroll(self, val):
        self._attr['onoverscroll'] = val

    def get_onscrollend(self):
        val = self._attr.get('onscrollend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onscrollend -> get attr')

    def set_onscrollend(self, val):
        self._attr['onscrollend'] = val

    def get_onscrollsnapchange(self):
        val = self._attr.get('onscrollsnapchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onscrollsnapchange -> get attr')

    def set_onscrollsnapchange(self, val):
        self._attr['onscrollsnapchange'] = val

    def get_onscrollsnapchanging(self):
        val = self._attr.get('onscrollsnapchanging')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.onscrollsnapchanging -> get attr')

    def set_onscrollsnapchanging(self, val):
        self._attr['onscrollsnapchanging'] = val

    def get_ontouchcancel(self):
        val = self._attr.get('ontouchcancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontouchcancel -> get attr')

    def set_ontouchcancel(self, val):
        self._attr['ontouchcancel'] = val

    def get_ontouchend(self):
        val = self._attr.get('ontouchend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontouchend -> get attr')

    def set_ontouchend(self, val):
        self._attr['ontouchend'] = val

    def get_ontouchmove(self):
        val = self._attr.get('ontouchmove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontouchmove -> get attr')

    def set_ontouchmove(self, val):
        self._attr['ontouchmove'] = val

    def get_ontouchstart(self):
        val = self._attr.get('ontouchstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.ontouchstart -> get attr')

    def set_ontouchstart(self, val):
        self._attr['ontouchstart'] = val

    def get_focusgroup(self):
        val = self._attr.get('focusgroup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.focusgroup -> get attr')

    def set_focusgroup(self, val):
        self._attr['focusgroup'] = val

    def fn_blur(self, *args):
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.blur{tuple(args)} -> method')

    def fn_focus(self, *args):
        logger.debug(f'patch -> v8_mathml_element.py -> MathMLElement.focus{tuple(args)} -> method')
