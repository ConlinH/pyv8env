from .flags import *


@construct_100001
class BluetoothRemoteGATTDescriptor:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("characteristic", "get_characteristic", None, 0, 1, 0, 0, 0, 0, 1),
        ("uuid", "get_uuid", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("readValue", "fn_readValue", 0, 0, 1, 0, 1, 0, 0),
        ("writeValue", "fn_writeValue", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_characteristic(self):
        val = self._attr.get('characteristic')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_descriptor.py -> BluetoothRemoteGATTDescriptor.characteristic -> get attr')

    def get_uuid(self):
        val = self._attr.get('uuid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_descriptor.py -> BluetoothRemoteGATTDescriptor.uuid -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_descriptor.py -> BluetoothRemoteGATTDescriptor.value -> get attr')

    def fn_readValue(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_descriptor.py -> BluetoothRemoteGATTDescriptor.readValue{tuple(args)} -> method')

    def fn_writeValue(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_descriptor.py -> BluetoothRemoteGATTDescriptor.writeValue{tuple(args)} -> method')
