from .flags import *


@construct_111001
class URL:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("origin", "get_origin", None, 0, 1, 0, 0, 0, 0, 1),
        ("protocol", "get_protocol", "set_protocol", 0, 1, 0, 0, 0, 0, 1),
        ("username", "get_username", "set_username", 0, 1, 0, 0, 0, 0, 1),
        ("password", "get_password", "set_password", 0, 1, 0, 0, 0, 0, 1),
        ("host", "get_host", "set_host", 0, 1, 0, 0, 0, 0, 1),
        ("hostname", "get_hostname", "set_hostname", 0, 1, 0, 0, 0, 0, 1),
        ("port", "get_port", "set_port", 0, 1, 0, 0, 0, 0, 1),
        ("pathname", "get_pathname", "set_pathname", 0, 1, 0, 0, 0, 0, 1),
        ("search", "get_search", "set_search", 0, 1, 0, 0, 0, 0, 1),
        ("searchParams", "get_searchParams", None, 0, 1, 0, 0, 0, 0, 1),
        ("hash", "get_hash", "set_hash", 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", "set_href", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("canParse", "fn_canParse", 1, 0, 2, 0, 1, 1, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),
        ("parse", "fn_parse", 1, 0, 2, 0, 1, 1, 0),
        ("createObjectURL", "fn_createObjectURL", 1, 0, 2, 0, 1, 1, 0),
        ("revokeObjectURL", "fn_revokeObjectURL", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.origin -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.protocol -> get attr')

    def set_protocol(self, val):
        self._attr['protocol'] = val

    def get_username(self):
        val = self._attr.get('username')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.username -> get attr')

    def set_username(self, val):
        self._attr['username'] = val

    def get_password(self):
        val = self._attr.get('password')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.password -> get attr')

    def set_password(self, val):
        self._attr['password'] = val

    def get_host(self):
        val = self._attr.get('host')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.host -> get attr')

    def set_host(self, val):
        self._attr['host'] = val

    def get_hostname(self):
        val = self._attr.get('hostname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.hostname -> get attr')

    def set_hostname(self, val):
        self._attr['hostname'] = val

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.port -> get attr')

    def set_port(self, val):
        self._attr['port'] = val

    def get_pathname(self):
        val = self._attr.get('pathname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.pathname -> get attr')

    def set_pathname(self, val):
        self._attr['pathname'] = val

    def get_search(self):
        val = self._attr.get('search')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.search -> get attr')

    def set_search(self, val):
        self._attr['search'] = val

    def get_searchParams(self):
        val = self._attr.get('searchParams')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.searchParams -> get attr')

    def get_hash(self):
        val = self._attr.get('hash')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.hash -> get attr')

    def set_hash(self, val):
        self._attr['hash'] = val

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url.py -> URL.href -> get attr')

    def set_href(self, val):
        self._attr['href'] = val

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_url.py -> URL.toJSON{tuple(args)} -> method')

    @classmethod
    def fn_canParse(cls, *args):
        logger.debug(f'patch -> v8_url.py -> URL.canParse{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_url.py -> URL.toString{tuple(args)} -> method')

    @classmethod
    def fn_parse(cls, *args):
        logger.debug(f'patch -> v8_url.py -> URL.parse{tuple(args)} -> method')

    @classmethod
    def fn_createObjectURL(cls, *args):
        logger.debug(f'patch -> v8_url.py -> URL.createObjectURL{tuple(args)} -> method')

    @classmethod
    def fn_revokeObjectURL(cls, *args):
        logger.debug(f'patch -> v8_url.py -> URL.revokeObjectURL{tuple(args)} -> method')
