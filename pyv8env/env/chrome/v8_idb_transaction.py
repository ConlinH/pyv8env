from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class IDBTransaction(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IDBTransaction, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("objectStoreNames", "get_objectStoreNames", None, 0, 1, 0, 0, 0, 0, 1),
        ("mode", "get_mode", None, 0, 1, 0, 0, 0, 0, 1),
        ("durability", "get_durability", None, 0, 1, 0, 0, 0, 0, 1),
        ("db", "get_db", None, 0, 1, 0, 0, 0, 0, 1),
        ("error", "get_error", None, 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),
        ("oncomplete", "get_oncomplete", "set_oncomplete", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 0, 0, 0),
        ("commit", "fn_commit", 0, 0, 1, 0, 0, 0, 0),
        ("objectStore", "fn_objectStore", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_objectStoreNames(self):
        val = self._attr.get('objectStoreNames')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.objectStoreNames -> get attr')

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.mode -> get attr')

    def get_durability(self):
        val = self._attr.get('durability')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.durability -> get attr')

    def get_db(self):
        val = self._attr.get('db')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.db -> get attr')

    def get_error(self):
        val = self._attr.get('error')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.error -> get attr')

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_oncomplete(self):
        val = self._attr.get('oncomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.oncomplete -> get attr')

    def set_oncomplete(self, val):
        self._attr['oncomplete'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.abort{tuple(args)} -> method')

    def fn_commit(self, *args):
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.commit{tuple(args)} -> method')

    def fn_objectStore(self, *args):
        logger.debug(f'patch -> v8_idb_transaction.py -> IDBTransaction.objectStore{tuple(args)} -> method')
