from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLAreaElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLAreaElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("alt", "get_alt", "set_alt", 0, 1, 0, 0, 0, 0, 1),
        ("coords", "get_coords", "set_coords", 0, 1, 0, 0, 0, 0, 1),
        ("download", "get_download", "set_download", 0, 1, 0, 0, 0, 0, 1),
        ("shape", "get_shape", "set_shape", 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", "set_target", 0, 1, 0, 0, 0, 0, 1),
        ("ping", "get_ping", "set_ping", 0, 1, 0, 0, 0, 0, 1),
        ("rel", "get_rel", "set_rel", 0, 1, 0, 0, 0, 0, 1),
        ("relList", "get_relList", "set_relList", 0, 1, 0, 0, 0, 0, 1),
        ("referrerPolicy", "get_referrerPolicy", "set_referrerPolicy", 0, 1, 0, 0, 0, 0, 1),
        ("noHref", "get_noHref", "set_noHref", 0, 1, 0, 0, 0, 0, 1),
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

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_alt(self):
        val = self._attr.get('alt')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.alt -> get attr')

    def set_alt(self, val):
        self._attr['alt'] = val

    def get_coords(self):
        val = self._attr.get('coords')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.coords -> get attr')

    def set_coords(self, val):
        self._attr['coords'] = val

    def get_download(self):
        val = self._attr.get('download')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.download -> get attr')

    def set_download(self, val):
        self._attr['download'] = val

    def get_shape(self):
        val = self._attr.get('shape')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.shape -> get attr')

    def set_shape(self, val):
        self._attr['shape'] = val

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.target -> get attr')

    def set_target(self, val):
        self._attr['target'] = val

    def get_ping(self):
        val = self._attr.get('ping')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.ping -> get attr')

    def set_ping(self, val):
        self._attr['ping'] = val

    def get_rel(self):
        val = self._attr.get('rel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.rel -> get attr')

    def set_rel(self, val):
        self._attr['rel'] = val

    def get_relList(self):
        val = self._attr.get('relList')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.relList -> get attr')

    def set_relList(self, val):
        self._attr['relList'] = val

    def get_referrerPolicy(self):
        val = self._attr.get('referrerPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.referrerPolicy -> get attr')

    def set_referrerPolicy(self, val):
        self._attr['referrerPolicy'] = val

    def get_noHref(self):
        val = self._attr.get('noHref')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.noHref -> get attr')

    def set_noHref(self, val):
        self._attr['noHref'] = val

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.origin -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.protocol -> get attr')

    def set_protocol(self, val):
        self._attr['protocol'] = val

    def get_username(self):
        val = self._attr.get('username')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.username -> get attr')

    def set_username(self, val):
        self._attr['username'] = val

    def get_password(self):
        val = self._attr.get('password')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.password -> get attr')

    def set_password(self, val):
        self._attr['password'] = val

    def get_host(self):
        val = self._attr.get('host')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.host -> get attr')

    def set_host(self, val):
        self._attr['host'] = val

    def get_hostname(self):
        val = self._attr.get('hostname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.hostname -> get attr')

    def set_hostname(self, val):
        self._attr['hostname'] = val

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.port -> get attr')

    def set_port(self, val):
        self._attr['port'] = val

    def get_pathname(self):
        val = self._attr.get('pathname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.pathname -> get attr')

    def set_pathname(self, val):
        self._attr['pathname'] = val

    def get_search(self):
        val = self._attr.get('search')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.search -> get attr')

    def set_search(self, val):
        self._attr['search'] = val

    def get_hash(self):
        val = self._attr.get('hash')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.hash -> get attr')

    def set_hash(self, val):
        self._attr['hash'] = val

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.href -> get attr')

    def set_href(self, val):
        self._attr['href'] = val

    def get_interestTargetElement(self):
        val = self._attr.get('interestTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.interestTargetElement -> get attr')

    def set_interestTargetElement(self, val):
        self._attr['interestTargetElement'] = val

    def get_interestAction(self):
        val = self._attr.get('interestAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.interestAction -> get attr')

    def set_interestAction(self, val):
        self._attr['interestAction'] = val

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_html_area_element.py -> HTMLAreaElement.toString{tuple(args)} -> method')
