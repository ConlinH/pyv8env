from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class BluetoothRemoteGATTCharacteristic(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BluetoothRemoteGATTCharacteristic, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("service", "get_service", None, 0, 1, 0, 0, 0, 0, 1),
        ("uuid", "get_uuid", None, 0, 1, 0, 0, 0, 0, 1),
        ("properties", "get_properties", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", None, 0, 1, 0, 0, 0, 0, 1),
        ("oncharacteristicvaluechanged", "get_oncharacteristicvaluechanged", "set_oncharacteristicvaluechanged", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getDescriptor", "fn_getDescriptor", 1, 0, 1, 0, 1, 0, 0),
        ("getDescriptors", "fn_getDescriptors", 0, 0, 1, 0, 1, 0, 0),
        ("readValue", "fn_readValue", 0, 0, 1, 0, 1, 0, 0),
        ("startNotifications", "fn_startNotifications", 0, 0, 1, 0, 1, 0, 0),
        ("stopNotifications", "fn_stopNotifications", 0, 0, 1, 0, 1, 0, 0),
        ("writeValue", "fn_writeValue", 1, 0, 1, 0, 1, 0, 0),
        ("writeValueWithResponse", "fn_writeValueWithResponse", 1, 0, 1, 0, 1, 0, 0),
        ("writeValueWithoutResponse", "fn_writeValueWithoutResponse", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_service(self):
        val = self._attr.get('service')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.service -> get attr')

    def get_uuid(self):
        val = self._attr.get('uuid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.uuid -> get attr')

    def get_properties(self):
        val = self._attr.get('properties')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.properties -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.value -> get attr')

    def get_oncharacteristicvaluechanged(self):
        val = self._attr.get('oncharacteristicvaluechanged')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.oncharacteristicvaluechanged -> get attr')

    def set_oncharacteristicvaluechanged(self, val):
        self._attr['oncharacteristicvaluechanged'] = val

    def fn_getDescriptor(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.getDescriptor{tuple(args)} -> method')

    def fn_getDescriptors(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.getDescriptors{tuple(args)} -> method')

    def fn_readValue(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.readValue{tuple(args)} -> method')

    def fn_startNotifications(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.startNotifications{tuple(args)} -> method')

    def fn_stopNotifications(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.stopNotifications{tuple(args)} -> method')

    def fn_writeValue(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.writeValue{tuple(args)} -> method')

    def fn_writeValueWithResponse(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.writeValueWithResponse{tuple(args)} -> method')

    def fn_writeValueWithoutResponse(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_characteristic.py -> BluetoothRemoteGATTCharacteristic.writeValueWithoutResponse{tuple(args)} -> method')
