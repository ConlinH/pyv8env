from .flags import *


@construct_000001
class StorageAccessHandle:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("sessionStorage", "get_sessionStorage", None, 0, 1, 0, 0, 0, 0, 1),
        ("localStorage", "get_localStorage", None, 0, 1, 0, 0, 0, 0, 1),
        ("indexedDB", "get_indexedDB", None, 0, 1, 0, 0, 0, 0, 1),
        ("locks", "get_locks", None, 0, 1, 0, 0, 0, 0, 1),
        ("caches", "get_caches", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("BroadcastChannel", "fn_BroadcastChannel", 1, 0, 1, 0, 0, 0, 0),
        ("SharedWorker", "fn_SharedWorker", 1, 0, 1, 0, 0, 0, 0),
        ("createObjectURL", "fn_createObjectURL", 1, 0, 1, 0, 0, 0, 0),
        ("estimate", "fn_estimate", 0, 0, 1, 0, 1, 0, 0),
        ("getDirectory", "fn_getDirectory", 0, 0, 1, 0, 1, 0, 0),
        ("revokeObjectURL", "fn_revokeObjectURL", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_sessionStorage(self):
        val = self._attr.get('sessionStorage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.sessionStorage -> get attr')

    def get_localStorage(self):
        val = self._attr.get('localStorage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.localStorage -> get attr')

    def get_indexedDB(self):
        val = self._attr.get('indexedDB')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.indexedDB -> get attr')

    def get_locks(self):
        val = self._attr.get('locks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.locks -> get attr')

    def get_caches(self):
        val = self._attr.get('caches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.caches -> get attr')

    def fn_BroadcastChannel(self, *args):
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.BroadcastChannel{tuple(args)} -> method')

    def fn_SharedWorker(self, *args):
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.SharedWorker{tuple(args)} -> method')

    def fn_createObjectURL(self, *args):
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.createObjectURL{tuple(args)} -> method')

    def fn_estimate(self, *args):
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.estimate{tuple(args)} -> method')

    def fn_getDirectory(self, *args):
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.getDirectory{tuple(args)} -> method')

    def fn_revokeObjectURL(self, *args):
        logger.debug(f'patch -> v8_storage_access_handle.py -> StorageAccessHandle.revokeObjectURL{tuple(args)} -> method')
