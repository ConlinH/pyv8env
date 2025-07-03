from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLEmbedElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLEmbedElement, self).__init__(*args, **kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_name_set__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_name_del__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_index_del__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_html_embed_element.py -> HTMLEmbedElement.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getSVGDocument", "fn_getSVGDocument", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_embed_element.py -> HTMLEmbedElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_embed_element.py -> HTMLEmbedElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_embed_element.py -> HTMLEmbedElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_embed_element.py -> HTMLEmbedElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_embed_element.py -> HTMLEmbedElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_embed_element.py -> HTMLEmbedElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def fn_getSVGDocument(self, *args):
        logger.debug(f'patch -> v8_html_embed_element.py -> HTMLEmbedElement.getSVGDocument{tuple(args)} -> method')
