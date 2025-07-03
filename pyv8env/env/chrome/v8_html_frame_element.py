from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLFrameElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLFrameElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("scrolling", "get_scrolling", "set_scrolling", 0, 1, 0, 0, 0, 0, 1),
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("frameBorder", "get_frameBorder", "set_frameBorder", 0, 1, 0, 0, 0, 0, 1),
        ("longDesc", "get_longDesc", "set_longDesc", 0, 1, 0, 0, 0, 0, 1),
        ("noResize", "get_noResize", "set_noResize", 0, 1, 0, 0, 0, 0, 1),
        ("contentDocument", "get_contentDocument", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentWindow", "get_contentWindow", None, 0, 1, 0, 0, 0, 0, 1),
        ("marginHeight", "get_marginHeight", "set_marginHeight", 0, 1, 0, 0, 0, 0, 1),
        ("marginWidth", "get_marginWidth", "set_marginWidth", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_scrolling(self):
        val = self._attr.get('scrolling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.scrolling -> get attr')

    def set_scrolling(self, val):
        self._attr['scrolling'] = val

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_frameBorder(self):
        val = self._attr.get('frameBorder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.frameBorder -> get attr')

    def set_frameBorder(self, val):
        self._attr['frameBorder'] = val

    def get_longDesc(self):
        val = self._attr.get('longDesc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.longDesc -> get attr')

    def set_longDesc(self, val):
        self._attr['longDesc'] = val

    def get_noResize(self):
        val = self._attr.get('noResize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.noResize -> get attr')

    def set_noResize(self, val):
        self._attr['noResize'] = val

    def get_contentDocument(self):
        val = self._attr.get('contentDocument')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.contentDocument -> get attr')

    def get_contentWindow(self):
        val = self._attr.get('contentWindow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.contentWindow -> get attr')

    def get_marginHeight(self):
        val = self._attr.get('marginHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.marginHeight -> get attr')

    def set_marginHeight(self, val):
        self._attr['marginHeight'] = val

    def get_marginWidth(self):
        val = self._attr.get('marginWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_frame_element.py -> HTMLFrameElement.marginWidth -> get attr')

    def set_marginWidth(self, val):
        self._attr['marginWidth'] = val
