from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class ServiceWorkerContainer(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ServiceWorkerContainer, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("controller", "get_controller", None, 0, 1, 0, 0, 0, 0, 1),
        ("ready", "get_ready", None, 0, 1, 0, 1, 0, 0, 1),
        ("oncontrollerchange", "get_oncontrollerchange", "set_oncontrollerchange", 0, 1, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),
        ("onmessageerror", "get_onmessageerror", "set_onmessageerror", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getRegistration", "fn_getRegistration", 0, 0, 1, 0, 1, 0, 0),
        ("getRegistrations", "fn_getRegistrations", 0, 0, 1, 0, 1, 0, 0),
        ("register", "fn_register", 1, 0, 1, 0, 1, 0, 0),
        ("startMessages", "fn_startMessages", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_controller(self):
        val = self._attr.get('controller')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.controller -> get attr')

    def get_ready(self):
        val = self._attr.get('ready')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.ready -> get attr')

    def get_oncontrollerchange(self):
        val = self._attr.get('oncontrollerchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.oncontrollerchange -> get attr')

    def set_oncontrollerchange(self, val):
        self._attr['oncontrollerchange'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onmessageerror(self):
        val = self._attr.get('onmessageerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.onmessageerror -> get attr')

    def set_onmessageerror(self, val):
        self._attr['onmessageerror'] = val

    def fn_getRegistration(self, *args):
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.getRegistration{tuple(args)} -> method')

    def fn_getRegistrations(self, *args):
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.getRegistrations{tuple(args)} -> method')

    def fn_register(self, *args):
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.register{tuple(args)} -> method')

    def fn_startMessages(self, *args):
        logger.debug(f'patch -> v8_service_worker_container.py -> ServiceWorkerContainer.startMessages{tuple(args)} -> method')
