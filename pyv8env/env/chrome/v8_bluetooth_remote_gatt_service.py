from .flags import *


@construct_100001
class BluetoothRemoteGATTService:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("device", "get_device", None, 0, 1, 0, 0, 0, 0, 1),
        ("uuid", "get_uuid", None, 0, 1, 0, 0, 0, 0, 1),
        ("isPrimary", "get_isPrimary", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getCharacteristic", "fn_getCharacteristic", 1, 0, 1, 0, 1, 0, 0),
        ("getCharacteristics", "fn_getCharacteristics", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_device(self):
        val = self._attr.get('device')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_service.py -> BluetoothRemoteGATTService.device -> get attr')

    def get_uuid(self):
        val = self._attr.get('uuid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_service.py -> BluetoothRemoteGATTService.uuid -> get attr')

    def get_isPrimary(self):
        val = self._attr.get('isPrimary')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_service.py -> BluetoothRemoteGATTService.isPrimary -> get attr')

    def fn_getCharacteristic(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_service.py -> BluetoothRemoteGATTService.getCharacteristic{tuple(args)} -> method')

    def fn_getCharacteristics(self, *args):
        logger.debug(f'patch -> v8_bluetooth_remote_gatt_service.py -> BluetoothRemoteGATTService.getCharacteristics{tuple(args)} -> method')
