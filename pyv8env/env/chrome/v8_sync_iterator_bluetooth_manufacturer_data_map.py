from .flags import *


@construct_000000
class SyncIterator_BluetoothManufacturerDataMap:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("next", "fn_next", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_next(self, *args):
        logger.debug(f'patch -> v8_sync_iterator_bluetooth_manufacturer_data_map.py -> SyncIterator_BluetoothManufacturerDataMap.next{tuple(args)} -> method')
