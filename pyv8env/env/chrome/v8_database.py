from .flags import *


@construct_000000
class Database:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("version", "get_version", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("changeVersion", "fn_changeVersion", 2, 0, 1, 0, 0, 0, 0),
        ("readTransaction", "fn_readTransaction", 1, 0, 1, 0, 0, 0, 0),
        ("transaction", "fn_transaction", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_version(self):
        val = self._attr.get('version')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_database.py -> Database.version -> get attr')

    def fn_changeVersion(self, *args):
        logger.debug(f'patch -> v8_database.py -> Database.changeVersion{tuple(args)} -> method')

    def fn_readTransaction(self, *args):
        logger.debug(f'patch -> v8_database.py -> Database.readTransaction{tuple(args)} -> method')

    def fn_transaction(self, *args):
        logger.debug(f'patch -> v8_database.py -> Database.transaction{tuple(args)} -> method')
