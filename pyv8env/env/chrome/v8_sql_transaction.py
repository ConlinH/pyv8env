from .flags import *


@construct_000000
class SQLTransaction:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("executeSql", "fn_executeSql", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_executeSql(self, *args):
        logger.debug(f'patch -> v8_sql_transaction.py -> SQLTransaction.executeSql{tuple(args)} -> method')
