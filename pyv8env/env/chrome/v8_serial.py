from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Serial(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Serial, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onconnect", "get_onconnect", "set_onconnect", 0, 1, 0, 0, 0, 0, 1),
        ("ondisconnect", "get_ondisconnect", "set_ondisconnect", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPorts", "fn_getPorts", 0, 0, 1, 0, 1, 0, 0),
        ("requestPort", "fn_requestPort", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_onconnect(self):
        val = self._attr.get('onconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_serial.py -> Serial.onconnect -> get attr')

    def set_onconnect(self, val):
        self._attr['onconnect'] = val

    def get_ondisconnect(self):
        val = self._attr.get('ondisconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_serial.py -> Serial.ondisconnect -> get attr')

    def set_ondisconnect(self, val):
        self._attr['ondisconnect'] = val

    def fn_getPorts(self, *args):
        logger.debug(f'patch -> v8_serial.py -> Serial.getPorts{tuple(args)} -> method')

    def fn_requestPort(self, *args):
        logger.debug(f'patch -> v8_serial.py -> Serial.requestPort{tuple(args)} -> method')
