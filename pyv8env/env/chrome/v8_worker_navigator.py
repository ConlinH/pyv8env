from .flags import *


@construct_100001
class WorkerNavigator:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("hardwareConcurrency", "get_hardwareConcurrency", None, 0, 1, 0, 0, 0, 0, 1),
        ("appCodeName", "get_appCodeName", None, 0, 1, 0, 0, 0, 0, 1),
        ("appName", "get_appName", None, 0, 1, 0, 0, 0, 0, 1),
        ("appVersion", "get_appVersion", None, 0, 1, 0, 0, 0, 0, 1),
        ("platform", "get_platform", None, 0, 1, 0, 0, 0, 0, 1),
        ("product", "get_product", None, 0, 1, 0, 0, 0, 0, 1),
        ("userAgent", "get_userAgent", None, 0, 1, 0, 0, 0, 0, 1),
        ("language", "get_language", None, 0, 1, 0, 0, 0, 0, 1),
        ("languages", "get_languages", None, 0, 1, 0, 0, 0, 0, 1),
        ("onLine", "get_onLine", None, 0, 1, 0, 0, 0, 0, 1),
        ("storageBuckets", "get_storageBuckets", None, 0, 1, 0, 0, 0, 0, 1),
        ("hid", "get_hid", None, 0, 1, 0, 0, 0, 0, 1),
        ("locks", "get_locks", None, 0, 1, 0, 0, 0, 0, 1),
        ("gpu", "get_gpu", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCapabilities", "get_mediaCapabilities", None, 0, 1, 0, 0, 0, 0, 1),
        ("connection", "get_connection", None, 0, 1, 0, 0, 0, 0, 1),
        ("ml", "get_ml", None, 0, 1, 0, 0, 0, 0, 1),
        ("permissions", "get_permissions", None, 0, 1, 0, 0, 0, 0, 1),
        ("storage", "get_storage", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceMemory", "get_deviceMemory", None, 0, 1, 0, 0, 0, 0, 1),
        ("userAgentData", "get_userAgentData", None, 0, 1, 0, 0, 0, 0, 1),
        ("wakeLock", "get_wakeLock", None, 0, 1, 0, 0, 0, 0, 1),
        ("usb", "get_usb", None, 0, 1, 0, 0, 0, 0, 1),
        ("serial", "get_serial", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clearAppBadge", "fn_clearAppBadge", 0, 0, 1, 0, 1, 0, 0),
        ("setAppBadge", "fn_setAppBadge", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_hardwareConcurrency(self):
        val = self._attr.get('hardwareConcurrency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.hardwareConcurrency -> get attr')

    def get_appCodeName(self):
        val = self._attr.get('appCodeName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.appCodeName -> get attr')

    def get_appName(self):
        val = self._attr.get('appName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.appName -> get attr')

    def get_appVersion(self):
        val = self._attr.get('appVersion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.appVersion -> get attr')

    def get_platform(self):
        val = self._attr.get('platform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.platform -> get attr')

    def get_product(self):
        val = self._attr.get('product')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.product -> get attr')

    def get_userAgent(self):
        val = self._attr.get('userAgent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.userAgent -> get attr')

    def get_language(self):
        val = self._attr.get('language')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.language -> get attr')

    def get_languages(self):
        val = self._attr.get('languages')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.languages -> get attr')

    def get_onLine(self):
        val = self._attr.get('onLine')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.onLine -> get attr')

    def get_storageBuckets(self):
        val = self._attr.get('storageBuckets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.storageBuckets -> get attr')

    def get_hid(self):
        val = self._attr.get('hid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.hid -> get attr')

    def get_locks(self):
        val = self._attr.get('locks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.locks -> get attr')

    def get_gpu(self):
        val = self._attr.get('gpu')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.gpu -> get attr')

    def get_mediaCapabilities(self):
        val = self._attr.get('mediaCapabilities')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.mediaCapabilities -> get attr')

    def get_connection(self):
        val = self._attr.get('connection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.connection -> get attr')

    def get_ml(self):
        val = self._attr.get('ml')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.ml -> get attr')

    def get_permissions(self):
        val = self._attr.get('permissions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.permissions -> get attr')

    def get_storage(self):
        val = self._attr.get('storage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.storage -> get attr')

    def get_deviceMemory(self):
        val = self._attr.get('deviceMemory')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.deviceMemory -> get attr')

    def get_userAgentData(self):
        val = self._attr.get('userAgentData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.userAgentData -> get attr')

    def get_wakeLock(self):
        val = self._attr.get('wakeLock')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.wakeLock -> get attr')

    def get_usb(self):
        val = self._attr.get('usb')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.usb -> get attr')

    def get_serial(self):
        val = self._attr.get('serial')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.serial -> get attr')

    def fn_clearAppBadge(self, *args):
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.clearAppBadge{tuple(args)} -> method')

    def fn_setAppBadge(self, *args):
        logger.debug(f'patch -> v8_worker_navigator.py -> WorkerNavigator.setAppBadge{tuple(args)} -> method')
