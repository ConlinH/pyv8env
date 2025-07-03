from .flags import *


@construct_100001
class IDBIndex:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("objectStore", "get_objectStore", None, 0, 1, 0, 0, 0, 0, 1),
        ("keyPath", "get_keyPath", None, 0, 1, 0, 0, 0, 0, 1),
        ("multiEntry", "get_multiEntry", None, 0, 1, 0, 0, 0, 0, 1),
        ("unique", "get_unique", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("count", "fn_count", 0, 0, 1, 0, 0, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 0, 0, 0),
        ("getAll", "fn_getAll", 0, 0, 1, 0, 0, 0, 0),
        ("getAllKeys", "fn_getAllKeys", 0, 0, 1, 0, 0, 0, 0),
        ("getKey", "fn_getKey", 1, 0, 1, 0, 0, 0, 0),
        ("openCursor", "fn_openCursor", 0, 0, 1, 0, 0, 0, 0),
        ("openKeyCursor", "fn_openKeyCursor", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_objectStore(self):
        val = self._attr.get('objectStore')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.objectStore -> get attr')

    def get_keyPath(self):
        val = self._attr.get('keyPath')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.keyPath -> get attr')

    def get_multiEntry(self):
        val = self._attr.get('multiEntry')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.multiEntry -> get attr')

    def get_unique(self):
        val = self._attr.get('unique')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.unique -> get attr')

    def fn_count(self, *args):
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.count{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.get{tuple(args)} -> method')

    def fn_getAll(self, *args):
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.getAll{tuple(args)} -> method')

    def fn_getAllKeys(self, *args):
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.getAllKeys{tuple(args)} -> method')

    def fn_getKey(self, *args):
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.getKey{tuple(args)} -> method')

    def fn_openCursor(self, *args):
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.openCursor{tuple(args)} -> method')

    def fn_openKeyCursor(self, *args):
        logger.debug(f'patch -> v8_idb_index.py -> IDBIndex.openKeyCursor{tuple(args)} -> method')
