from .flags import *


@construct_100001
class IDBKeyRange:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("lower", "get_lower", None, 0, 1, 0, 0, 0, 0, 1),
        ("upper", "get_upper", None, 0, 1, 0, 0, 0, 0, 1),
        ("lowerOpen", "get_lowerOpen", None, 0, 1, 0, 0, 0, 0, 1),
        ("upperOpen", "get_upperOpen", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("includes", "fn_includes", 1, 0, 1, 0, 0, 0, 0),
        ("bound", "fn_bound", 2, 0, 2, 0, 1, 1, 0),
        ("lowerBound", "fn_lowerBound", 1, 0, 2, 0, 1, 1, 0),
        ("only", "fn_only", 1, 0, 2, 0, 1, 1, 0),
        ("upperBound", "fn_upperBound", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_lower(self):
        val = self._attr.get('lower')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.lower -> get attr')

    def get_upper(self):
        val = self._attr.get('upper')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.upper -> get attr')

    def get_lowerOpen(self):
        val = self._attr.get('lowerOpen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.lowerOpen -> get attr')

    def get_upperOpen(self):
        val = self._attr.get('upperOpen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.upperOpen -> get attr')

    def fn_includes(self, *args):
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.includes{tuple(args)} -> method')

    @classmethod
    def fn_bound(cls, *args):
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.bound{tuple(args)} -> method')

    @classmethod
    def fn_lowerBound(cls, *args):
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.lowerBound{tuple(args)} -> method')

    @classmethod
    def fn_only(cls, *args):
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.only{tuple(args)} -> method')

    @classmethod
    def fn_upperBound(cls, *args):
        logger.debug(f'patch -> v8_idb_key_range.py -> IDBKeyRange.upperBound{tuple(args)} -> method')
