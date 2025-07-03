from .flags import *
from .v8_event import Event


@construct_111001
class StorageEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(StorageEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("key", "get_key", None, 0, 1, 0, 0, 0, 0, 1),
        ("oldValue", "get_oldValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("newValue", "get_newValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("storageArea", "get_storageArea", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("initStorageEvent", "fn_initStorageEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_key(self):
        val = self._attr.get('key')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_event.py -> StorageEvent.key -> get attr')

    def get_oldValue(self):
        val = self._attr.get('oldValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_event.py -> StorageEvent.oldValue -> get attr')

    def get_newValue(self):
        val = self._attr.get('newValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_event.py -> StorageEvent.newValue -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_event.py -> StorageEvent.url -> get attr')

    def get_storageArea(self):
        val = self._attr.get('storageArea')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_event.py -> StorageEvent.storageArea -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_event.py -> StorageEvent.isTrusted -> get attr')

    def fn_initStorageEvent(self, *args):
        logger.debug(f'patch -> v8_storage_event.py -> StorageEvent.initStorageEvent{tuple(args)} -> method')
