from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class Worker(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Worker, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("postMessage", "fn_postMessage", 1, 0, 1, 0, 0, 0, 0),
        ("terminate", "fn_terminate", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker.py -> Worker.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worker.py -> Worker.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def fn_postMessage(self, *args):
        logger.debug(f'patch -> v8_worker.py -> Worker.postMessage{tuple(args)} -> method')

    def fn_terminate(self, *args):
        logger.debug(f'patch -> v8_worker.py -> Worker.terminate{tuple(args)} -> method')
