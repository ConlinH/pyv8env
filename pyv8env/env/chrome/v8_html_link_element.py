from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLLinkElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLLinkElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", "set_href", 0, 1, 0, 0, 0, 0, 1),
        ("crossOrigin", "get_crossOrigin", "set_crossOrigin", 0, 1, 0, 0, 0, 0, 1),
        ("rel", "get_rel", "set_rel", 0, 1, 0, 0, 0, 0, 1),
        ("relList", "get_relList", "set_relList", 0, 1, 0, 0, 0, 0, 1),
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),
        ("hreflang", "get_hreflang", "set_hreflang", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("as", "get_as", "set_as", 0, 1, 0, 0, 0, 0, 1),
        ("referrerPolicy", "get_referrerPolicy", "set_referrerPolicy", 0, 1, 0, 0, 0, 0, 1),
        ("sizes", "get_sizes", "set_sizes", 0, 1, 0, 0, 0, 0, 1),
        ("fetchPriority", "get_fetchPriority", "set_fetchPriority", 0, 1, 0, 0, 0, 0, 1),
        ("imageSrcset", "get_imageSrcset", "set_imageSrcset", 0, 1, 0, 0, 0, 0, 1),
        ("imageSizes", "get_imageSizes", "set_imageSizes", 0, 1, 0, 0, 0, 0, 1),
        ("charset", "get_charset", "set_charset", 0, 1, 0, 0, 0, 0, 1),
        ("rev", "get_rev", "set_rev", 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", "set_target", 0, 1, 0, 0, 0, 0, 1),
        ("sheet", "get_sheet", None, 0, 1, 0, 0, 0, 0, 1),
        ("integrity", "get_integrity", "set_integrity", 0, 1, 0, 0, 0, 0, 1),
        ("blocking", "get_blocking", "set_blocking", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.href -> get attr')

    def set_href(self, val):
        self._attr['href'] = val

    def get_crossOrigin(self):
        val = self._attr.get('crossOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.crossOrigin -> get attr')

    def set_crossOrigin(self, val):
        self._attr['crossOrigin'] = val

    def get_rel(self):
        val = self._attr.get('rel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.rel -> get attr')

    def set_rel(self, val):
        self._attr['rel'] = val

    def get_relList(self):
        val = self._attr.get('relList')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.relList -> get attr')

    def set_relList(self, val):
        self._attr['relList'] = val

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val

    def get_hreflang(self):
        val = self._attr.get('hreflang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.hreflang -> get attr')

    def set_hreflang(self, val):
        self._attr['hreflang'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_as(self):
        val = self._attr.get('as')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.as -> get attr')

    def set_as(self, val):
        self._attr['as'] = val

    def get_referrerPolicy(self):
        val = self._attr.get('referrerPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.referrerPolicy -> get attr')

    def set_referrerPolicy(self, val):
        self._attr['referrerPolicy'] = val

    def get_sizes(self):
        val = self._attr.get('sizes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.sizes -> get attr')

    def set_sizes(self, val):
        self._attr['sizes'] = val

    def get_fetchPriority(self):
        val = self._attr.get('fetchPriority')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.fetchPriority -> get attr')

    def set_fetchPriority(self, val):
        self._attr['fetchPriority'] = val

    def get_imageSrcset(self):
        val = self._attr.get('imageSrcset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.imageSrcset -> get attr')

    def set_imageSrcset(self, val):
        self._attr['imageSrcset'] = val

    def get_imageSizes(self):
        val = self._attr.get('imageSizes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.imageSizes -> get attr')

    def set_imageSizes(self, val):
        self._attr['imageSizes'] = val

    def get_charset(self):
        val = self._attr.get('charset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.charset -> get attr')

    def set_charset(self, val):
        self._attr['charset'] = val

    def get_rev(self):
        val = self._attr.get('rev')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.rev -> get attr')

    def set_rev(self, val):
        self._attr['rev'] = val

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.target -> get attr')

    def set_target(self, val):
        self._attr['target'] = val

    def get_sheet(self):
        val = self._attr.get('sheet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.sheet -> get attr')

    def get_integrity(self):
        val = self._attr.get('integrity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.integrity -> get attr')

    def set_integrity(self, val):
        self._attr['integrity'] = val

    def get_blocking(self):
        val = self._attr.get('blocking')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_link_element.py -> HTMLLinkElement.blocking -> get attr')

    def set_blocking(self, val):
        self._attr['blocking'] = val
