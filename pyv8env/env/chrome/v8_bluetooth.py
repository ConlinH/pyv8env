from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Bluetooth(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Bluetooth, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onadvertisementreceived", "get_onadvertisementreceived", "set_onadvertisementreceived", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getAvailability", "fn_getAvailability", 0, 0, 1, 0, 1, 0, 0),
        ("requestDevice", "fn_requestDevice", 0, 0, 1, 0, 1, 0, 0),
        ("getDevices", "fn_getDevices", 0, 0, 1, 0, 1, 0, 0),
        ("requestLEScan", "fn_requestLEScan", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_onadvertisementreceived(self):
        val = self._attr.get('onadvertisementreceived')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth.py -> Bluetooth.onadvertisementreceived -> get attr')

    def set_onadvertisementreceived(self, val):
        self._attr['onadvertisementreceived'] = val

    def fn_getAvailability(self, *args):
        logger.debug(f'patch -> v8_bluetooth.py -> Bluetooth.getAvailability{tuple(args)} -> method')

    def fn_requestDevice(self, *args):
        logger.debug(f'patch -> v8_bluetooth.py -> Bluetooth.requestDevice{tuple(args)} -> method')

    def fn_getDevices(self, *args):
        logger.debug(f'patch -> v8_bluetooth.py -> Bluetooth.getDevices{tuple(args)} -> method')

    def fn_requestLEScan(self, *args):
        logger.debug(f'patch -> v8_bluetooth.py -> Bluetooth.requestLEScan{tuple(args)} -> method')
