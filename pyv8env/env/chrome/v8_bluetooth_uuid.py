from .flags import *


@construct_100001
class BluetoothUUID:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("canonicalUUID", "fn_canonicalUUID", 1, 0, 2, 0, 1, 1, 0),
        ("getCharacteristic", "fn_getCharacteristic", 1, 0, 2, 0, 1, 1, 0),
        ("getDescriptor", "fn_getDescriptor", 1, 0, 2, 0, 1, 1, 0),
        ("getService", "fn_getService", 1, 0, 2, 0, 1, 1, 0),

    )

    @classmethod
    def fn_canonicalUUID(cls, *args):
        logger.debug(f'patch -> v8_bluetooth_uuid.py -> BluetoothUUID.canonicalUUID{tuple(args)} -> method')

    @classmethod
    def fn_getCharacteristic(cls, *args):
        logger.debug(f'patch -> v8_bluetooth_uuid.py -> BluetoothUUID.getCharacteristic{tuple(args)} -> method')

    @classmethod
    def fn_getDescriptor(cls, *args):
        logger.debug(f'patch -> v8_bluetooth_uuid.py -> BluetoothUUID.getDescriptor{tuple(args)} -> method')

    @classmethod
    def fn_getService(cls, *args):
        logger.debug(f'patch -> v8_bluetooth_uuid.py -> BluetoothUUID.getService{tuple(args)} -> method')
