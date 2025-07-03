from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLBodyElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLBodyElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("text", "get_text", "set_text", 0, 1, 0, 0, 0, 0, 1),
        ("link", "get_link", "set_link", 0, 1, 0, 0, 0, 0, 1),
        ("vLink", "get_vLink", "set_vLink", 0, 1, 0, 0, 0, 0, 1),
        ("aLink", "get_aLink", "set_aLink", 0, 1, 0, 0, 0, 0, 1),
        ("bgColor", "get_bgColor", "set_bgColor", 0, 1, 0, 0, 0, 0, 1),
        ("background", "get_background", "set_background", 0, 1, 0, 0, 0, 0, 1),
        ("onblur", "get_onblur", "set_onblur", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onfocus", "get_onfocus", "set_onfocus", 0, 1, 0, 0, 0, 0, 1),
        ("onload", "get_onload", "set_onload", 0, 1, 0, 0, 0, 0, 1),
        ("onresize", "get_onresize", "set_onresize", 0, 1, 0, 0, 0, 0, 1),
        ("onscroll", "get_onscroll", "set_onscroll", 0, 1, 0, 0, 0, 0, 1),
        ("onafterprint", "get_onafterprint", "set_onafterprint", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforeprint", "get_onbeforeprint", "set_onbeforeprint", 0, 1, 0, 0, 0, 0, 1),
        ("onbeforeunload", "get_onbeforeunload", "set_onbeforeunload", 0, 1, 0, 0, 0, 0, 1),
        ("onhashchange", "get_onhashchange", "set_onhashchange", 0, 1, 0, 0, 0, 0, 1),
        ("onlanguagechange", "get_onlanguagechange", "set_onlanguagechange", 0, 1, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),
        ("onmessageerror", "get_onmessageerror", "set_onmessageerror", 0, 1, 0, 0, 0, 0, 1),
        ("onoffline", "get_onoffline", "set_onoffline", 0, 1, 0, 0, 0, 0, 1),
        ("ononline", "get_ononline", "set_ononline", 0, 1, 0, 0, 0, 0, 1),
        ("onpagehide", "get_onpagehide", "set_onpagehide", 0, 1, 0, 0, 0, 0, 1),
        ("onpageshow", "get_onpageshow", "set_onpageshow", 0, 1, 0, 0, 0, 0, 1),
        ("onpopstate", "get_onpopstate", "set_onpopstate", 0, 1, 0, 0, 0, 0, 1),
        ("onrejectionhandled", "get_onrejectionhandled", "set_onrejectionhandled", 0, 1, 0, 0, 0, 0, 1),
        ("onstorage", "get_onstorage", "set_onstorage", 0, 1, 0, 0, 0, 0, 1),
        ("onunhandledrejection", "get_onunhandledrejection", "set_onunhandledrejection", 0, 1, 0, 0, 0, 0, 1),
        ("onunload", "get_onunload", "set_onunload", 0, 1, 0, 0, 0, 0, 1),
        ("onorientationchange", "get_onorientationchange", "set_onorientationchange", 0, 1, 0, 0, 0, 0, 1),
        ("onmove", "get_onmove", "set_onmove", 0, 1, 0, 0, 0, 0, 1),
        ("ontimezonechange", "get_ontimezonechange", "set_ontimezonechange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.text -> get attr')

    def set_text(self, val):
        self._attr['text'] = val

    def get_link(self):
        val = self._attr.get('link')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.link -> get attr')

    def set_link(self, val):
        self._attr['link'] = val

    def get_vLink(self):
        val = self._attr.get('vLink')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.vLink -> get attr')

    def set_vLink(self, val):
        self._attr['vLink'] = val

    def get_aLink(self):
        val = self._attr.get('aLink')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.aLink -> get attr')

    def set_aLink(self, val):
        self._attr['aLink'] = val

    def get_bgColor(self):
        val = self._attr.get('bgColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.bgColor -> get attr')

    def set_bgColor(self, val):
        self._attr['bgColor'] = val

    def get_background(self):
        val = self._attr.get('background')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.background -> get attr')

    def set_background(self, val):
        self._attr['background'] = val

    def get_onblur(self):
        val = self._attr.get('onblur')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onblur -> get attr')

    def set_onblur(self, val):
        self._attr['onblur'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onfocus(self):
        val = self._attr.get('onfocus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onfocus -> get attr')

    def set_onfocus(self, val):
        self._attr['onfocus'] = val

    def get_onload(self):
        val = self._attr.get('onload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onload -> get attr')

    def set_onload(self, val):
        self._attr['onload'] = val

    def get_onresize(self):
        val = self._attr.get('onresize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onresize -> get attr')

    def set_onresize(self, val):
        self._attr['onresize'] = val

    def get_onscroll(self):
        val = self._attr.get('onscroll')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onscroll -> get attr')

    def set_onscroll(self, val):
        self._attr['onscroll'] = val

    def get_onafterprint(self):
        val = self._attr.get('onafterprint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onafterprint -> get attr')

    def set_onafterprint(self, val):
        self._attr['onafterprint'] = val

    def get_onbeforeprint(self):
        val = self._attr.get('onbeforeprint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onbeforeprint -> get attr')

    def set_onbeforeprint(self, val):
        self._attr['onbeforeprint'] = val

    def get_onbeforeunload(self):
        val = self._attr.get('onbeforeunload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onbeforeunload -> get attr')

    def set_onbeforeunload(self, val):
        self._attr['onbeforeunload'] = val

    def get_onhashchange(self):
        val = self._attr.get('onhashchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onhashchange -> get attr')

    def set_onhashchange(self, val):
        self._attr['onhashchange'] = val

    def get_onlanguagechange(self):
        val = self._attr.get('onlanguagechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onlanguagechange -> get attr')

    def set_onlanguagechange(self, val):
        self._attr['onlanguagechange'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onmessageerror(self):
        val = self._attr.get('onmessageerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onmessageerror -> get attr')

    def set_onmessageerror(self, val):
        self._attr['onmessageerror'] = val

    def get_onoffline(self):
        val = self._attr.get('onoffline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onoffline -> get attr')

    def set_onoffline(self, val):
        self._attr['onoffline'] = val

    def get_ononline(self):
        val = self._attr.get('ononline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.ononline -> get attr')

    def set_ononline(self, val):
        self._attr['ononline'] = val

    def get_onpagehide(self):
        val = self._attr.get('onpagehide')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onpagehide -> get attr')

    def set_onpagehide(self, val):
        self._attr['onpagehide'] = val

    def get_onpageshow(self):
        val = self._attr.get('onpageshow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onpageshow -> get attr')

    def set_onpageshow(self, val):
        self._attr['onpageshow'] = val

    def get_onpopstate(self):
        val = self._attr.get('onpopstate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onpopstate -> get attr')

    def set_onpopstate(self, val):
        self._attr['onpopstate'] = val

    def get_onrejectionhandled(self):
        val = self._attr.get('onrejectionhandled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onrejectionhandled -> get attr')

    def set_onrejectionhandled(self, val):
        self._attr['onrejectionhandled'] = val

    def get_onstorage(self):
        val = self._attr.get('onstorage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onstorage -> get attr')

    def set_onstorage(self, val):
        self._attr['onstorage'] = val

    def get_onunhandledrejection(self):
        val = self._attr.get('onunhandledrejection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onunhandledrejection -> get attr')

    def set_onunhandledrejection(self, val):
        self._attr['onunhandledrejection'] = val

    def get_onunload(self):
        val = self._attr.get('onunload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onunload -> get attr')

    def set_onunload(self, val):
        self._attr['onunload'] = val

    def get_onorientationchange(self):
        val = self._attr.get('onorientationchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onorientationchange -> get attr')

    def set_onorientationchange(self, val):
        self._attr['onorientationchange'] = val

    def get_onmove(self):
        val = self._attr.get('onmove')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.onmove -> get attr')

    def set_onmove(self, val):
        self._attr['onmove'] = val

    def get_ontimezonechange(self):
        val = self._attr.get('ontimezonechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_body_element.py -> HTMLBodyElement.ontimezonechange -> get attr')

    def set_ontimezonechange(self, val):
        self._attr['ontimezonechange'] = val
