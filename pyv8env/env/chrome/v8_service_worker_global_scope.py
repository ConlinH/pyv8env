from .flags import *
from .v8_worker_global_scope import WorkerGlobalScope


@construct_100031
class ServiceWorkerGlobalScope(WorkerGlobalScope):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ServiceWorkerGlobalScope, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("clients", "get_clients", None, 0, 0, 0, 0, 0, 0, 1),
        ("registration", "get_registration", None, 0, 0, 0, 0, 0, 0, 1),
        ("serviceWorker", "get_serviceWorker", None, 0, 0, 0, 0, 0, 0, 1),
        ("onactivate", "get_onactivate", "set_onactivate", 0, 0, 0, 0, 0, 0, 1),
        ("onfetch", "get_onfetch", "set_onfetch", 0, 0, 0, 0, 0, 0, 1),
        ("oninstall", "get_oninstall", "set_oninstall", 0, 0, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 0, 0, 0, 0, 0, 1),
        ("onmessageerror", "get_onmessageerror", "set_onmessageerror", 0, 0, 0, 0, 0, 0, 1),
        ("onsync", "get_onsync", "set_onsync", 0, 0, 0, 0, 0, 0, 1),
        ("cookieStore", "get_cookieStore", None, 0, 0, 0, 0, 0, 0, 1),
        ("oncookiechange", "get_oncookiechange", "set_oncookiechange", 0, 0, 0, 0, 0, 0, 1),
        ("onbackgroundfetchsuccess", "get_onbackgroundfetchsuccess", "set_onbackgroundfetchsuccess", 0, 0, 0, 0, 0, 0, 1),
        ("onbackgroundfetchfail", "get_onbackgroundfetchfail", "set_onbackgroundfetchfail", 0, 0, 0, 0, 0, 0, 1),
        ("onbackgroundfetchabort", "get_onbackgroundfetchabort", "set_onbackgroundfetchabort", 0, 0, 0, 0, 0, 0, 1),
        ("onbackgroundfetchclick", "get_onbackgroundfetchclick", "set_onbackgroundfetchclick", 0, 0, 0, 0, 0, 0, 1),
        ("onperiodicsync", "get_onperiodicsync", "set_onperiodicsync", 0, 0, 0, 0, 0, 0, 1),
        ("oncontentdelete", "get_oncontentdelete", "set_oncontentdelete", 0, 0, 0, 0, 0, 0, 1),
        ("onnotificationclick", "get_onnotificationclick", "set_onnotificationclick", 0, 0, 0, 0, 0, 0, 1),
        ("onnotificationclose", "get_onnotificationclose", "set_onnotificationclose", 0, 0, 0, 0, 0, 0, 1),
        ("onabortpayment", "get_onabortpayment", "set_onabortpayment", 0, 0, 0, 0, 0, 0, 1),
        ("oncanmakepayment", "get_oncanmakepayment", "set_oncanmakepayment", 0, 0, 0, 0, 0, 0, 1),
        ("onpaymentrequest", "get_onpaymentrequest", "set_onpaymentrequest", 0, 0, 0, 0, 0, 0, 1),
        ("onpush", "get_onpush", "set_onpush", 0, 0, 0, 0, 0, 0, 1),
        ("onpushsubscriptionchange", "get_onpushsubscriptionchange", "set_onpushsubscriptionchange", 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("skipWaiting", "fn_skipWaiting", 0, 0, 0, 0, 1, 0, 0),

    )

    def get_clients(self):
        val = self._attr.get('clients')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.clients -> get attr')

    def get_registration(self):
        val = self._attr.get('registration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.registration -> get attr')

    def get_serviceWorker(self):
        val = self._attr.get('serviceWorker')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.serviceWorker -> get attr')

    def get_onactivate(self):
        val = self._attr.get('onactivate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onactivate -> get attr')

    def set_onactivate(self, val):
        self._attr['onactivate'] = val

    def get_onfetch(self):
        val = self._attr.get('onfetch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onfetch -> get attr')

    def set_onfetch(self, val):
        self._attr['onfetch'] = val

    def get_oninstall(self):
        val = self._attr.get('oninstall')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.oninstall -> get attr')

    def set_oninstall(self, val):
        self._attr['oninstall'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onmessageerror(self):
        val = self._attr.get('onmessageerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onmessageerror -> get attr')

    def set_onmessageerror(self, val):
        self._attr['onmessageerror'] = val

    def get_onsync(self):
        val = self._attr.get('onsync')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onsync -> get attr')

    def set_onsync(self, val):
        self._attr['onsync'] = val

    def get_cookieStore(self):
        val = self._attr.get('cookieStore')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.cookieStore -> get attr')

    def get_oncookiechange(self):
        val = self._attr.get('oncookiechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.oncookiechange -> get attr')

    def set_oncookiechange(self, val):
        self._attr['oncookiechange'] = val

    def get_onbackgroundfetchsuccess(self):
        val = self._attr.get('onbackgroundfetchsuccess')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onbackgroundfetchsuccess -> get attr')

    def set_onbackgroundfetchsuccess(self, val):
        self._attr['onbackgroundfetchsuccess'] = val

    def get_onbackgroundfetchfail(self):
        val = self._attr.get('onbackgroundfetchfail')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onbackgroundfetchfail -> get attr')

    def set_onbackgroundfetchfail(self, val):
        self._attr['onbackgroundfetchfail'] = val

    def get_onbackgroundfetchabort(self):
        val = self._attr.get('onbackgroundfetchabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onbackgroundfetchabort -> get attr')

    def set_onbackgroundfetchabort(self, val):
        self._attr['onbackgroundfetchabort'] = val

    def get_onbackgroundfetchclick(self):
        val = self._attr.get('onbackgroundfetchclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onbackgroundfetchclick -> get attr')

    def set_onbackgroundfetchclick(self, val):
        self._attr['onbackgroundfetchclick'] = val

    def get_onperiodicsync(self):
        val = self._attr.get('onperiodicsync')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onperiodicsync -> get attr')

    def set_onperiodicsync(self, val):
        self._attr['onperiodicsync'] = val

    def get_oncontentdelete(self):
        val = self._attr.get('oncontentdelete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.oncontentdelete -> get attr')

    def set_oncontentdelete(self, val):
        self._attr['oncontentdelete'] = val

    def get_onnotificationclick(self):
        val = self._attr.get('onnotificationclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onnotificationclick -> get attr')

    def set_onnotificationclick(self, val):
        self._attr['onnotificationclick'] = val

    def get_onnotificationclose(self):
        val = self._attr.get('onnotificationclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onnotificationclose -> get attr')

    def set_onnotificationclose(self, val):
        self._attr['onnotificationclose'] = val

    def get_onabortpayment(self):
        val = self._attr.get('onabortpayment')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onabortpayment -> get attr')

    def set_onabortpayment(self, val):
        self._attr['onabortpayment'] = val

    def get_oncanmakepayment(self):
        val = self._attr.get('oncanmakepayment')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.oncanmakepayment -> get attr')

    def set_oncanmakepayment(self, val):
        self._attr['oncanmakepayment'] = val

    def get_onpaymentrequest(self):
        val = self._attr.get('onpaymentrequest')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onpaymentrequest -> get attr')

    def set_onpaymentrequest(self, val):
        self._attr['onpaymentrequest'] = val

    def get_onpush(self):
        val = self._attr.get('onpush')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onpush -> get attr')

    def set_onpush(self, val):
        self._attr['onpush'] = val

    def get_onpushsubscriptionchange(self):
        val = self._attr.get('onpushsubscriptionchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.onpushsubscriptionchange -> get attr')

    def set_onpushsubscriptionchange(self, val):
        self._attr['onpushsubscriptionchange'] = val

    def fn_skipWaiting(self, *args):
        logger.debug(f'patch -> v8_service_worker_global_scope.py -> ServiceWorkerGlobalScope.skipWaiting{tuple(args)} -> method')
