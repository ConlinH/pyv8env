from .flags import *
from .v8_event_target import EventTarget


@construct_100021
class WorkerGlobalScope(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WorkerGlobalScope, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("self", "get_self", None, 0, 1, 0, 0, 0, 0, 1),
        ("location", "get_location", None, 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onlanguagechange", "get_onlanguagechange", "set_onlanguagechange", 0, 1, 0, 0, 0, 0, 1),
        ("navigator", "get_navigator", None, 0, 1, 0, 0, 0, 0, 1),
        ("onrejectionhandled", "get_onrejectionhandled", "set_onrejectionhandled", 0, 1, 0, 0, 0, 0, 1),
        ("onunhandledrejection", "get_onunhandledrejection", "set_onunhandledrejection", 0, 1, 0, 0, 0, 0, 1),
        ("isSecureContext", "get_isSecureContext", None, 0, 1, 0, 0, 0, 0, 1),
        ("origin", "get_origin", "set_origin", 0, 1, 0, 0, 0, 0, 1),
        ("trustedTypes", "get_trustedTypes", None, 0, 1, 0, 0, 0, 0, 1),
        ("performance", "get_performance", "set_performance", 0, 1, 0, 0, 0, 0, 1),
        ("crypto", "get_crypto", None, 0, 1, 0, 0, 0, 0, 1),
        ("indexedDB", "get_indexedDB", None, 0, 1, 0, 0, 0, 0, 1),
        ("fonts", "get_fonts", None, 0, 1, 0, 0, 0, 0, 1),
        ("ontimezonechange", "get_ontimezonechange", "set_ontimezonechange", 0, 1, 0, 0, 0, 0, 1),
        ("caches", "get_caches", None, 0, 1, 0, 0, 0, 0, 1),
        ("crossOriginIsolated", "get_crossOriginIsolated", None, 0, 1, 0, 0, 0, 0, 1),
        ("scheduler", "get_scheduler", "set_scheduler", 0, 1, 0, 0, 0, 0, 1),
        ("crossOriginEmbedderPolicy", "get_crossOriginEmbedderPolicy", None, 0, 1, 0, 0, 0, 0, 1),
        ("translation", "get_translation", "set_translation", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createImageBitmap", "fn_createImageBitmap", 1, 0, 1, 0, 1, 0, 0),
        ("fetch", "fn_fetch", 1, 0, 1, 0, 1, 0, 0),
        ("importScripts", "fn_importScripts", 0, 0, 1, 0, 0, 0, 0),
        ("queueMicrotask", "fn_queueMicrotask", 1, 0, 1, 0, 0, 0, 0),
        ("atob", "fn_atob", 1, 0, 1, 0, 0, 0, 0),
        ("btoa", "fn_btoa", 1, 0, 1, 0, 0, 0, 0),
        ("clearInterval", "fn_clearInterval", 0, 0, 1, 0, 0, 0, 0),
        ("clearTimeout", "fn_clearTimeout", 0, 0, 1, 0, 0, 0, 0),
        ("reportError", "fn_reportError", 1, 0, 1, 0, 0, 0, 0),
        ("setInterval", "fn_setInterval", 1, 0, 1, 0, 0, 0, 0),
        ("setTimeout", "fn_setTimeout", 1, 0, 1, 0, 0, 0, 0),
        ("structuredClone", "fn_structuredClone", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_self(self):
        val = self._attr.get('self')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.self -> get attr')

    def get_location(self):
        val = self._attr.get('location')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.location -> get attr')

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onlanguagechange(self):
        val = self._attr.get('onlanguagechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.onlanguagechange -> get attr')

    def set_onlanguagechange(self, val):
        self._attr['onlanguagechange'] = val

    def get_navigator(self):
        val = self._attr.get('navigator')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.navigator -> get attr')

    def get_onrejectionhandled(self):
        val = self._attr.get('onrejectionhandled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.onrejectionhandled -> get attr')

    def set_onrejectionhandled(self, val):
        self._attr['onrejectionhandled'] = val

    def get_onunhandledrejection(self):
        val = self._attr.get('onunhandledrejection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.onunhandledrejection -> get attr')

    def set_onunhandledrejection(self, val):
        self._attr['onunhandledrejection'] = val

    def get_isSecureContext(self):
        val = self._attr.get('isSecureContext')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.isSecureContext -> get attr')

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.origin -> get attr')

    def set_origin(self, val):
        self._attr['origin'] = val

    def get_trustedTypes(self):
        val = self._attr.get('trustedTypes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.trustedTypes -> get attr')

    def get_performance(self):
        val = self._attr.get('performance')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.performance -> get attr')

    def set_performance(self, val):
        self._attr['performance'] = val

    def get_crypto(self):
        val = self._attr.get('crypto')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.crypto -> get attr')

    def get_indexedDB(self):
        val = self._attr.get('indexedDB')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.indexedDB -> get attr')

    def get_fonts(self):
        val = self._attr.get('fonts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.fonts -> get attr')

    def get_ontimezonechange(self):
        val = self._attr.get('ontimezonechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.ontimezonechange -> get attr')

    def set_ontimezonechange(self, val):
        self._attr['ontimezonechange'] = val

    def get_caches(self):
        val = self._attr.get('caches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.caches -> get attr')

    def get_crossOriginIsolated(self):
        val = self._attr.get('crossOriginIsolated')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.crossOriginIsolated -> get attr')

    def get_scheduler(self):
        val = self._attr.get('scheduler')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.scheduler -> get attr')

    def set_scheduler(self, val):
        self._attr['scheduler'] = val

    def get_crossOriginEmbedderPolicy(self):
        val = self._attr.get('crossOriginEmbedderPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.crossOriginEmbedderPolicy -> get attr')

    def get_translation(self):
        val = self._attr.get('translation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.translation -> get attr')

    def set_translation(self, val):
        self._attr['translation'] = val

    def fn_createImageBitmap(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.createImageBitmap{tuple(args)} -> method')

    def fn_fetch(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.fetch{tuple(args)} -> method')

    def fn_importScripts(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.importScripts{tuple(args)} -> method')

    def fn_queueMicrotask(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.queueMicrotask{tuple(args)} -> method')

    def fn_atob(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.atob{tuple(args)} -> method')

    def fn_btoa(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.btoa{tuple(args)} -> method')

    def fn_clearInterval(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.clearInterval{tuple(args)} -> method')

    def fn_clearTimeout(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.clearTimeout{tuple(args)} -> method')

    def fn_reportError(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.reportError{tuple(args)} -> method')

    def fn_setInterval(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.setInterval{tuple(args)} -> method')

    def fn_setTimeout(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.setTimeout{tuple(args)} -> method')

    def fn_structuredClone(self, *args):
        logger.debug(f'patch -> v8_worker_global_scope.py -> WorkerGlobalScope.structuredClone{tuple(args)} -> method')
