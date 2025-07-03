from .flags import *


@construct_100001
class BluetoothCharacteristicProperties:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("broadcast", "get_broadcast", None, 0, 1, 0, 0, 0, 0, 1),
        ("read", "get_read", None, 0, 1, 0, 0, 0, 0, 1),
        ("writeWithoutResponse", "get_writeWithoutResponse", None, 0, 1, 0, 0, 0, 0, 1),
        ("write", "get_write", None, 0, 1, 0, 0, 0, 0, 1),
        ("notify", "get_notify", None, 0, 1, 0, 0, 0, 0, 1),
        ("indicate", "get_indicate", None, 0, 1, 0, 0, 0, 0, 1),
        ("authenticatedSignedWrites", "get_authenticatedSignedWrites", None, 0, 1, 0, 0, 0, 0, 1),
        ("reliableWrite", "get_reliableWrite", None, 0, 1, 0, 0, 0, 0, 1),
        ("writableAuxiliaries", "get_writableAuxiliaries", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_broadcast(self):
        val = self._attr.get('broadcast')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.broadcast -> get attr')

    def get_read(self):
        val = self._attr.get('read')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.read -> get attr')

    def get_writeWithoutResponse(self):
        val = self._attr.get('writeWithoutResponse')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.writeWithoutResponse -> get attr')

    def get_write(self):
        val = self._attr.get('write')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.write -> get attr')

    def get_notify(self):
        val = self._attr.get('notify')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.notify -> get attr')

    def get_indicate(self):
        val = self._attr.get('indicate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.indicate -> get attr')

    def get_authenticatedSignedWrites(self):
        val = self._attr.get('authenticatedSignedWrites')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.authenticatedSignedWrites -> get attr')

    def get_reliableWrite(self):
        val = self._attr.get('reliableWrite')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.reliableWrite -> get attr')

    def get_writableAuxiliaries(self):
        val = self._attr.get('writableAuxiliaries')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_characteristic_properties.py -> BluetoothCharacteristicProperties.writableAuxiliaries -> get attr')
