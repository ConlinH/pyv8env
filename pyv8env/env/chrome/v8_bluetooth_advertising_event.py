from .flags import *
from .v8_event import Event


@construct_100001
class BluetoothAdvertisingEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BluetoothAdvertisingEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("device", "get_device", None, 0, 1, 0, 0, 0, 0, 1),
        ("uuids", "get_uuids", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("appearance", "get_appearance", None, 0, 1, 0, 0, 0, 0, 1),
        ("txPower", "get_txPower", None, 0, 1, 0, 0, 0, 0, 1),
        ("rssi", "get_rssi", None, 0, 1, 0, 0, 0, 0, 1),
        ("manufacturerData", "get_manufacturerData", None, 0, 1, 0, 0, 0, 0, 1),
        ("serviceData", "get_serviceData", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_device(self):
        val = self._attr.get('device')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.device -> get attr')

    def get_uuids(self):
        val = self._attr.get('uuids')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.uuids -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.name -> get attr')

    def get_appearance(self):
        val = self._attr.get('appearance')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.appearance -> get attr')

    def get_txPower(self):
        val = self._attr.get('txPower')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.txPower -> get attr')

    def get_rssi(self):
        val = self._attr.get('rssi')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.rssi -> get attr')

    def get_manufacturerData(self):
        val = self._attr.get('manufacturerData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.manufacturerData -> get attr')

    def get_serviceData(self):
        val = self._attr.get('serviceData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.serviceData -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bluetooth_advertising_event.py -> BluetoothAdvertisingEvent.isTrusted -> get attr')
