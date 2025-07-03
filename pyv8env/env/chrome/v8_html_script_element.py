from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLScriptElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLScriptElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("noModule", "get_noModule", "set_noModule", 0, 1, 0, 0, 0, 0, 1),
        ("charset", "get_charset", "set_charset", 0, 1, 0, 0, 0, 0, 1),
        ("async", "get_async", "set_async", 0, 1, 0, 0, 0, 0, 1),
        ("defer", "get_defer", "set_defer", 0, 1, 0, 0, 0, 0, 1),
        ("crossOrigin", "get_crossOrigin", "set_crossOrigin", 0, 1, 0, 0, 0, 0, 1),
        ("text", "get_text", "set_text", 0, 1, 0, 0, 0, 0, 1),
        ("referrerPolicy", "get_referrerPolicy", "set_referrerPolicy", 0, 1, 0, 0, 0, 0, 1),
        ("fetchPriority", "get_fetchPriority", "set_fetchPriority", 0, 1, 0, 0, 0, 0, 1),
        ("event", "get_event", "set_event", 0, 1, 0, 0, 0, 0, 1),
        ("htmlFor", "get_htmlFor", "set_htmlFor", 0, 1, 0, 0, 0, 0, 1),
        ("integrity", "get_integrity", "set_integrity", 0, 1, 0, 0, 0, 0, 1),
        ("blocking", "get_blocking", "set_blocking", 0, 1, 0, 0, 0, 0, 1),
        ("attributionSrc", "get_attributionSrc", "set_attributionSrc", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("supports", "fn_supports", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_noModule(self):
        val = self._attr.get('noModule')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.noModule -> get attr')

    def set_noModule(self, val):
        self._attr['noModule'] = val

    def get_charset(self):
        val = self._attr.get('charset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.charset -> get attr')

    def set_charset(self, val):
        self._attr['charset'] = val

    def get_async(self):
        val = self._attr.get('async')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.async -> get attr')

    def set_async(self, val):
        self._attr['async'] = val

    def get_defer(self):
        val = self._attr.get('defer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.defer -> get attr')

    def set_defer(self, val):
        self._attr['defer'] = val

    def get_crossOrigin(self):
        val = self._attr.get('crossOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.crossOrigin -> get attr')

    def set_crossOrigin(self, val):
        self._attr['crossOrigin'] = val

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.text -> get attr')

    def set_text(self, val):
        self._attr['text'] = val

    def get_referrerPolicy(self):
        val = self._attr.get('referrerPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.referrerPolicy -> get attr')

    def set_referrerPolicy(self, val):
        self._attr['referrerPolicy'] = val

    def get_fetchPriority(self):
        val = self._attr.get('fetchPriority')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.fetchPriority -> get attr')

    def set_fetchPriority(self, val):
        self._attr['fetchPriority'] = val

    def get_event(self):
        val = self._attr.get('event')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.event -> get attr')

    def set_event(self, val):
        self._attr['event'] = val

    def get_htmlFor(self):
        val = self._attr.get('htmlFor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.htmlFor -> get attr')

    def set_htmlFor(self, val):
        self._attr['htmlFor'] = val

    def get_integrity(self):
        val = self._attr.get('integrity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.integrity -> get attr')

    def set_integrity(self, val):
        self._attr['integrity'] = val

    def get_blocking(self):
        val = self._attr.get('blocking')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.blocking -> get attr')

    def set_blocking(self, val):
        self._attr['blocking'] = val

    def get_attributionSrc(self):
        val = self._attr.get('attributionSrc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.attributionSrc -> get attr')

    def set_attributionSrc(self, val):
        self._attr['attributionSrc'] = val

    @classmethod
    def fn_supports(cls, *args):
        logger.debug(f'patch -> v8_html_script_element.py -> HTMLScriptElement.supports{tuple(args)} -> method')
