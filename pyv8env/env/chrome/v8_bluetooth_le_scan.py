from .flags import *


@construct_100001
class BluetoothLEScan:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("filters", "get_filters", None, 0, 1, 0, 0, 0, 0, 1),
        ("keepRepeatedDevices", "get_keepRepeatedDevices", None, 0, 1, 0, 0, 0, 0, 1),
        ("acceptAllAdvertisements", "get_acceptAllAdvertisements", None, 0, 1, 0, 0, 0, 0, 1),
        ("active", "get_active", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_filters(self):
        val = self._attr.get('filters')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_le_scan.py -> BluetoothLEScan.filters -> get attr')

    def get_keepRepeatedDevices(self):
        val = self._attr.get('keepRepeatedDevices')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_le_scan.py -> BluetoothLEScan.keepRepeatedDevices -> get attr')

    def get_acceptAllAdvertisements(self):
        val = self._attr.get('acceptAllAdvertisements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_le_scan.py -> BluetoothLEScan.acceptAllAdvertisements -> get attr')

    def get_active(self):
        val = self._attr.get('active')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_le_scan.py -> BluetoothLEScan.active -> get attr')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_bluetooth_le_scan.py -> BluetoothLEScan.stop{tuple(args)} -> method')
