from .flags import *


@construct_100001
class FileSystemSyncAccessHandle:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("mode", "get_mode", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("flush", "fn_flush", 0, 0, 1, 0, 0, 0, 0),
        ("getSize", "fn_getSize", 0, 0, 1, 0, 0, 0, 0),
        ("read", "fn_read", 1, 0, 1, 0, 0, 0, 0),
        ("truncate", "fn_truncate", 1, 0, 1, 0, 0, 0, 0),
        ("write", "fn_write", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_sync_access_handle.py -> FileSystemSyncAccessHandle.mode -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_file_system_sync_access_handle.py -> FileSystemSyncAccessHandle.close{tuple(args)} -> method')

    def fn_flush(self, *args):
        logger.debug(f'patch -> v8_file_system_sync_access_handle.py -> FileSystemSyncAccessHandle.flush{tuple(args)} -> method')

    def fn_getSize(self, *args):
        logger.debug(f'patch -> v8_file_system_sync_access_handle.py -> FileSystemSyncAccessHandle.getSize{tuple(args)} -> method')

    def fn_read(self, *args):
        logger.debug(f'patch -> v8_file_system_sync_access_handle.py -> FileSystemSyncAccessHandle.read{tuple(args)} -> method')

    def fn_truncate(self, *args):
        logger.debug(f'patch -> v8_file_system_sync_access_handle.py -> FileSystemSyncAccessHandle.truncate{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_file_system_sync_access_handle.py -> FileSystemSyncAccessHandle.write{tuple(args)} -> method')
