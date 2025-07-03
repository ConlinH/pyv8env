from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class IDBRequest(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IDBRequest, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),
        ("error", "get_error", None, 0, 1, 0, 0, 0, 0, 1),
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),
        ("transaction", "get_transaction", None, 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("onsuccess", "get_onsuccess", "set_onsuccess", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_request.py -> IDBRequest.result -> get attr')

    def get_error(self):
        val = self._attr.get('error')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_request.py -> IDBRequest.error -> get attr')

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_request.py -> IDBRequest.source -> get attr')

    def get_transaction(self):
        val = self._attr.get('transaction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_request.py -> IDBRequest.transaction -> get attr')

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_request.py -> IDBRequest.readyState -> get attr')

    def get_onsuccess(self):
        val = self._attr.get('onsuccess')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_request.py -> IDBRequest.onsuccess -> get attr')

    def set_onsuccess(self, val):
        self._attr['onsuccess'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_request.py -> IDBRequest.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val
