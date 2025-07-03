from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class BluetoothDevice(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BluetoothDevice, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("gatt", "get_gatt", None, 0, 1, 0, 0, 0, 0, 1),
        ("ongattserverdisconnected", "get_ongattserverdisconnected", "set_ongattserverdisconnected", 0, 1, 0, 0, 0, 0, 1),
        ("watchingAdvertisements", "get_watchingAdvertisements", None, 0, 1, 0, 0, 0, 0, 1),
        ("onadvertisementreceived", "get_onadvertisementreceived", "set_onadvertisementreceived", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("forget", "fn_forget", 0, 0, 1, 0, 1, 0, 0),
        ("watchAdvertisements", "fn_watchAdvertisements", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.id -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.name -> get attr')

    def get_gatt(self):
        val = self._attr.get('gatt')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.gatt -> get attr')

    def get_ongattserverdisconnected(self):
        val = self._attr.get('ongattserverdisconnected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.ongattserverdisconnected -> get attr')

    def set_ongattserverdisconnected(self, val):
        self._attr['ongattserverdisconnected'] = val

    def get_watchingAdvertisements(self):
        val = self._attr.get('watchingAdvertisements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.watchingAdvertisements -> get attr')

    def get_onadvertisementreceived(self):
        val = self._attr.get('onadvertisementreceived')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.onadvertisementreceived -> get attr')

    def set_onadvertisementreceived(self, val):
        self._attr['onadvertisementreceived'] = val

    def fn_forget(self, *args):
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.forget{tuple(args)} -> method')

    def fn_watchAdvertisements(self, *args):
        logger.debug(f'patch -> v8_bluetooth_device.py -> BluetoothDevice.watchAdvertisements{tuple(args)} -> method')
