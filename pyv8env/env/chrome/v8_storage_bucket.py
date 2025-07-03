from .flags import *


@construct_100001
class StorageBucket:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("indexedDB", "get_indexedDB", None, 0, 1, 0, 0, 0, 0, 1),
        ("caches", "get_caches", None, 0, 1, 0, 0, 0, 0, 1),
        ("locks", "get_locks", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("estimate", "fn_estimate", 0, 0, 1, 0, 1, 0, 0),
        ("expires", "fn_expires", 0, 0, 1, 0, 1, 0, 0),
        ("getDirectory", "fn_getDirectory", 0, 0, 1, 0, 1, 0, 0),
        ("persisted", "fn_persisted", 0, 0, 1, 0, 1, 0, 0),
        ("setExpires", "fn_setExpires", 1, 0, 1, 0, 1, 0, 0),
        ("durability", "fn_durability", 0, 0, 1, 0, 1, 0, 0),
        ("persist", "fn_persist", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.name -> get attr')

    def get_indexedDB(self):
        val = self._attr.get('indexedDB')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.indexedDB -> get attr')

    def get_caches(self):
        val = self._attr.get('caches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.caches -> get attr')

    def get_locks(self):
        val = self._attr.get('locks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.locks -> get attr')

    def fn_estimate(self, *args):
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.estimate{tuple(args)} -> method')

    def fn_expires(self, *args):
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.expires{tuple(args)} -> method')

    def fn_getDirectory(self, *args):
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.getDirectory{tuple(args)} -> method')

    def fn_persisted(self, *args):
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.persisted{tuple(args)} -> method')

    def fn_setExpires(self, *args):
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.setExpires{tuple(args)} -> method')

    def fn_durability(self, *args):
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.durability{tuple(args)} -> method')

    def fn_persist(self, *args):
        logger.debug(f'patch -> v8_storage_bucket.py -> StorageBucket.persist{tuple(args)} -> method')
