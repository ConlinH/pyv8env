from .flags import *


@construct_110001
class URLPattern:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("protocol", "get_protocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("username", "get_username", None, 0, 1, 0, 0, 0, 0, 1),
        ("password", "get_password", None, 0, 1, 0, 0, 0, 0, 1),
        ("hostname", "get_hostname", None, 0, 1, 0, 0, 0, 0, 1),
        ("port", "get_port", None, 0, 1, 0, 0, 0, 0, 1),
        ("pathname", "get_pathname", None, 0, 1, 0, 0, 0, 0, 1),
        ("search", "get_search", None, 0, 1, 0, 0, 0, 0, 1),
        ("hash", "get_hash", None, 0, 1, 0, 0, 0, 0, 1),
        ("hasRegExpGroups", "get_hasRegExpGroups", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("exec", "fn_exec", 0, 0, 1, 0, 0, 0, 0),
        ("test", "fn_test", 0, 0, 1, 0, 0, 0, 0),
        ("compareComponent", "fn_compareComponent", 3, 0, 2, 0, 1, 1, 0),

    )

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.protocol -> get attr')

    def get_username(self):
        val = self._attr.get('username')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.username -> get attr')

    def get_password(self):
        val = self._attr.get('password')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.password -> get attr')

    def get_hostname(self):
        val = self._attr.get('hostname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.hostname -> get attr')

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.port -> get attr')

    def get_pathname(self):
        val = self._attr.get('pathname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.pathname -> get attr')

    def get_search(self):
        val = self._attr.get('search')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.search -> get attr')

    def get_hash(self):
        val = self._attr.get('hash')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.hash -> get attr')

    def get_hasRegExpGroups(self):
        val = self._attr.get('hasRegExpGroups')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.hasRegExpGroups -> get attr')

    def fn_exec(self, *args):
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.exec{tuple(args)} -> method')

    def fn_test(self, *args):
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.test{tuple(args)} -> method')

    @classmethod
    def fn_compareComponent(cls, *args):
        logger.debug(f'patch -> v8_url_pattern.py -> URLPattern.compareComponent{tuple(args)} -> method')
