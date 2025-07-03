from .flags import *


@construct_100001
class BluetoothRemoteGATTServer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("device", "get_device", None, 0, 1, 0, 0, 0, 0, 1),
        ("connected", "get_connected", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("connect", "fn_connect", 0, 0, 1, 0, 1, 0, 0),
        ("disconnect", "fn_disconnect", 0, 0, 1, 0, 0, 0, 0),
        ("getPrimaryService", "fn_getPrimaryService", 1, 0, 1, 0, 1, 0, 0),
        ("getPrimaryServices", "fn_getPrimaryServices", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_device(self):
        val = self._attr.get('device')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_server.py -> BluetoothRemoteGATTServer.device -> get attr')

    def get_connected(self):
        val = self._attr.get('connected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_server.py -> BluetoothRemoteGATTServer.connected -> get attr')

    def fn_connect(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_server.py -> BluetoothRemoteGATTServer.connect{tuple(args)} -> method')

    def fn_disconnect(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_server.py -> BluetoothRemoteGATTServer.disconnect{tuple(args)} -> method')

    def fn_getPrimaryService(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_server.py -> BluetoothRemoteGATTServer.getPrimaryService{tuple(args)} -> method')

    def fn_getPrimaryServices(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_server.py -> BluetoothRemoteGATTServer.getPrimaryServices{tuple(args)} -> method')
