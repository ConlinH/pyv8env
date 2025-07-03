from .flags import *


@construct_100001
class SharedStorageWorklet:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addModule", "fn_addModule", 1, 0, 1, 0, 1, 0, 0),
        ("run", "fn_run", 1, 0, 1, 0, 1, 0, 0),
        ("selectURL", "fn_selectURL", 2, 0, 1, 0, 1, 0, 0),

    )

    def fn_addModule(self, *args):
        logger.debug(f'patch -> v8_shared_storage_worklet.py -> SharedStorageWorklet.addModule{tuple(args)} -> method')

    def fn_run(self, *args):
        logger.debug(f'patch -> v8_shared_storage_worklet.py -> SharedStorageWorklet.run{tuple(args)} -> method')

    def fn_selectURL(self, *args):
        logger.debug(f'patch -> v8_shared_storage_worklet.py -> SharedStorageWorklet.selectURL{tuple(args)} -> method')
