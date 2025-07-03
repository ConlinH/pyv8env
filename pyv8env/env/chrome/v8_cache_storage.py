from .flags import *


@construct_100001
class CacheStorage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("delete", "fn_delete", 1, 0, 1, 0, 1, 0, 0),
        ("has", "fn_has", 1, 0, 1, 0, 1, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 1, 0, 0),
        ("match", "fn_match", 1, 0, 1, 0, 1, 0, 0),
        ("open", "fn_open", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_cache_storage.py -> CacheStorage.delete{tuple(args)} -> method')

    def fn_has(self, *args):
        logger.debug(f'patch -> v8_cache_storage.py -> CacheStorage.has{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_cache_storage.py -> CacheStorage.keys{tuple(args)} -> method')

    def fn_match(self, *args):
        logger.debug(f'patch -> v8_cache_storage.py -> CacheStorage.match{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_cache_storage.py -> CacheStorage.open{tuple(args)} -> method')
