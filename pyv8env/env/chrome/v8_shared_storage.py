from .flags import *


@construct_100001
class SharedStorage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("context", "get_context", None, 0, 1, 0, 0, 0, 0, 1),
        ("worklet", "get_worklet", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("append", "fn_append", 2, 0, 1, 0, 1, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 1, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 1, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 1, 0, 0),
        ("set", "fn_set", 2, 0, 1, 0, 1, 0, 0),
        ("createWorklet", "fn_createWorklet", 1, 0, 1, 0, 1, 0, 0),
        ("length", "fn_length", 0, 0, 1, 0, 1, 0, 0),
        ("remainingBudget", "fn_remainingBudget", 0, 0, 1, 0, 1, 0, 0),
        ("entries", "fn_entries", 0, 0, 1, 0, 0, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 0, 0, 0),
        ("values", "fn_values", 0, 0, 1, 0, 0, 0, 0),
        ("run", "fn_run", 1, 0, 1, 0, 1, 0, 0),
        ("selectURL", "fn_selectURL", 2, 0, 1, 0, 1, 0, 0),

    )

    def get_context(self):
        val = self._attr.get('context')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.context -> get attr')

    def get_worklet(self):
        val = self._attr.get('worklet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.worklet -> get attr')

    def fn_append(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.append{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.clear{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.delete{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.get{tuple(args)} -> method')

    def fn_set(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.set{tuple(args)} -> method')

    def fn_createWorklet(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.createWorklet{tuple(args)} -> method')

    def fn_length(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.length{tuple(args)} -> method')

    def fn_remainingBudget(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.remainingBudget{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.entries{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.keys{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.values{tuple(args)} -> method')

    def fn_run(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.run{tuple(args)} -> method')

    def fn_selectURL(self, *args):
        logger.debug(f'patch -> v8_shared_storage.py -> SharedStorage.selectURL{tuple(args)} -> method')
