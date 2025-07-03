from .flags import *


@construct_000000
class SQLResultSet:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rows", "get_rows", None, 0, 1, 0, 0, 0, 0, 1),
        ("insertId", "get_insertId", None, 0, 1, 0, 0, 0, 0, 1),
        ("rowsAffected", "get_rowsAffected", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_rows(self):
        val = self._attr.get('rows')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sql_result_set.py -> SQLResultSet.rows -> get attr')

    def get_insertId(self):
        val = self._attr.get('insertId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sql_result_set.py -> SQLResultSet.insertId -> get attr')

    def get_rowsAffected(self):
        val = self._attr.get('rowsAffected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sql_result_set.py -> SQLResultSet.rowsAffected -> get attr')
