from .flags import *
from .v8_node import Node


@construct_110001
class Document(Node):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Document, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("implementation", "get_implementation", None, 0, 1, 0, 0, 0, 0, 1),
        ("URL", "get_URL", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentURI", "get_documentURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("compatMode", "get_compatMode", None, 0, 1, 0, 0, 0, 0, 1),
        ("characterSet", "get_characterSet", None, 0, 1, 0, 0, 0, 0, 1),
        ("charset", "get_charset", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputEncoding", "get_inputEncoding", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentType", "get_contentType", None, 0, 1, 0, 0, 0, 0, 1),
        ("doctype", "get_doctype", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentElement", "get_documentElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("xmlEncoding", "get_xmlEncoding", None, 0, 1, 0, 0, 0, 0, 1),
        ("xmlVersion", "get_xmlVersion", "set_xmlVersion", 0, 1, 0, 0, 0, 0, 1),
        ("xmlStandalone", "get_xmlStandalone", "set_xmlStandalone", 0, 1, 0, 0, 0, 0, 1),
        ("location", "get_location", "set_location", 0, 0, 4, 0, 0, 0, 1),
        ("domain", "get_domain", "set_domain", 0, 1, 0, 0, 0, 0, 1),
        ("referrer", "get_referrer", None, 0, 1, 0, 0, 0, 0, 1),
        ("cookie", "get_cookie", "set_cookie", 0, 1, 0, 0, 0, 0, 1),
        ("lastModified", "get_lastModified", None, 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("title", "get_title", "set_title", 0, 1, 0, 0, 0, 0, 1),
        ("dir", "get_dir", "set_dir", 0, 1, 0, 0, 0, 0, 1),
        ("body", "get_body", "set_body", 0, 1, 0, 0, 0, 0, 1),
        ("head", "get_head", None, 0, 1, 0, 0, 0, 0, 1),
        ("images", "get_images", None, 0, 1, 0, 0, 0, 0, 1),
        ("embeds", "get_embeds", None, 0, 1, 0, 0, 0, 0, 1),
        ("plugins", "get_plugins", None, 0, 1, 0, 0, 0, 0, 1),
        ("links", "get_links", None, 0, 1, 0, 0, 0, 0, 1),
        ("forms", "get_forms", None, 0, 1, 0, 0, 0, 0, 1),
        ("scripts", "get_scripts", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentScript", "get_currentScript", None, 0, 1, 0, 0, 0, 0, 1),
        ("defaultView", "get_defaultView", None, 0, 1, 0, 0, 0, 0, 1),
        ("designMode", "get_designMode", "set_designMode", 0, 1, 0, 0, 0, 0, 1),
        ("onreadystatechange", "get_onreadystatechange", "set_onreadystatechange", 0, 1, 0, 1, 0, 0, 1),
        ("anchors", "get_anchors", None, 0, 1, 0, 0, 0, 0, 1),
        ("applets", "get_applets", None, 0, 1, 0, 0, 0, 0, 1),
        ("fgColor", "get_fgColor", "set_fgColor", 0, 1, 0, 0, 0, 0, 1),
        ("linkColor", "get_linkColor", "set_linkColor", 0, 1, 0, 0, 0, 0, 1),
        ("vlinkColor", "get_vlinkColor", "set_vlinkColor", 0, 1, 0, 0, 0, 0, 1),
        ("alinkColor", "get_alinkColor", "set_alinkColor", 0, 1, 0, 0, 0, 0, 1),
        ("bgColor", "get_bgColor", "set_bgColor", 0, 1, 0, 0, 0, 0, 1),
        ("all", "get_all", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollingElement", "get_scrollingElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("onpointerlockchange", "get_onpointerlockchange", "set_onpointerlockchange", 0, 1, 0, 0, 0, 0, 1),
        ("onpointerlockerror", "get_onpointerlockerror", "set_onpointerlockerror", 0, 1, 0, 0, 0, 0, 1),
        ("hidden", "get_hidden", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibilityState", "get_visibilityState", None, 0, 1, 0, 0, 0, 0, 1),
        ("wasDiscarded", "get_wasDiscarded", None, 0, 1, 0, 0, 0, 0, 1),
        ("prerendering", "get_prerendering", None, 0, 1, 0, 0, 0, 0, 1),
        ("featurePolicy", "get_featurePolicy", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitVisibilityState", "get_webkitVisibilityState", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitHidden", "get_webkitHidden", None, 0, 1, 0, 0, 0, 0, 1),
        ("onbeforecopy", "get_onbeforecopy", "set_onbeforecopy", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforecut", "get_onbeforecut", "set_onbeforecut", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforepaste", "get_onbeforepaste", "set_onbeforepaste", 0, 1, 0, 0, 0, 0, 1),
        ("onfreeze", "get_onfreeze", "set_onfreeze", 0, 1, 0, 0, 0, 0, 1),
        ("onprerenderingchange", "get_onprerenderingchange", "set_onprerenderingchange", 0, 1, 0, 0, 0, 0, 1),
        ("onresume", "get_onresume", "set_onresume", 0, 1, 0, 0, 0, 0, 1),
        ("onsearch", "get_onsearch", "set_onsearch", 0, 1, 0, 0, 0, 0, 1),
        ("onvisibilitychange", "get_onvisibilitychange", "set_onvisibilitychange", 0, 1, 0, 0, 0, 0, 1),
        ("timeline", "get_timeline", None, 0, 1, 0, 0, 0, 0, 1),
        ("fullscreenEnabled", "get_fullscreenEnabled", "set_fullscreenEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("fullscreen", "get_fullscreen", "set_fullscreen", 0, 1, 0, 0, 0, 0, 1),
        ("onfullscreenchange", "get_onfullscreenchange", "set_onfullscreenchange", 0, 1, 0, 0, 0, 0, 1),
        ("onfullscreenerror", "get_onfullscreenerror", "set_onfullscreenerror", 0, 1, 0, 0, 0, 0, 1),
        ("webkitIsFullScreen", "get_webkitIsFullScreen", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitCurrentFullScreenElement", "get_webkitCurrentFullScreenElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitFullscreenEnabled", "get_webkitFullscreenEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitFullscreenElement", "get_webkitFullscreenElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("onwebkitfullscreenchange", "get_onwebkitfullscreenchange", "set_onwebkitfullscreenchange", 0, 1, 0, 0, 0, 0, 1),
        ("onwebkitfullscreenerror", "get_onwebkitfullscreenerror", "set_onwebkitfullscreenerror", 0, 1, 0, 0, 0, 0, 1),
        ("rootElement", "get_rootElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("pictureInPictureEnabled", "get_pictureInPictureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
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
        ("children", "get_children", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstElementChild", "get_firstElementChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastElementChild", "get_lastElementChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("childElementCount", "get_childElementCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("activeElement", "get_activeElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("styleSheets", "get_styleSheets", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointerLockElement", "get_pointerLockElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("fullscreenElement", "get_fullscreenElement", "set_fullscreenElement", 0, 1, 0, 0, 0, 0, 1),
        ("adoptedStyleSheets", "get_adoptedStyleSheets", "set_adoptedStyleSheets", 0, 1, 0, 0, 0, 0, 1),
        ("pictureInPictureElement", "get_pictureInPictureElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("fonts", "get_fonts", None, 0, 1, 0, 0, 0, 0, 1),
        ("onfencedtreeclick", "get_onfencedtreeclick", "set_onfencedtreeclick", 0, 1, 0, 0, 0, 0, 1),
        ("onoverscroll", "get_onoverscroll", "set_onoverscroll", 0, 1, 0, 0, 0, 0, 1),
        ("onscrollend", "get_onscrollend", "set_onscrollend", 0, 1, 0, 0, 0, 0, 1),
        ("onscrollsnapchange", "get_onscrollsnapchange", "set_onscrollsnapchange", 0, 1, 0, 0, 0, 0, 1),
        ("onscrollsnapchanging", "get_onscrollsnapchanging", "set_onscrollsnapchanging", 0, 1, 0, 0, 0, 0, 1),
        # ("softNavigations", "get_softNavigations", None, 0, 1, 0, 0, 0, 0, 1),
        ("fragmentDirective", "get_fragmentDirective", None, 0, 1, 0, 0, 0, 0, 1),
        # ("ontouchcancel", "get_ontouchcancel", "set_ontouchcancel", 0, 1, 0, 0, 0, 0, 1),
        # ("ontouchend", "get_ontouchend", "set_ontouchend", 0, 1, 0, 0, 0, 0, 1),
        # ("ontouchmove", "get_ontouchmove", "set_ontouchmove", 0, 1, 0, 0, 0, 0, 1),
        # ("ontouchstart", "get_ontouchstart", "set_ontouchstart", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("adoptNode", "fn_adoptNode", 1, 0, 1, 0, 0, 0, 0),
        ("append", "fn_append", 0, 0, 1, 0, 0, 0, 0),
        ("captureEvents", "fn_captureEvents", 0, 0, 1, 0, 0, 0, 0),
        ("caretRangeFromPoint", "fn_caretRangeFromPoint", 0, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("createAttribute", "fn_createAttribute", 1, 0, 1, 0, 0, 0, 0),
        ("createAttributeNS", "fn_createAttributeNS", 2, 0, 1, 0, 0, 0, 0),
        ("createCDATASection", "fn_createCDATASection", 1, 0, 1, 0, 0, 0, 0),
        ("createComment", "fn_createComment", 1, 0, 1, 0, 0, 0, 0),
        ("createDocumentFragment", "fn_createDocumentFragment", 0, 0, 1, 0, 0, 0, 0),
        ("createElement", "fn_createElement", 1, 0, 1, 0, 0, 0, 0),
        ("createElementNS", "fn_createElementNS", 2, 0, 1, 0, 0, 0, 0),
        ("createEvent", "fn_createEvent", 1, 0, 1, 0, 0, 0, 0),
        ("createExpression", "fn_createExpression", 1, 0, 1, 0, 0, 0, 0),
        ("createNSResolver", "fn_createNSResolver", 1, 0, 1, 0, 0, 0, 0),
        ("createNodeIterator", "fn_createNodeIterator", 1, 0, 1, 0, 0, 0, 0),
        ("createProcessingInstruction", "fn_createProcessingInstruction", 2, 0, 1, 0, 0, 0, 0),
        ("createRange", "fn_createRange", 0, 0, 1, 0, 0, 0, 0),
        ("createTextNode", "fn_createTextNode", 1, 0, 1, 0, 0, 0, 0),
        ("createTreeWalker", "fn_createTreeWalker", 1, 0, 1, 0, 0, 0, 0),
        ("elementFromPoint", "fn_elementFromPoint", 2, 0, 1, 0, 0, 0, 0),
        ("elementsFromPoint", "fn_elementsFromPoint", 2, 0, 1, 0, 0, 0, 0),
        ("evaluate", "fn_evaluate", 2, 0, 1, 0, 0, 0, 0),
        ("execCommand", "fn_execCommand", 1, 0, 1, 0, 0, 0, 0),
        ("exitFullscreen", "fn_exitFullscreen", 0, 0, 1, 0, 1, 0, 0),
        ("exitPictureInPicture", "fn_exitPictureInPicture", 0, 0, 1, 0, 1, 0, 0),
        ("exitPointerLock", "fn_exitPointerLock", 0, 0, 1, 0, 0, 0, 0),
        ("getAnimations", "fn_getAnimations", 0, 0, 1, 0, 0, 0, 0),
        ("getElementById", "fn_getElementById", 1, 0, 1, 0, 0, 0, 0),
        ("getElementsByClassName", "fn_getElementsByClassName", 1, 0, 1, 0, 0, 0, 1),
        ("getElementsByName", "fn_getElementsByName", 1, 0, 1, 0, 0, 0, 1),
        ("getElementsByTagName", "fn_getElementsByTagName", 1, 0, 1, 0, 0, 0, 1),
        ("getElementsByTagNameNS", "fn_getElementsByTagNameNS", 2, 0, 1, 0, 0, 0, 1),
        ("getSelection", "fn_getSelection", 0, 0, 1, 0, 0, 0, 1),
        ("hasFocus", "fn_hasFocus", 0, 0, 1, 0, 0, 0, 1),
        ("hasStorageAccess", "fn_hasStorageAccess", 0, 0, 1, 0, 1, 0, 0),
        ("hasUnpartitionedCookieAccess", "fn_hasUnpartitionedCookieAccess", 0, 0, 1, 0, 1, 0, 0),
        ("importNode", "fn_importNode", 1, 0, 1, 0, 0, 0, 0),
        ("open", "fn_open", 0, 0, 1, 0, 0, 0, 0),
        ("prepend", "fn_prepend", 0, 0, 1, 0, 0, 0, 0),
        ("queryCommandEnabled", "fn_queryCommandEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("queryCommandIndeterm", "fn_queryCommandIndeterm", 1, 0, 1, 0, 0, 0, 0),
        ("queryCommandState", "fn_queryCommandState", 1, 0, 1, 0, 0, 0, 0),
        ("queryCommandSupported", "fn_queryCommandSupported", 1, 0, 1, 0, 0, 0, 0),
        ("queryCommandValue", "fn_queryCommandValue", 1, 0, 1, 0, 0, 0, 0),
        ("querySelector", "fn_querySelector", 1, 0, 1, 0, 0, 0, 1),
        ("querySelectorAll", "fn_querySelectorAll", 1, 0, 1, 0, 0, 0, 1),
        ("releaseEvents", "fn_releaseEvents", 0, 0, 1, 0, 0, 0, 0),
        ("replaceChildren", "fn_replaceChildren", 0, 0, 1, 0, 0, 0, 0),
        ("requestStorageAccess", "fn_requestStorageAccess", 0, 0, 1, 0, 1, 0, 0),
        ("requestStorageAccessFor", "fn_requestStorageAccessFor", 1, 0, 1, 0, 1, 0, 0),
        ("startViewTransition", "fn_startViewTransition", 0, 0, 1, 0, 0, 0, 0),
        ("webkitCancelFullScreen", "fn_webkitCancelFullScreen", 0, 0, 1, 0, 0, 0, 0),
        ("webkitExitFullscreen", "fn_webkitExitFullscreen", 0, 0, 1, 0, 0, 0, 0),
        ("write", "fn_write", 0, 0, 1, 0, 0, 0, 0),
        ("writeln", "fn_writeln", 0, 0, 1, 0, 0, 0, 0),
        ("ariaNotify", "fn_ariaNotify", 1, 0, 1, 0, 0, 0, 0),
        ("caretPositionFromPoint", "fn_caretPositionFromPoint", 2, 0, 1, 0, 0, 0, 0),
        ("getPartRoot", "fn_getPartRoot", 0, 0, 1, 0, 0, 0, 0),
        ("setSequentialFocusStartingPoint", "fn_setSequentialFocusStartingPoint", 1, 0, 1, 0, 0, 0, 0),
        ("parseHTMLUnsafe", "fn_parseHTMLUnsafe", 1, 0, 2, 0, 1, 1, 0),
        ("browsingTopics", "fn_browsingTopics", 0, 0, 1, 0, 1, 0, 0),
        ("hasPrivateToken", "fn_hasPrivateToken", 1, 0, 1, 0, 1, 0, 0),
        ("hasRedemptionRecord", "fn_hasRedemptionRecord", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_implementation(self):
        val = self._attr.get('implementation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.implementation -> get attr')

    def get_URL(self):
        val = self._attr.get('URL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.URL -> get attr')

    def get_documentURI(self):
        val = self._attr.get('documentURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.documentURI -> get attr')

    def get_compatMode(self):
        val = self._attr.get('compatMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.compatMode -> get attr')

    def get_characterSet(self):
        val = self._attr.get('characterSet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.characterSet -> get attr')

    def get_charset(self):
        val = self._attr.get('charset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.charset -> get attr')

    def get_inputEncoding(self):
        val = self._attr.get('inputEncoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.inputEncoding -> get attr')

    def get_contentType(self):
        val = self._attr.get('contentType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.contentType -> get attr')

    def get_doctype(self):
        val = self._attr.get('doctype')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.doctype -> get attr')

    def get_documentElement(self):
        val = self._attr.get('documentElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.documentElement -> get attr')

    def get_xmlEncoding(self):
        val = self._attr.get('xmlEncoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.xmlEncoding -> get attr')

    def get_xmlVersion(self):
        val = self._attr.get('xmlVersion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.xmlVersion -> get attr')

    def set_xmlVersion(self, val):
        self._attr['xmlVersion'] = val

    def get_xmlStandalone(self):
        val = self._attr.get('xmlStandalone')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.xmlStandalone -> get attr')

    def set_xmlStandalone(self, val):
        self._attr['xmlStandalone'] = val

    def get_location(self):
        val = self._attr.get('location')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.location -> get attr')

    def set_location(self, val):
        self._attr['location'] = val

    def get_domain(self):
        val = self._attr.get('domain')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.domain -> get attr')

    def set_domain(self, val):
        self._attr['domain'] = val

    def get_referrer(self):
        val = self._attr.get('referrer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.referrer -> get attr')

    def get_cookie(self):
        val = self._attr.get('cookie')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.cookie -> get attr')

    def set_cookie(self, val):
        self._attr['cookie'] = val

    def get_lastModified(self):
        val = self._attr.get('lastModified')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.lastModified -> get attr')

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.readyState -> get attr')

    def get_title(self):
        val = self._attr.get('title')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.title -> get attr')

    def set_title(self, val):
        self._attr['title'] = val

    def get_dir(self):
        val = self._attr.get('dir')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.dir -> get attr')

    def set_dir(self, val):
        self._attr['dir'] = val

    def get_body(self):
        val = self._attr.get('body')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.body -> get attr')

    def set_body(self, val):
        self._attr['body'] = val

    def get_head(self):
        val = self._attr.get('head')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.head -> get attr')

    def get_images(self):
        val = self._attr.get('images')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.images -> get attr')

    def get_embeds(self):
        val = self._attr.get('embeds')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.embeds -> get attr')

    def get_plugins(self):
        val = self._attr.get('plugins')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.plugins -> get attr')

    def get_links(self):
        val = self._attr.get('links')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.links -> get attr')

    def get_forms(self):
        val = self._attr.get('forms')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.forms -> get attr')

    def get_scripts(self):
        val = self._attr.get('scripts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.scripts -> get attr')

    def get_currentScript(self):
        val = self._attr.get('currentScript')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.currentScript -> get attr')

    def get_defaultView(self):
        val = self._attr.get('defaultView')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.defaultView -> get attr')

    def get_designMode(self):
        val = self._attr.get('designMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.designMode -> get attr')

    def set_designMode(self, val):
        self._attr['designMode'] = val

    def get_onreadystatechange(self):
        val = self._attr.get('onreadystatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onreadystatechange -> get attr')

    def set_onreadystatechange(self, val):
        self._attr['onreadystatechange'] = val

    def get_anchors(self):
        val = self._attr.get('anchors')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.anchors -> get attr')

    def get_applets(self):
        val = self._attr.get('applets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.applets -> get attr')

    def get_fgColor(self):
        val = self._attr.get('fgColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.fgColor -> get attr')

    def set_fgColor(self, val):
        self._attr['fgColor'] = val

    def get_linkColor(self):
        val = self._attr.get('linkColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.linkColor -> get attr')

    def set_linkColor(self, val):
        self._attr['linkColor'] = val

    def get_vlinkColor(self):
        val = self._attr.get('vlinkColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.vlinkColor -> get attr')

    def set_vlinkColor(self, val):
        self._attr['vlinkColor'] = val

    def get_alinkColor(self):
        val = self._attr.get('alinkColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.alinkColor -> get attr')

    def set_alinkColor(self, val):
        self._attr['alinkColor'] = val

    def get_bgColor(self):
        val = self._attr.get('bgColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.bgColor -> get attr')

    def set_bgColor(self, val):
        self._attr['bgColor'] = val

    def get_all(self):
        val = self._attr.get('all')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.all -> get attr')

    def get_scrollingElement(self):
        val = self._attr.get('scrollingElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.scrollingElement -> get attr')

    def get_onpointerlockchange(self):
        val = self._attr.get('onpointerlockchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerlockchange -> get attr')

    def set_onpointerlockchange(self, val):
        self._attr['onpointerlockchange'] = val

    def get_onpointerlockerror(self):
        val = self._attr.get('onpointerlockerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerlockerror -> get attr')

    def set_onpointerlockerror(self, val):
        self._attr['onpointerlockerror'] = val

    def get_hidden(self):
        val = self._attr.get('hidden')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.hidden -> get attr')

    def get_visibilityState(self):
        val = self._attr.get('visibilityState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.visibilityState -> get attr')

    def get_wasDiscarded(self):
        val = self._attr.get('wasDiscarded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.wasDiscarded -> get attr')

    def get_prerendering(self):
        val = self._attr.get('prerendering')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.prerendering -> get attr')

    def get_featurePolicy(self):
        val = self._attr.get('featurePolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.featurePolicy -> get attr')

    def get_webkitVisibilityState(self):
        val = self._attr.get('webkitVisibilityState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.webkitVisibilityState -> get attr')

    def get_webkitHidden(self):
        val = self._attr.get('webkitHidden')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.webkitHidden -> get attr')

    def get_onbeforecopy(self):
        val = self._attr.get('onbeforecopy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onbeforecopy -> get attr')

    def set_onbeforecopy(self, val):
        self._attr['onbeforecopy'] = val

    def get_onbeforecut(self):
        val = self._attr.get('onbeforecut')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onbeforecut -> get attr')

    def set_onbeforecut(self, val):
        self._attr['onbeforecut'] = val

    def get_onbeforepaste(self):
        val = self._attr.get('onbeforepaste')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onbeforepaste -> get attr')

    def set_onbeforepaste(self, val):
        self._attr['onbeforepaste'] = val

    def get_onfreeze(self):
        val = self._attr.get('onfreeze')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onfreeze -> get attr')

    def set_onfreeze(self, val):
        self._attr['onfreeze'] = val

    def get_onprerenderingchange(self):
        val = self._attr.get('onprerenderingchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onprerenderingchange -> get attr')

    def set_onprerenderingchange(self, val):
        self._attr['onprerenderingchange'] = val

    def get_onresume(self):
        val = self._attr.get('onresume')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onresume -> get attr')

    def set_onresume(self, val):
        self._attr['onresume'] = val

    def get_onsearch(self):
        val = self._attr.get('onsearch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onsearch -> get attr')

    def set_onsearch(self, val):
        self._attr['onsearch'] = val

    def get_onvisibilitychange(self):
        val = self._attr.get('onvisibilitychange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onvisibilitychange -> get attr')

    def set_onvisibilitychange(self, val):
        self._attr['onvisibilitychange'] = val

    def get_timeline(self):
        val = self._attr.get('timeline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.timeline -> get attr')

    def get_fullscreenEnabled(self):
        val = self._attr.get('fullscreenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.fullscreenEnabled -> get attr')

    def set_fullscreenEnabled(self, val):
        self._attr['fullscreenEnabled'] = val

    def get_fullscreen(self):
        val = self._attr.get('fullscreen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.fullscreen -> get attr')

    def set_fullscreen(self, val):
        self._attr['fullscreen'] = val

    def get_onfullscreenchange(self):
        val = self._attr.get('onfullscreenchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onfullscreenchange -> get attr')

    def set_onfullscreenchange(self, val):
        self._attr['onfullscreenchange'] = val

    def get_onfullscreenerror(self):
        val = self._attr.get('onfullscreenerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onfullscreenerror -> get attr')

    def set_onfullscreenerror(self, val):
        self._attr['onfullscreenerror'] = val

    def get_webkitIsFullScreen(self):
        val = self._attr.get('webkitIsFullScreen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.webkitIsFullScreen -> get attr')

    def get_webkitCurrentFullScreenElement(self):
        val = self._attr.get('webkitCurrentFullScreenElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.webkitCurrentFullScreenElement -> get attr')

    def get_webkitFullscreenEnabled(self):
        val = self._attr.get('webkitFullscreenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.webkitFullscreenEnabled -> get attr')

    def get_webkitFullscreenElement(self):
        val = self._attr.get('webkitFullscreenElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.webkitFullscreenElement -> get attr')

    def get_onwebkitfullscreenchange(self):
        val = self._attr.get('onwebkitfullscreenchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwebkitfullscreenchange -> get attr')

    def set_onwebkitfullscreenchange(self, val):
        self._attr['onwebkitfullscreenchange'] = val

    def get_onwebkitfullscreenerror(self):
        val = self._attr.get('onwebkitfullscreenerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwebkitfullscreenerror -> get attr')

    def set_onwebkitfullscreenerror(self, val):
        self._attr['onwebkitfullscreenerror'] = val

    def get_rootElement(self):
        val = self._attr.get('rootElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.rootElement -> get attr')

    def get_pictureInPictureEnabled(self):
        val = self._attr.get('pictureInPictureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.pictureInPictureEnabled -> get attr')

    def get_onbeforexrselect(self):
        val = self._attr.get('onbeforexrselect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onbeforexrselect -> get attr')

    def set_onbeforexrselect(self, val):
        self._attr['onbeforexrselect'] = val

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_onbeforeinput(self):
        val = self._attr.get('onbeforeinput')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onbeforeinput -> get attr')

    def set_onbeforeinput(self, val):
        self._attr['onbeforeinput'] = val

    def get_onbeforematch(self):
        val = self._attr.get('onbeforematch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onbeforematch -> get attr')

    def set_onbeforematch(self, val):
        self._attr['onbeforematch'] = val

    def get_onbeforetoggle(self):
        val = self._attr.get('onbeforetoggle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onbeforetoggle -> get attr')

    def set_onbeforetoggle(self, val):
        self._attr['onbeforetoggle'] = val

    def get_onblur(self):
        val = self._attr.get('onblur')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onblur -> get attr')

    def set_onblur(self, val):
        self._attr['onblur'] = val

    def get_oncancel(self):
        val = self._attr.get('oncancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncancel -> get attr')

    def set_oncancel(self, val):
        self._attr['oncancel'] = val

    def get_oncanplay(self):
        val = self._attr.get('oncanplay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncanplay -> get attr')

    def set_oncanplay(self, val):
        self._attr['oncanplay'] = val

    def get_oncanplaythrough(self):
        val = self._attr.get('oncanplaythrough')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncanplaythrough -> get attr')

    def set_oncanplaythrough(self, val):
        self._attr['oncanplaythrough'] = val

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def get_onclick(self):
        val = self._attr.get('onclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onclick -> get attr')

    def set_onclick(self, val):
        self._attr['onclick'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_oncontentvisibilityautostatechange(self):
        val = self._attr.get('oncontentvisibilityautostatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncontentvisibilityautostatechange -> get attr')

    def set_oncontentvisibilityautostatechange(self, val):
        self._attr['oncontentvisibilityautostatechange'] = val

    def get_oncontextlost(self):
        val = self._attr.get('oncontextlost')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncontextlost -> get attr')

    def set_oncontextlost(self, val):
        self._attr['oncontextlost'] = val

    def get_oncontextmenu(self):
        val = self._attr.get('oncontextmenu')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncontextmenu -> get attr')

    def set_oncontextmenu(self, val):
        self._attr['oncontextmenu'] = val

    def get_oncontextrestored(self):
        val = self._attr.get('oncontextrestored')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncontextrestored -> get attr')

    def set_oncontextrestored(self, val):
        self._attr['oncontextrestored'] = val

    def get_oncuechange(self):
        val = self._attr.get('oncuechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncuechange -> get attr')

    def set_oncuechange(self, val):
        self._attr['oncuechange'] = val

    def get_ondblclick(self):
        val = self._attr.get('ondblclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondblclick -> get attr')

    def set_ondblclick(self, val):
        self._attr['ondblclick'] = val

    def get_ondrag(self):
        val = self._attr.get('ondrag')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondrag -> get attr')

    def set_ondrag(self, val):
        self._attr['ondrag'] = val

    def get_ondragend(self):
        val = self._attr.get('ondragend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondragend -> get attr')

    def set_ondragend(self, val):
        self._attr['ondragend'] = val

    def get_ondragenter(self):
        val = self._attr.get('ondragenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondragenter -> get attr')

    def set_ondragenter(self, val):
        self._attr['ondragenter'] = val

    def get_ondragleave(self):
        val = self._attr.get('ondragleave')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondragleave -> get attr')

    def set_ondragleave(self, val):
        self._attr['ondragleave'] = val

    def get_ondragover(self):
        val = self._attr.get('ondragover')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondragover -> get attr')

    def set_ondragover(self, val):
        self._attr['ondragover'] = val

    def get_ondragstart(self):
        val = self._attr.get('ondragstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondragstart -> get attr')

    def set_ondragstart(self, val):
        self._attr['ondragstart'] = val

    def get_ondrop(self):
        val = self._attr.get('ondrop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondrop -> get attr')

    def set_ondrop(self, val):
        self._attr['ondrop'] = val

    def get_ondurationchange(self):
        val = self._attr.get('ondurationchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ondurationchange -> get attr')

    def set_ondurationchange(self, val):
        self._attr['ondurationchange'] = val

    def get_onemptied(self):
        val = self._attr.get('onemptied')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onemptied -> get attr')

    def set_onemptied(self, val):
        self._attr['onemptied'] = val

    def get_onended(self):
        val = self._attr.get('onended')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onended -> get attr')

    def set_onended(self, val):
        self._attr['onended'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onfocus(self):
        val = self._attr.get('onfocus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onfocus -> get attr')

    def set_onfocus(self, val):
        self._attr['onfocus'] = val

    def get_onformdata(self):
        val = self._attr.get('onformdata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onformdata -> get attr')

    def set_onformdata(self, val):
        self._attr['onformdata'] = val

    def get_oninput(self):
        val = self._attr.get('oninput')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oninput -> get attr')

    def set_oninput(self, val):
        self._attr['oninput'] = val

    def get_oninvalid(self):
        val = self._attr.get('oninvalid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oninvalid -> get attr')

    def set_oninvalid(self, val):
        self._attr['oninvalid'] = val

    def get_onkeydown(self):
        val = self._attr.get('onkeydown')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onkeydown -> get attr')

    def set_onkeydown(self, val):
        self._attr['onkeydown'] = val

    def get_onkeypress(self):
        val = self._attr.get('onkeypress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onkeypress -> get attr')

    def set_onkeypress(self, val):
        self._attr['onkeypress'] = val

    def get_onkeyup(self):
        val = self._attr.get('onkeyup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onkeyup -> get attr')

    def set_onkeyup(self, val):
        self._attr['onkeyup'] = val

    def get_onload(self):
        val = self._attr.get('onload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onload -> get attr')

    def set_onload(self, val):
        self._attr['onload'] = val

    def get_onloadeddata(self):
        val = self._attr.get('onloadeddata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onloadeddata -> get attr')

    def set_onloadeddata(self, val):
        self._attr['onloadeddata'] = val

    def get_onloadedmetadata(self):
        val = self._attr.get('onloadedmetadata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onloadedmetadata -> get attr')

    def set_onloadedmetadata(self, val):
        self._attr['onloadedmetadata'] = val

    def get_onloadstart(self):
        val = self._attr.get('onloadstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onloadstart -> get attr')

    def set_onloadstart(self, val):
        self._attr['onloadstart'] = val

    def get_onmousedown(self):
        val = self._attr.get('onmousedown')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmousedown -> get attr')

    def set_onmousedown(self, val):
        self._attr['onmousedown'] = val

    def get_onmouseenter(self):
        val = self._attr.get('onmouseenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmouseenter -> get attr')

    def set_onmouseenter(self, val):
        self._attr['onmouseenter'] = val

    def get_onmouseleave(self):
        val = self._attr.get('onmouseleave')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmouseleave -> get attr')

    def set_onmouseleave(self, val):
        self._attr['onmouseleave'] = val

    def get_onmousemove(self):
        val = self._attr.get('onmousemove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmousemove -> get attr')

    def set_onmousemove(self, val):
        self._attr['onmousemove'] = val

    def get_onmouseout(self):
        val = self._attr.get('onmouseout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmouseout -> get attr')

    def set_onmouseout(self, val):
        self._attr['onmouseout'] = val

    def get_onmouseover(self):
        val = self._attr.get('onmouseover')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmouseover -> get attr')

    def set_onmouseover(self, val):
        self._attr['onmouseover'] = val

    def get_onmouseup(self):
        val = self._attr.get('onmouseup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmouseup -> get attr')

    def set_onmouseup(self, val):
        self._attr['onmouseup'] = val

    def get_onmousewheel(self):
        val = self._attr.get('onmousewheel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onmousewheel -> get attr')

    def set_onmousewheel(self, val):
        self._attr['onmousewheel'] = val

    def get_onpause(self):
        val = self._attr.get('onpause')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpause -> get attr')

    def set_onpause(self, val):
        self._attr['onpause'] = val

    def get_onplay(self):
        val = self._attr.get('onplay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onplay -> get attr')

    def set_onplay(self, val):
        self._attr['onplay'] = val

    def get_onplaying(self):
        val = self._attr.get('onplaying')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onplaying -> get attr')

    def set_onplaying(self, val):
        self._attr['onplaying'] = val

    def get_onprogress(self):
        val = self._attr.get('onprogress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onprogress -> get attr')

    def set_onprogress(self, val):
        self._attr['onprogress'] = val

    def get_onratechange(self):
        val = self._attr.get('onratechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onratechange -> get attr')

    def set_onratechange(self, val):
        self._attr['onratechange'] = val

    def get_onreset(self):
        val = self._attr.get('onreset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onreset -> get attr')

    def set_onreset(self, val):
        self._attr['onreset'] = val

    def get_onresize(self):
        val = self._attr.get('onresize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onresize -> get attr')

    def set_onresize(self, val):
        self._attr['onresize'] = val

    def get_onscroll(self):
        val = self._attr.get('onscroll')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onscroll -> get attr')

    def set_onscroll(self, val):
        self._attr['onscroll'] = val

    def get_onsecuritypolicyviolation(self):
        val = self._attr.get('onsecuritypolicyviolation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onsecuritypolicyviolation -> get attr')

    def set_onsecuritypolicyviolation(self, val):
        self._attr['onsecuritypolicyviolation'] = val

    def get_onseeked(self):
        val = self._attr.get('onseeked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onseeked -> get attr')

    def set_onseeked(self, val):
        self._attr['onseeked'] = val

    def get_onseeking(self):
        val = self._attr.get('onseeking')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onseeking -> get attr')

    def set_onseeking(self, val):
        self._attr['onseeking'] = val

    def get_onselect(self):
        val = self._attr.get('onselect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onselect -> get attr')

    def set_onselect(self, val):
        self._attr['onselect'] = val

    def get_onslotchange(self):
        val = self._attr.get('onslotchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onslotchange -> get attr')

    def set_onslotchange(self, val):
        self._attr['onslotchange'] = val

    def get_onstalled(self):
        val = self._attr.get('onstalled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onstalled -> get attr')

    def set_onstalled(self, val):
        self._attr['onstalled'] = val

    def get_onsubmit(self):
        val = self._attr.get('onsubmit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onsubmit -> get attr')

    def set_onsubmit(self, val):
        self._attr['onsubmit'] = val

    def get_onsuspend(self):
        val = self._attr.get('onsuspend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onsuspend -> get attr')

    def set_onsuspend(self, val):
        self._attr['onsuspend'] = val

    def get_ontimeupdate(self):
        val = self._attr.get('ontimeupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontimeupdate -> get attr')

    def set_ontimeupdate(self, val):
        self._attr['ontimeupdate'] = val

    def get_ontoggle(self):
        val = self._attr.get('ontoggle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontoggle -> get attr')

    def set_ontoggle(self, val):
        self._attr['ontoggle'] = val

    def get_onvolumechange(self):
        val = self._attr.get('onvolumechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onvolumechange -> get attr')

    def set_onvolumechange(self, val):
        self._attr['onvolumechange'] = val

    def get_onwaiting(self):
        val = self._attr.get('onwaiting')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwaiting -> get attr')

    def set_onwaiting(self, val):
        self._attr['onwaiting'] = val

    def get_onwebkitanimationend(self):
        val = self._attr.get('onwebkitanimationend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwebkitanimationend -> get attr')

    def set_onwebkitanimationend(self, val):
        self._attr['onwebkitanimationend'] = val

    def get_onwebkitanimationiteration(self):
        val = self._attr.get('onwebkitanimationiteration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwebkitanimationiteration -> get attr')

    def set_onwebkitanimationiteration(self, val):
        self._attr['onwebkitanimationiteration'] = val

    def get_onwebkitanimationstart(self):
        val = self._attr.get('onwebkitanimationstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwebkitanimationstart -> get attr')

    def set_onwebkitanimationstart(self, val):
        self._attr['onwebkitanimationstart'] = val

    def get_onwebkittransitionend(self):
        val = self._attr.get('onwebkittransitionend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwebkittransitionend -> get attr')

    def set_onwebkittransitionend(self, val):
        self._attr['onwebkittransitionend'] = val

    def get_onwheel(self):
        val = self._attr.get('onwheel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onwheel -> get attr')

    def set_onwheel(self, val):
        self._attr['onwheel'] = val

    def get_onauxclick(self):
        val = self._attr.get('onauxclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onauxclick -> get attr')

    def set_onauxclick(self, val):
        self._attr['onauxclick'] = val

    def get_ongotpointercapture(self):
        val = self._attr.get('ongotpointercapture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ongotpointercapture -> get attr')

    def set_ongotpointercapture(self, val):
        self._attr['ongotpointercapture'] = val

    def get_onlostpointercapture(self):
        val = self._attr.get('onlostpointercapture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onlostpointercapture -> get attr')

    def set_onlostpointercapture(self, val):
        self._attr['onlostpointercapture'] = val

    def get_onpointerdown(self):
        val = self._attr.get('onpointerdown')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerdown -> get attr')

    def set_onpointerdown(self, val):
        self._attr['onpointerdown'] = val

    def get_onpointermove(self):
        val = self._attr.get('onpointermove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointermove -> get attr')

    def set_onpointermove(self, val):
        self._attr['onpointermove'] = val

    def get_onpointerrawupdate(self):
        val = self._attr.get('onpointerrawupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerrawupdate -> get attr')

    def set_onpointerrawupdate(self, val):
        self._attr['onpointerrawupdate'] = val

    def get_onpointerup(self):
        val = self._attr.get('onpointerup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerup -> get attr')

    def set_onpointerup(self, val):
        self._attr['onpointerup'] = val

    def get_onpointercancel(self):
        val = self._attr.get('onpointercancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointercancel -> get attr')

    def set_onpointercancel(self, val):
        self._attr['onpointercancel'] = val

    def get_onpointerover(self):
        val = self._attr.get('onpointerover')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerover -> get attr')

    def set_onpointerover(self, val):
        self._attr['onpointerover'] = val

    def get_onpointerout(self):
        val = self._attr.get('onpointerout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerout -> get attr')

    def set_onpointerout(self, val):
        self._attr['onpointerout'] = val

    def get_onpointerenter(self):
        val = self._attr.get('onpointerenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerenter -> get attr')

    def set_onpointerenter(self, val):
        self._attr['onpointerenter'] = val

    def get_onpointerleave(self):
        val = self._attr.get('onpointerleave')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpointerleave -> get attr')

    def set_onpointerleave(self, val):
        self._attr['onpointerleave'] = val

    def get_onselectstart(self):
        val = self._attr.get('onselectstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onselectstart -> get attr')

    def set_onselectstart(self, val):
        self._attr['onselectstart'] = val

    def get_onselectionchange(self):
        val = self._attr.get('onselectionchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onselectionchange -> get attr')

    def set_onselectionchange(self, val):
        self._attr['onselectionchange'] = val

    def get_onanimationend(self):
        val = self._attr.get('onanimationend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onanimationend -> get attr')

    def set_onanimationend(self, val):
        self._attr['onanimationend'] = val

    def get_onanimationiteration(self):
        val = self._attr.get('onanimationiteration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onanimationiteration -> get attr')

    def set_onanimationiteration(self, val):
        self._attr['onanimationiteration'] = val

    def get_onanimationstart(self):
        val = self._attr.get('onanimationstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onanimationstart -> get attr')

    def set_onanimationstart(self, val):
        self._attr['onanimationstart'] = val

    def get_ontransitionrun(self):
        val = self._attr.get('ontransitionrun')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontransitionrun -> get attr')

    def set_ontransitionrun(self, val):
        self._attr['ontransitionrun'] = val

    def get_ontransitionstart(self):
        val = self._attr.get('ontransitionstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontransitionstart -> get attr')

    def set_ontransitionstart(self, val):
        self._attr['ontransitionstart'] = val

    def get_ontransitionend(self):
        val = self._attr.get('ontransitionend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontransitionend -> get attr')

    def set_ontransitionend(self, val):
        self._attr['ontransitionend'] = val

    def get_ontransitioncancel(self):
        val = self._attr.get('ontransitioncancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontransitioncancel -> get attr')

    def set_ontransitioncancel(self, val):
        self._attr['ontransitioncancel'] = val

    def get_oncopy(self):
        val = self._attr.get('oncopy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncopy -> get attr')

    def set_oncopy(self, val):
        self._attr['oncopy'] = val

    def get_oncut(self):
        val = self._attr.get('oncut')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.oncut -> get attr')

    def set_oncut(self, val):
        self._attr['oncut'] = val

    def get_onpaste(self):
        val = self._attr.get('onpaste')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onpaste -> get attr')

    def set_onpaste(self, val):
        self._attr['onpaste'] = val

    def get_children(self):
        val = self._attr.get('children')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.children -> get attr')

    def get_firstElementChild(self):
        val = self._attr.get('firstElementChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.firstElementChild -> get attr')

    def get_lastElementChild(self):
        val = self._attr.get('lastElementChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.lastElementChild -> get attr')

    def get_childElementCount(self):
        val = self._attr.get('childElementCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.childElementCount -> get attr')

    def get_activeElement(self):
        val = self._attr.get('activeElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.activeElement -> get attr')

    def get_styleSheets(self):
        val = self._attr.get('styleSheets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.styleSheets -> get attr')

    def get_pointerLockElement(self):
        val = self._attr.get('pointerLockElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.pointerLockElement -> get attr')

    def get_fullscreenElement(self):
        val = self._attr.get('fullscreenElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.fullscreenElement -> get attr')

    def set_fullscreenElement(self, val):
        self._attr['fullscreenElement'] = val

    def get_adoptedStyleSheets(self):
        val = self._attr.get('adoptedStyleSheets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.adoptedStyleSheets -> get attr')

    def set_adoptedStyleSheets(self, val):
        self._attr['adoptedStyleSheets'] = val

    def get_pictureInPictureElement(self):
        val = self._attr.get('pictureInPictureElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.pictureInPictureElement -> get attr')

    def get_fonts(self):
        val = self._attr.get('fonts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.fonts -> get attr')

    def get_onfencedtreeclick(self):
        val = self._attr.get('onfencedtreeclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onfencedtreeclick -> get attr')

    def set_onfencedtreeclick(self, val):
        self._attr['onfencedtreeclick'] = val

    def get_onoverscroll(self):
        val = self._attr.get('onoverscroll')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onoverscroll -> get attr')

    def set_onoverscroll(self, val):
        self._attr['onoverscroll'] = val

    def get_onscrollend(self):
        val = self._attr.get('onscrollend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onscrollend -> get attr')

    def set_onscrollend(self, val):
        self._attr['onscrollend'] = val

    def get_onscrollsnapchange(self):
        val = self._attr.get('onscrollsnapchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onscrollsnapchange -> get attr')

    def set_onscrollsnapchange(self, val):
        self._attr['onscrollsnapchange'] = val

    def get_onscrollsnapchanging(self):
        val = self._attr.get('onscrollsnapchanging')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.onscrollsnapchanging -> get attr')

    def set_onscrollsnapchanging(self, val):
        self._attr['onscrollsnapchanging'] = val

    def get_softNavigations(self):
        val = self._attr.get('softNavigations')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.softNavigations -> get attr')

    def get_fragmentDirective(self):
        val = self._attr.get('fragmentDirective')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.fragmentDirective -> get attr')

    def get_ontouchcancel(self):
        val = self._attr.get('ontouchcancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontouchcancel -> get attr')

    def set_ontouchcancel(self, val):
        self._attr['ontouchcancel'] = val

    def get_ontouchend(self):
        val = self._attr.get('ontouchend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontouchend -> get attr')

    def set_ontouchend(self, val):
        self._attr['ontouchend'] = val

    def get_ontouchmove(self):
        val = self._attr.get('ontouchmove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontouchmove -> get attr')

    def set_ontouchmove(self, val):
        self._attr['ontouchmove'] = val

    def get_ontouchstart(self):
        val = self._attr.get('ontouchstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document.py -> Document.ontouchstart -> get attr')

    def set_ontouchstart(self, val):
        self._attr['ontouchstart'] = val

    def fn_adoptNode(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.adoptNode{tuple(args)} -> method')

    def fn_append(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.append{tuple(args)} -> method')

    def fn_captureEvents(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.captureEvents{tuple(args)} -> method')

    def fn_caretRangeFromPoint(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.caretRangeFromPoint{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.clear{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.close{tuple(args)} -> method')

    def fn_createAttribute(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createAttribute{tuple(args)} -> method')

    def fn_createAttributeNS(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createAttributeNS{tuple(args)} -> method')

    def fn_createCDATASection(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createCDATASection{tuple(args)} -> method')

    def fn_createComment(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createComment{tuple(args)} -> method')

    def fn_createDocumentFragment(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createDocumentFragment{tuple(args)} -> method')

    def fn_createElement(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createElement{tuple(args)} -> method')

    def fn_createElementNS(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createElementNS{tuple(args)} -> method')

    def fn_createEvent(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createEvent{tuple(args)} -> method')

    def fn_createExpression(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createExpression{tuple(args)} -> method')

    def fn_createNSResolver(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createNSResolver{tuple(args)} -> method')

    def fn_createNodeIterator(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createNodeIterator{tuple(args)} -> method')

    def fn_createProcessingInstruction(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createProcessingInstruction{tuple(args)} -> method')

    def fn_createRange(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createRange{tuple(args)} -> method')

    def fn_createTextNode(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createTextNode{tuple(args)} -> method')

    def fn_createTreeWalker(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.createTreeWalker{tuple(args)} -> method')

    def fn_elementFromPoint(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.elementFromPoint{tuple(args)} -> method')

    def fn_elementsFromPoint(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.elementsFromPoint{tuple(args)} -> method')

    def fn_evaluate(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.evaluate{tuple(args)} -> method')

    def fn_execCommand(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.execCommand{tuple(args)} -> method')

    def fn_exitFullscreen(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.exitFullscreen{tuple(args)} -> method')

    def fn_exitPictureInPicture(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.exitPictureInPicture{tuple(args)} -> method')

    def fn_exitPointerLock(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.exitPointerLock{tuple(args)} -> method')

    def fn_getAnimations(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getAnimations{tuple(args)} -> method')

    def fn_getElementById(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getElementById{tuple(args)} -> method')

    def fn_getElementsByClassName(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getElementsByClassName{tuple(args)} -> method')

    def fn_getElementsByName(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getElementsByName{tuple(args)} -> method')

    def fn_getElementsByTagName(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getElementsByTagName{tuple(args)} -> method')

    def fn_getElementsByTagNameNS(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getElementsByTagNameNS{tuple(args)} -> method')

    def fn_getSelection(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getSelection{tuple(args)} -> method')

    def fn_hasFocus(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.hasFocus{tuple(args)} -> method')

    def fn_hasStorageAccess(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.hasStorageAccess{tuple(args)} -> method')

    def fn_hasUnpartitionedCookieAccess(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.hasUnpartitionedCookieAccess{tuple(args)} -> method')

    def fn_importNode(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.importNode{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.open{tuple(args)} -> method')

    def fn_prepend(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.prepend{tuple(args)} -> method')

    def fn_queryCommandEnabled(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.queryCommandEnabled{tuple(args)} -> method')

    def fn_queryCommandIndeterm(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.queryCommandIndeterm{tuple(args)} -> method')

    def fn_queryCommandState(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.queryCommandState{tuple(args)} -> method')

    def fn_queryCommandSupported(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.queryCommandSupported{tuple(args)} -> method')

    def fn_queryCommandValue(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.queryCommandValue{tuple(args)} -> method')

    def fn_querySelector(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.querySelector{tuple(args)} -> method')

    def fn_querySelectorAll(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.querySelectorAll{tuple(args)} -> method')

    def fn_releaseEvents(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.releaseEvents{tuple(args)} -> method')

    def fn_replaceChildren(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.replaceChildren{tuple(args)} -> method')

    def fn_requestStorageAccess(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.requestStorageAccess{tuple(args)} -> method')

    def fn_requestStorageAccessFor(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.requestStorageAccessFor{tuple(args)} -> method')

    def fn_startViewTransition(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.startViewTransition{tuple(args)} -> method')

    def fn_webkitCancelFullScreen(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.webkitCancelFullScreen{tuple(args)} -> method')

    def fn_webkitExitFullscreen(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.webkitExitFullscreen{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.write{tuple(args)} -> method')

    def fn_writeln(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.writeln{tuple(args)} -> method')

    def fn_ariaNotify(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.ariaNotify{tuple(args)} -> method')

    def fn_caretPositionFromPoint(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.caretPositionFromPoint{tuple(args)} -> method')

    def fn_getPartRoot(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.getPartRoot{tuple(args)} -> method')

    def fn_setSequentialFocusStartingPoint(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.setSequentialFocusStartingPoint{tuple(args)} -> method')

    @classmethod
    def fn_parseHTMLUnsafe(cls, *args):
        logger.debug(f'patch -> v8_document.py -> Document.parseHTMLUnsafe{tuple(args)} -> method')

    def fn_browsingTopics(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.browsingTopics{tuple(args)} -> method')

    def fn_hasPrivateToken(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.hasPrivateToken{tuple(args)} -> method')

    def fn_hasRedemptionRecord(self, *args):
        logger.debug(f'patch -> v8_document.py -> Document.hasRedemptionRecord{tuple(args)} -> method')
