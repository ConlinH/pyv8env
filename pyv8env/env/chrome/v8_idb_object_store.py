from .flags import *


@construct_100001
class IDBObjectStore:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("keyPath", "get_keyPath", None, 0, 1, 0, 0, 0, 0, 1),
        ("indexNames", "get_indexNames", None, 0, 1, 0, 0, 0, 0, 1),
        ("transaction", "get_transaction", None, 0, 1, 0, 0, 0, 0, 1),
        ("autoIncrement", "get_autoIncrement", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("count", "fn_count", 0, 0, 1, 0, 0, 0, 0),
        ("createIndex", "fn_createIndex", 2, 0, 1, 0, 0, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 0, 0, 0),
        ("deleteIndex", "fn_deleteIndex", 1, 0, 1, 0, 0, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 0, 0, 0),
        ("getAll", "fn_getAll", 0, 0, 1, 0, 0, 0, 0),
        ("getAllKeys", "fn_getAllKeys", 0, 0, 1, 0, 0, 0, 0),
        ("getKey", "fn_getKey", 1, 0, 1, 0, 0, 0, 0),
        ("index", "fn_index", 1, 0, 1, 0, 0, 0, 0),
        ("openCursor", "fn_openCursor", 0, 0, 1, 0, 0, 0, 0),
        ("openKeyCursor", "fn_openKeyCursor", 0, 0, 1, 0, 0, 0, 0),
        ("put", "fn_put", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_keyPath(self):
        val = self._attr.get('keyPath')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.keyPath -> get attr')

    def get_indexNames(self):
        val = self._attr.get('indexNames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.indexNames -> get attr')

    def get_transaction(self):
        val = self._attr.get('transaction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.transaction -> get attr')

    def get_autoIncrement(self):
        val = self._attr.get('autoIncrement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.autoIncrement -> get attr')

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.add{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.clear{tuple(args)} -> method')

    def fn_count(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.count{tuple(args)} -> method')

    def fn_createIndex(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.createIndex{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.delete{tuple(args)} -> method')

    def fn_deleteIndex(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.deleteIndex{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.get{tuple(args)} -> method')

    def fn_getAll(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.getAll{tuple(args)} -> method')

    def fn_getAllKeys(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.getAllKeys{tuple(args)} -> method')

    def fn_getKey(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.getKey{tuple(args)} -> method')

    def fn_index(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.index{tuple(args)} -> method')

    def fn_openCursor(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.openCursor{tuple(args)} -> method')

    def fn_openKeyCursor(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.openKeyCursor{tuple(args)} -> method')

    def fn_put(self, *args):
        logger.debug(f'patch -> v8_idb_object_store.py -> IDBObjectStore.put{tuple(args)} -> method')
