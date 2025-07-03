from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class IDBDatabase(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IDBDatabase, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("version", "get_version", None, 0, 1, 0, 0, 0, 0, 1),
        ("objectStoreNames", "get_objectStoreNames", None, 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onversionchange", "get_onversionchange", "set_onversionchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("createObjectStore", "fn_createObjectStore", 1, 0, 1, 0, 0, 0, 0),
        ("deleteObjectStore", "fn_deleteObjectStore", 1, 0, 1, 0, 0, 0, 0),
        ("transaction", "fn_transaction", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.name -> get attr')

    def get_version(self):
        val = self._attr.get('version')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.version -> get attr')

    def get_objectStoreNames(self):
        val = self._attr.get('objectStoreNames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.objectStoreNames -> get attr')

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onversionchange(self):
        val = self._attr.get('onversionchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.onversionchange -> get attr')

    def set_onversionchange(self, val):
        self._attr['onversionchange'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.close{tuple(args)} -> method')

    def fn_createObjectStore(self, *args):
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.createObjectStore{tuple(args)} -> method')

    def fn_deleteObjectStore(self, *args):
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.deleteObjectStore{tuple(args)} -> method')

    def fn_transaction(self, *args):
        logger.debug(f'patch -> v8_idb_database.py -> IDBDatabase.transaction{tuple(args)} -> method')
