from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class ServiceWorkerRegistration(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ServiceWorkerRegistration, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("installing", "get_installing", None, 0, 1, 0, 0, 0, 0, 1),
        ("waiting", "get_waiting", None, 0, 1, 0, 0, 0, 0, 1),
        ("active", "get_active", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigationPreload", "get_navigationPreload", None, 0, 1, 0, 0, 0, 0, 1),
        ("scope", "get_scope", None, 0, 1, 0, 0, 0, 0, 1),
        ("updateViaCache", "get_updateViaCache", None, 0, 1, 0, 0, 0, 0, 1),
        ("onupdatefound", "get_onupdatefound", "set_onupdatefound", 0, 1, 0, 0, 0, 0, 1),
        ("paymentManager", "get_paymentManager", None, 0, 1, 0, 0, 0, 0, 1),
        ("backgroundFetch", "get_backgroundFetch", None, 0, 1, 0, 0, 0, 0, 1),
        ("periodicSync", "get_periodicSync", None, 0, 1, 0, 0, 0, 0, 1),
        ("sync", "get_sync", None, 0, 1, 0, 0, 0, 0, 1),
        ("index", "get_index", None, 0, 1, 0, 0, 0, 0, 1),
        ("cookies", "get_cookies", None, 0, 1, 0, 0, 0, 0, 1),
        ("pushManager", "get_pushManager", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("unregister", "fn_unregister", 0, 0, 1, 0, 1, 0, 0),
        ("update", "fn_update", 0, 0, 1, 0, 1, 0, 0),
        ("getNotifications", "fn_getNotifications", 0, 0, 1, 0, 1, 0, 0),
        ("showNotification", "fn_showNotification", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_installing(self):
        val = self._attr.get('installing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.installing -> get attr')

    def get_waiting(self):
        val = self._attr.get('waiting')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.waiting -> get attr')

    def get_active(self):
        val = self._attr.get('active')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.active -> get attr')

    def get_navigationPreload(self):
        val = self._attr.get('navigationPreload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.navigationPreload -> get attr')

    def get_scope(self):
        val = self._attr.get('scope')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.scope -> get attr')

    def get_updateViaCache(self):
        val = self._attr.get('updateViaCache')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.updateViaCache -> get attr')

    def get_onupdatefound(self):
        val = self._attr.get('onupdatefound')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.onupdatefound -> get attr')

    def set_onupdatefound(self, val):
        self._attr['onupdatefound'] = val

    def get_paymentManager(self):
        val = self._attr.get('paymentManager')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.paymentManager -> get attr')

    def get_backgroundFetch(self):
        val = self._attr.get('backgroundFetch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.backgroundFetch -> get attr')

    def get_periodicSync(self):
        val = self._attr.get('periodicSync')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.periodicSync -> get attr')

    def get_sync(self):
        val = self._attr.get('sync')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.sync -> get attr')

    def get_index(self):
        val = self._attr.get('index')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.index -> get attr')

    def get_cookies(self):
        val = self._attr.get('cookies')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.cookies -> get attr')

    def get_pushManager(self):
        val = self._attr.get('pushManager')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.pushManager -> get attr')

    def fn_unregister(self, *args):
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.unregister{tuple(args)} -> method')

    def fn_update(self, *args):
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.update{tuple(args)} -> method')

    def fn_getNotifications(self, *args):
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.getNotifications{tuple(args)} -> method')

    def fn_showNotification(self, *args):
        logger.debug(f'patch -> v8_service_worker_registration.py -> ServiceWorkerRegistration.showNotification{tuple(args)} -> method')
