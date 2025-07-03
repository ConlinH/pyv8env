from .flags import *


@construct_100001
class StorageBucketManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("delete", "fn_delete", 1, 0, 1, 0, 1, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 1, 0, 0),
        ("open", "fn_open", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_storage_bucket_manager.py -> StorageBucketManager.delete{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_storage_bucket_manager.py -> StorageBucketManager.keys{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_storage_bucket_manager.py -> StorageBucketManager.open{tuple(args)} -> method')
