from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLMetaElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLMetaElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("httpEquiv", "get_httpEquiv", "set_httpEquiv", 0, 1, 0, 0, 0, 0, 1),
        ("content", "get_content", "set_content", 0, 1, 0, 0, 0, 0, 1),
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),
        ("scheme", "get_scheme", "set_scheme", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meta_element.py -> HTMLMetaElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_httpEquiv(self):
        val = self._attr.get('httpEquiv')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meta_element.py -> HTMLMetaElement.httpEquiv -> get attr')

    def set_httpEquiv(self, val):
        self._attr['httpEquiv'] = val

    def get_content(self):
        val = self._attr.get('content')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meta_element.py -> HTMLMetaElement.content -> get attr')

    def set_content(self, val):
        self._attr['content'] = val

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meta_element.py -> HTMLMetaElement.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val

    def get_scheme(self):
        val = self._attr.get('scheme')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meta_element.py -> HTMLMetaElement.scheme -> get attr')

    def set_scheme(self, val):
        self._attr['scheme'] = val
