from .flags import *


@construct_100001
class IDBCursor:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),
        ("direction", "get_direction", None, 0, 1, 0, 0, 0, 0, 1),
        ("key", "get_key", None, 0, 1, 0, 0, 0, 0, 1),
        ("primaryKey", "get_primaryKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("request", "get_request", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("advance", "fn_advance", 1, 0, 1, 0, 0, 0, 0),
        ("continue", "fn_continue", 0, 0, 1, 0, 0, 0, 0),
        ("continuePrimaryKey", "fn_continuePrimaryKey", 2, 0, 1, 0, 0, 0, 0),
        ("delete", "fn_delete", 0, 0, 1, 0, 0, 0, 0),
        ("update", "fn_update", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.source -> get attr')

    def get_direction(self):
        val = self._attr.get('direction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.direction -> get attr')

    def get_key(self):
        val = self._attr.get('key')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.key -> get attr')

    def get_primaryKey(self):
        val = self._attr.get('primaryKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.primaryKey -> get attr')

    def get_request(self):
        val = self._attr.get('request')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.request -> get attr')

    def fn_advance(self, *args):
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.advance{tuple(args)} -> method')

    def fn_continue(self, *args):
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.continue{tuple(args)} -> method')

    def fn_continuePrimaryKey(self, *args):
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.continuePrimaryKey{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.delete{tuple(args)} -> method')

    def fn_update(self, *args):
        logger.debug(f'patch -> v8_idb_cursor.py -> IDBCursor.update{tuple(args)} -> method')
