from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLImageElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLImageElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("alt", "get_alt", "set_alt", 0, 1, 0, 0, 0, 0, 1),
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("srcset", "get_srcset", "set_srcset", 0, 1, 0, 0, 0, 0, 1),
        ("sizes", "get_sizes", "set_sizes", 0, 1, 0, 0, 0, 0, 1),
        ("crossOrigin", "get_crossOrigin", "set_crossOrigin", 0, 1, 0, 0, 0, 0, 1),
        ("useMap", "get_useMap", "set_useMap", 0, 1, 0, 0, 0, 0, 1),
        ("isMap", "get_isMap", "set_isMap", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("naturalWidth", "get_naturalWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("naturalHeight", "get_naturalHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("complete", "get_complete", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentSrc", "get_currentSrc", None, 0, 1, 0, 0, 0, 0, 1),
        ("referrerPolicy", "get_referrerPolicy", "set_referrerPolicy", 0, 1, 0, 0, 0, 0, 1),
        ("decoding", "get_decoding", "set_decoding", 0, 1, 0, 0, 0, 0, 1),
        ("fetchPriority", "get_fetchPriority", "set_fetchPriority", 0, 1, 0, 0, 0, 0, 1),
        ("loading", "get_loading", "set_loading", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("lowsrc", "get_lowsrc", "set_lowsrc", 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("hspace", "get_hspace", "set_hspace", 0, 1, 0, 0, 0, 0, 1),
        ("vspace", "get_vspace", "set_vspace", 0, 1, 0, 0, 0, 0, 1),
        ("longDesc", "get_longDesc", "set_longDesc", 0, 1, 0, 0, 0, 0, 1),
        ("border", "get_border", "set_border", 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("attributionSrc", "get_attributionSrc", "set_attributionSrc", 0, 1, 0, 0, 0, 0, 1),
        ("sharedStorageWritable", "get_sharedStorageWritable", "set_sharedStorageWritable", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("decode", "fn_decode", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_alt(self):
        val = self._attr.get('alt')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.alt -> get attr')

    def set_alt(self, val):
        self._attr['alt'] = val

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_srcset(self):
        val = self._attr.get('srcset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.srcset -> get attr')

    def set_srcset(self, val):
        self._attr['srcset'] = val

    def get_sizes(self):
        val = self._attr.get('sizes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.sizes -> get attr')

    def set_sizes(self, val):
        self._attr['sizes'] = val

    def get_crossOrigin(self):
        val = self._attr.get('crossOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.crossOrigin -> get attr')

    def set_crossOrigin(self, val):
        self._attr['crossOrigin'] = val

    def get_useMap(self):
        val = self._attr.get('useMap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.useMap -> get attr')

    def set_useMap(self, val):
        self._attr['useMap'] = val

    def get_isMap(self):
        val = self._attr.get('isMap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.isMap -> get attr')

    def set_isMap(self, val):
        self._attr['isMap'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_naturalWidth(self):
        val = self._attr.get('naturalWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.naturalWidth -> get attr')

    def get_naturalHeight(self):
        val = self._attr.get('naturalHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.naturalHeight -> get attr')

    def get_complete(self):
        val = self._attr.get('complete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.complete -> get attr')

    def get_currentSrc(self):
        val = self._attr.get('currentSrc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.currentSrc -> get attr')

    def get_referrerPolicy(self):
        val = self._attr.get('referrerPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.referrerPolicy -> get attr')

    def set_referrerPolicy(self, val):
        self._attr['referrerPolicy'] = val

    def get_decoding(self):
        val = self._attr.get('decoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.decoding -> get attr')

    def set_decoding(self, val):
        self._attr['decoding'] = val

    def get_fetchPriority(self):
        val = self._attr.get('fetchPriority')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.fetchPriority -> get attr')

    def set_fetchPriority(self, val):
        self._attr['fetchPriority'] = val

    def get_loading(self):
        val = self._attr.get('loading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.loading -> get attr')

    def set_loading(self, val):
        self._attr['loading'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_lowsrc(self):
        val = self._attr.get('lowsrc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.lowsrc -> get attr')

    def set_lowsrc(self, val):
        self._attr['lowsrc'] = val

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_hspace(self):
        val = self._attr.get('hspace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.hspace -> get attr')

    def set_hspace(self, val):
        self._attr['hspace'] = val

    def get_vspace(self):
        val = self._attr.get('vspace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.vspace -> get attr')

    def set_vspace(self, val):
        self._attr['vspace'] = val

    def get_longDesc(self):
        val = self._attr.get('longDesc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.longDesc -> get attr')

    def set_longDesc(self, val):
        self._attr['longDesc'] = val

    def get_border(self):
        val = self._attr.get('border')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.border -> get attr')

    def set_border(self, val):
        self._attr['border'] = val

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.y -> get attr')

    def get_attributionSrc(self):
        val = self._attr.get('attributionSrc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.attributionSrc -> get attr')

    def set_attributionSrc(self, val):
        self._attr['attributionSrc'] = val

    def get_sharedStorageWritable(self):
        val = self._attr.get('sharedStorageWritable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.sharedStorageWritable -> get attr')

    def set_sharedStorageWritable(self, val):
        self._attr['sharedStorageWritable'] = val

    def fn_decode(self, *args):
        logger.debug(f'patch -> v8_html_image_element.py -> HTMLImageElement.decode{tuple(args)} -> method')
