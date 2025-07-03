from .flags import *
from .v8_worker_global_scope import WorkerGlobalScope


@construct_100031
class DedicatedWorkerGlobalScope(WorkerGlobalScope):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DedicatedWorkerGlobalScope, self).__init__(*args, **kw)
    TEMPORARY = 0
    PERSISTENT = 1

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 0, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 0, 0, 0, 0, 0, 1),
        ("onmessageerror", "get_onmessageerror", "set_onmessageerror", 0, 0, 0, 0, 0, 0, 1),
        ("ai", "get_ai", "set_ai", 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancelAnimationFrame", "fn_cancelAnimationFrame", 1, 0, 0, 0, 0, 0, 0),
        ("close", "fn_close", 0, 0, 0, 0, 0, 0, 0),
        ("postMessage", "fn_postMessage", 1, 0, 0, 0, 0, 0, 0),
        ("requestAnimationFrame", "fn_requestAnimationFrame", 1, 0, 0, 0, 0, 0, 0),
        ("webkitRequestFileSystem", "fn_webkitRequestFileSystem", 2, 0, 0, 0, 0, 0, 0),
        ("webkitRequestFileSystemSync", "fn_webkitRequestFileSystemSync", 2, 0, 0, 0, 0, 0, 0),
        ("webkitResolveLocalFileSystemSyncURL", "fn_webkitResolveLocalFileSystemSyncURL", 1, 0, 0, 0, 0, 0, 0),
        ("webkitResolveLocalFileSystemURL", "fn_webkitResolveLocalFileSystemURL", 2, 0, 0, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onmessageerror(self):
        val = self._attr.get('onmessageerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.onmessageerror -> get attr')

    def set_onmessageerror(self, val):
        self._attr['onmessageerror'] = val

    def get_ai(self):
        val = self._attr.get('ai')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.ai -> get attr')

    def set_ai(self, val):
        self._attr['ai'] = val

    def fn_cancelAnimationFrame(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.cancelAnimationFrame{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.close{tuple(args)} -> method')

    def fn_postMessage(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.postMessage{tuple(args)} -> method')

    def fn_requestAnimationFrame(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.requestAnimationFrame{tuple(args)} -> method')

    def fn_webkitRequestFileSystem(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.webkitRequestFileSystem{tuple(args)} -> method')

    def fn_webkitRequestFileSystemSync(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.webkitRequestFileSystemSync{tuple(args)} -> method')

    def fn_webkitResolveLocalFileSystemSyncURL(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.webkitResolveLocalFileSystemSyncURL{tuple(args)} -> method')

    def fn_webkitResolveLocalFileSystemURL(self, *args):
        logger.debug(f'patch -> v8_dedicated_worker_global_scope.py -> DedicatedWorkerGlobalScope.webkitResolveLocalFileSystemURL{tuple(args)} -> method')
