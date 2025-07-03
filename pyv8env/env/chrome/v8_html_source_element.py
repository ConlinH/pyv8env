from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLSourceElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLSourceElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("srcset", "get_srcset", "set_srcset", 0, 1, 0, 0, 0, 0, 1),
        ("sizes", "get_sizes", "set_sizes", 0, 1, 0, 0, 0, 0, 1),
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_source_element.py -> HTMLSourceElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_source_element.py -> HTMLSourceElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_srcset(self):
        val = self._attr.get('srcset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_source_element.py -> HTMLSourceElement.srcset -> get attr')

    def set_srcset(self, val):
        self._attr['srcset'] = val

    def get_sizes(self):
        val = self._attr.get('sizes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_source_element.py -> HTMLSourceElement.sizes -> get attr')

    def set_sizes(self, val):
        self._attr['sizes'] = val

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_source_element.py -> HTMLSourceElement.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_source_element.py -> HTMLSourceElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_source_element.py -> HTMLSourceElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val
