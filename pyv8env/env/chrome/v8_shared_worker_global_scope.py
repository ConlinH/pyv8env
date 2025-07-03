from .flags import *
from .v8_worker_global_scope import WorkerGlobalScope


@construct_100031
class SharedWorkerGlobalScope(WorkerGlobalScope):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SharedWorkerGlobalScope, self).__init__(*args, **kw)
    TEMPORARY = 0
    PERSISTENT = 1

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 0, 0, 0, 0, 0, 1),
        ("onconnect", "get_onconnect", "set_onconnect", 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 0, 0, 0, 0, 0),
        ("webkitRequestFileSystem", "fn_webkitRequestFileSystem", 2, 0, 0, 0, 0, 0, 0),
        ("webkitRequestFileSystemSync", "fn_webkitRequestFileSystemSync", 2, 0, 0, 0, 0, 0, 0),
        ("webkitResolveLocalFileSystemSyncURL", "fn_webkitResolveLocalFileSystemSyncURL", 1, 0, 0, 0, 0, 0, 0),
        ("webkitResolveLocalFileSystemURL", "fn_webkitResolveLocalFileSystemURL", 2, 0, 0, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shared_worker_global_scope.py -> SharedWorkerGlobalScope.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_onconnect(self):
        val = self._attr.get('onconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shared_worker_global_scope.py -> SharedWorkerGlobalScope.onconnect -> get attr')

    def set_onconnect(self, val):
        self._attr['onconnect'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_shared_worker_global_scope.py -> SharedWorkerGlobalScope.close{tuple(args)} -> method')

    def fn_webkitRequestFileSystem(self, *args):
        logger.debug(f'patch -> v8_shared_worker_global_scope.py -> SharedWorkerGlobalScope.webkitRequestFileSystem{tuple(args)} -> method')

    def fn_webkitRequestFileSystemSync(self, *args):
        logger.debug(f'patch -> v8_shared_worker_global_scope.py -> SharedWorkerGlobalScope.webkitRequestFileSystemSync{tuple(args)} -> method')

    def fn_webkitResolveLocalFileSystemSyncURL(self, *args):
        logger.debug(f'patch -> v8_shared_worker_global_scope.py -> SharedWorkerGlobalScope.webkitResolveLocalFileSystemSyncURL{tuple(args)} -> method')

    def fn_webkitResolveLocalFileSystemURL(self, *args):
        logger.debug(f'patch -> v8_shared_worker_global_scope.py -> SharedWorkerGlobalScope.webkitResolveLocalFileSystemURL{tuple(args)} -> method')
