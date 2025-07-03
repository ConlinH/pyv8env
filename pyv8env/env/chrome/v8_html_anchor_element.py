from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLAnchorElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLAnchorElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("target", "get_target", "set_target", 0, 1, 0, 0, 0, 0, 1),
        ("download", "get_download", "set_download", 0, 1, 0, 0, 0, 0, 1),
        ("ping", "get_ping", "set_ping", 0, 1, 0, 0, 0, 0, 1),
        ("rel", "get_rel", "set_rel", 0, 1, 0, 0, 0, 0, 1),
        ("relList", "get_relList", "set_relList", 0, 1, 0, 0, 0, 0, 1),
        ("hreflang", "get_hreflang", "set_hreflang", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("referrerPolicy", "get_referrerPolicy", "set_referrerPolicy", 0, 1, 0, 0, 0, 0, 1),
        ("text", "get_text", "set_text", 0, 1, 0, 0, 0, 0, 1),
        ("coords", "get_coords", "set_coords", 0, 1, 0, 0, 0, 0, 1),
        ("charset", "get_charset", "set_charset", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("rev", "get_rev", "set_rev", 0, 1, 0, 0, 0, 0, 1),
        ("shape", "get_shape", "set_shape", 0, 1, 0, 0, 0, 0, 1),
        ("origin", "get_origin", None, 0, 1, 0, 0, 0, 0, 1),
        ("protocol", "get_protocol", "set_protocol", 0, 1, 0, 0, 0, 0, 1),
        ("username", "get_username", "set_username", 0, 1, 0, 0, 0, 0, 1),
        ("password", "get_password", "set_password", 0, 1, 0, 0, 0, 0, 1),
        ("host", "get_host", "set_host", 0, 1, 0, 0, 0, 0, 1),
        ("hostname", "get_hostname", "set_hostname", 0, 1, 0, 0, 0, 0, 1),
        ("port", "get_port", "set_port", 0, 1, 0, 0, 0, 0, 1),
        ("pathname", "get_pathname", "set_pathname", 0, 1, 0, 0, 0, 0, 1),
        ("search", "get_search", "set_search", 0, 1, 0, 0, 0, 0, 1),
        ("hash", "get_hash", "set_hash", 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", "set_href", 0, 1, 0, 0, 0, 0, 1),
        ("interestTargetElement", "get_interestTargetElement", "set_interestTargetElement", 0, 1, 0, 0, 0, 0, 1),
        ("interestAction", "get_interestAction", "set_interestAction", 0, 1, 0, 0, 0, 0, 1),
        ("hrefTranslate", "get_hrefTranslate", "set_hrefTranslate", 0, 1, 0, 0, 0, 0, 1),
        ("attributionSrc", "get_attributionSrc", "set_attributionSrc", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.target -> get attr')

    def set_target(self, val):
        self._attr['target'] = val

    def get_download(self):
        val = self._attr.get('download')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.download -> get attr')

    def set_download(self, val):
        self._attr['download'] = val

    def get_ping(self):
        val = self._attr.get('ping')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.ping -> get attr')

    def set_ping(self, val):
        self._attr['ping'] = val

    def get_rel(self):
        val = self._attr.get('rel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.rel -> get attr')

    def set_rel(self, val):
        self._attr['rel'] = val

    def get_relList(self):
        val = self._attr.get('relList')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.relList -> get attr')

    def set_relList(self, val):
        self._attr['relList'] = val

    def get_hreflang(self):
        val = self._attr.get('hreflang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.hreflang -> get attr')

    def set_hreflang(self, val):
        self._attr['hreflang'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_referrerPolicy(self):
        val = self._attr.get('referrerPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.referrerPolicy -> get attr')

    def set_referrerPolicy(self, val):
        self._attr['referrerPolicy'] = val

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.text -> get attr')

    def set_text(self, val):
        self._attr['text'] = val

    def get_coords(self):
        val = self._attr.get('coords')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.coords -> get attr')

    def set_coords(self, val):
        self._attr['coords'] = val

    def get_charset(self):
        val = self._attr.get('charset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.charset -> get attr')

    def set_charset(self, val):
        self._attr['charset'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_rev(self):
        val = self._attr.get('rev')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.rev -> get attr')

    def set_rev(self, val):
        self._attr['rev'] = val

    def get_shape(self):
        val = self._attr.get('shape')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.shape -> get attr')

    def set_shape(self, val):
        self._attr['shape'] = val

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.origin -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.protocol -> get attr')

    def set_protocol(self, val):
        self._attr['protocol'] = val

    def get_username(self):
        val = self._attr.get('username')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.username -> get attr')

    def set_username(self, val):
        self._attr['username'] = val

    def get_password(self):
        val = self._attr.get('password')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.password -> get attr')

    def set_password(self, val):
        self._attr['password'] = val

    def get_host(self):
        val = self._attr.get('host')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.host -> get attr')

    def set_host(self, val):
        self._attr['host'] = val

    def get_hostname(self):
        val = self._attr.get('hostname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.hostname -> get attr')

    def set_hostname(self, val):
        self._attr['hostname'] = val

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.port -> get attr')

    def set_port(self, val):
        self._attr['port'] = val

    def get_pathname(self):
        val = self._attr.get('pathname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.pathname -> get attr')

    def set_pathname(self, val):
        self._attr['pathname'] = val

    def get_search(self):
        val = self._attr.get('search')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.search -> get attr')

    def set_search(self, val):
        self._attr['search'] = val

    def get_hash(self):
        val = self._attr.get('hash')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.hash -> get attr')

    def set_hash(self, val):
        self._attr['hash'] = val

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.href -> get attr')

    def set_href(self, val):
        self._attr['href'] = val

    def get_interestTargetElement(self):
        val = self._attr.get('interestTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.interestTargetElement -> get attr')

    def set_interestTargetElement(self, val):
        self._attr['interestTargetElement'] = val

    def get_interestAction(self):
        val = self._attr.get('interestAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.interestAction -> get attr')

    def set_interestAction(self, val):
        self._attr['interestAction'] = val

    def get_hrefTranslate(self):
        val = self._attr.get('hrefTranslate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.hrefTranslate -> get attr')

    def set_hrefTranslate(self, val):
        self._attr['hrefTranslate'] = val

    def get_attributionSrc(self):
        val = self._attr.get('attributionSrc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.attributionSrc -> get attr')

    def set_attributionSrc(self, val):
        self._attr['attributionSrc'] = val

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_html_anchor_element.py -> HTMLAnchorElement.toString{tuple(args)} -> method')
