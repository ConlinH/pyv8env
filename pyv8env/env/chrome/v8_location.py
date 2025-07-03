from .flags import *


@construct_100031
class Location:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("ancestorOrigins", "get_ancestorOrigins", None, 0, 0, 4, 0, 0, 0, 1),
        ("href", "get_href", "set_href", 0, 0, 4, 0, 0, 1, 1),
        ("origin", "get_origin", None, 0, 0, 4, 0, 0, 0, 1),
        ("protocol", "get_protocol", "set_protocol", 0, 0, 4, 0, 0, 0, 1),
        ("host", "get_host", "set_host", 0, 0, 4, 0, 0, 0, 1),
        ("hostname", "get_hostname", "set_hostname", 0, 0, 4, 0, 0, 0, 1),
        ("port", "get_port", "set_port", 0, 0, 4, 0, 0, 0, 1),
        ("pathname", "get_pathname", "set_pathname", 0, 0, 4, 0, 0, 0, 1),
        ("search", "get_search", "set_search", 0, 0, 4, 0, 0, 0, 1),
        ("hash", "get_hash", "set_hash", 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("assign", "fn_assign", 1, 0, 0, 5, 0, 0, 0),
        ("reload", "fn_reload", 0, 0, 0, 5, 0, 0, 0),
        ("replace", "fn_replace", 1, 0, 0, 5, 0, 1, 0),
        ("toString", "fn_toString", 0, 0, 0, 5, 0, 0, 0),

    )

    def get_ancestorOrigins(self):
        val = self._attr.get('ancestorOrigins')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.ancestorOrigins -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.href -> get attr')

    def set_href(self, val):
        self._attr['href'] = val

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.origin -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.protocol -> get attr')

    def set_protocol(self, val):
        self._attr['protocol'] = val

    def get_host(self):
        val = self._attr.get('host')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.host -> get attr')

    def set_host(self, val):
        self._attr['host'] = val

    def get_hostname(self):
        val = self._attr.get('hostname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.hostname -> get attr')

    def set_hostname(self, val):
        self._attr['hostname'] = val

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.port -> get attr')

    def set_port(self, val):
        self._attr['port'] = val

    def get_pathname(self):
        val = self._attr.get('pathname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.pathname -> get attr')

    def set_pathname(self, val):
        self._attr['pathname'] = val

    def get_search(self):
        val = self._attr.get('search')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.search -> get attr')

    def set_search(self, val):
        self._attr['search'] = val

    def get_hash(self):
        val = self._attr.get('hash')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_location.py -> Location.hash -> get attr')

    def set_hash(self, val):
        self._attr['hash'] = val

    def fn_assign(self, *args):
        logger.debug(f'patch -> v8_location.py -> Location.assign{tuple(args)} -> method')

    def fn_reload(self, *args):
        logger.debug(f'patch -> v8_location.py -> Location.reload{tuple(args)} -> method')

    def fn_replace(self, *args):
        logger.debug(f'patch -> v8_location.py -> Location.replace{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_location.py -> Location.toString{tuple(args)} -> method')
