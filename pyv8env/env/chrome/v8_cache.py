from .flags import *


@construct_100001
class Cache:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 1, 0, 0),
        ("addAll", "fn_addAll", 1, 0, 1, 0, 1, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 1, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 1, 0, 0),
        ("match", "fn_match", 1, 0, 1, 0, 1, 0, 0),
        ("matchAll", "fn_matchAll", 0, 0, 1, 0, 1, 0, 0),
        ("put", "fn_put", 2, 0, 1, 0, 1, 0, 0),

    )

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_cache.py -> Cache.add{tuple(args)} -> method')

    def fn_addAll(self, *args):
        logger.debug(f'patch -> v8_cache.py -> Cache.addAll{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_cache.py -> Cache.delete{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_cache.py -> Cache.keys{tuple(args)} -> method')

    def fn_match(self, *args):
        logger.debug(f'patch -> v8_cache.py -> Cache.match{tuple(args)} -> method')

    def fn_matchAll(self, *args):
        logger.debug(f'patch -> v8_cache.py -> Cache.matchAll{tuple(args)} -> method')

    def fn_put(self, *args):
        logger.debug(f'patch -> v8_cache.py -> Cache.put{tuple(args)} -> method')
