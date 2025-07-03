from .flags import *


@construct_100001
class WorkerLocation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("origin", "get_origin", None, 0, 1, 0, 0, 0, 0, 1),
        ("protocol", "get_protocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("host", "get_host", None, 0, 1, 0, 0, 0, 0, 1),
        ("hostname", "get_hostname", None, 0, 1, 0, 0, 0, 0, 1),
        ("port", "get_port", None, 0, 1, 0, 0, 0, 0, 1),
        ("pathname", "get_pathname", None, 0, 1, 0, 0, 0, 0, 1),
        ("search", "get_search", None, 0, 1, 0, 0, 0, 0, 1),
        ("hash", "get_hash", None, 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.origin -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.protocol -> get attr')

    def get_host(self):
        val = self._attr.get('host')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.host -> get attr')

    def get_hostname(self):
        val = self._attr.get('hostname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.hostname -> get attr')

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.port -> get attr')

    def get_pathname(self):
        val = self._attr.get('pathname')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.pathname -> get attr')

    def get_search(self):
        val = self._attr.get('search')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.search -> get attr')

    def get_hash(self):
        val = self._attr.get('hash')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.hash -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.href -> get attr')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_worker_location.py -> WorkerLocation.toString{tuple(args)} -> method')
