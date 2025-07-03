from .flags import *


@construct_100001
class IDBFactory:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cmp", "fn_cmp", 2, 0, 1, 0, 0, 0, 0),
        ("databases", "fn_databases", 0, 0, 1, 0, 1, 0, 0),
        ("deleteDatabase", "fn_deleteDatabase", 1, 0, 1, 0, 0, 0, 0),
        ("open", "fn_open", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_cmp(self, *args):
        logger.debug(f'patch -> v8_idb_factory.py -> IDBFactory.cmp{tuple(args)} -> method')

    def fn_databases(self, *args):
        logger.debug(f'patch -> v8_idb_factory.py -> IDBFactory.databases{tuple(args)} -> method')

    def fn_deleteDatabase(self, *args):
        logger.debug(f'patch -> v8_idb_factory.py -> IDBFactory.deleteDatabase{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_idb_factory.py -> IDBFactory.open{tuple(args)} -> method')
