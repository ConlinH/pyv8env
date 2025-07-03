from .flags import *


@construct_100001
class FileSystemHandle:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("kind", "get_kind", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("isSameEntry", "fn_isSameEntry", 1, 0, 1, 0, 1, 0, 0),
        ("queryPermission", "fn_queryPermission", 0, 0, 1, 0, 1, 0, 0),
        ("remove", "fn_remove", 0, 0, 1, 0, 1, 0, 0),
        ("requestPermission", "fn_requestPermission", 0, 0, 1, 0, 1, 0, 0),
        ("getCloudIdentifiers", "fn_getCloudIdentifiers", 0, 0, 1, 0, 1, 0, 0),
        ("getUniqueId", "fn_getUniqueId", 0, 0, 1, 0, 1, 0, 0),
        ("move", "fn_move", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.kind -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.name -> get attr')

    def fn_isSameEntry(self, *args):
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.isSameEntry{tuple(args)} -> method')

    def fn_queryPermission(self, *args):
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.queryPermission{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.remove{tuple(args)} -> method')

    def fn_requestPermission(self, *args):
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.requestPermission{tuple(args)} -> method')

    def fn_getCloudIdentifiers(self, *args):
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.getCloudIdentifiers{tuple(args)} -> method')

    def fn_getUniqueId(self, *args):
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.getUniqueId{tuple(args)} -> method')

    def fn_move(self, *args):
        logger.debug(f'patch -> v8_file_system_handle.py -> FileSystemHandle.move{tuple(args)} -> method')
