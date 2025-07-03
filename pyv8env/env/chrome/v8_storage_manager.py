from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class StorageManager(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(StorageManager, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onquotachange", "get_onquotachange", "set_onquotachange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("estimate", "fn_estimate", 0, 0, 1, 0, 1, 0, 0),
        ("persisted", "fn_persisted", 0, 0, 1, 0, 1, 0, 0),
        ("getDirectory", "fn_getDirectory", 0, 0, 1, 0, 1, 0, 0),
        ("persist", "fn_persist", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_onquotachange(self):
        val = self._attr.get('onquotachange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage_manager.py -> StorageManager.onquotachange -> get attr')

    def set_onquotachange(self, val):
        self._attr['onquotachange'] = val

    def fn_estimate(self, *args):
        logger.debug(f'patch -> v8_storage_manager.py -> StorageManager.estimate{tuple(args)} -> method')

    def fn_persisted(self, *args):
        logger.debug(f'patch -> v8_storage_manager.py -> StorageManager.persisted{tuple(args)} -> method')

    def fn_getDirectory(self, *args):
        logger.debug(f'patch -> v8_storage_manager.py -> StorageManager.getDirectory{tuple(args)} -> method')

    def fn_persist(self, *args):
        logger.debug(f'patch -> v8_storage_manager.py -> StorageManager.persist{tuple(args)} -> method')
