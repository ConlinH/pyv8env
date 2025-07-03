from .flags import *


@construct_000000
class SQLError:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    UNKNOWN_ERR = 0
    DATABASE_ERR = 1
    VERSION_ERR = 2
    TOO_LARGE_ERR = 3
    QUOTA_ERR = 4
    SYNTAX_ERR = 5
    CONSTRAINT_ERR = 6
    TIMEOUT_ERR = 7

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("code", "get_code", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_code(self):
        val = self._attr.get('code')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sql_error.py -> SQLError.code -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sql_error.py -> SQLError.message -> get attr')
