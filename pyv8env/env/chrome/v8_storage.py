from .flags import *


@construct_100001
class Storage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_name_set__')
            
    def __v8_name_query__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_name_query__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_name_del__')
            
    def __v8_name_enum__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_name_enum__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_index_del__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_storage.py -> Storage.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("getItem", "fn_getItem", 1, 0, 1, 0, 0, 0, 0),
        ("key", "fn_key", 1, 0, 1, 0, 0, 0, 0),
        ("removeItem", "fn_removeItem", 1, 0, 1, 0, 0, 0, 0),
        ("setItem", "fn_setItem", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_storage.py -> Storage.length -> get attr')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_storage.py -> Storage.clear{tuple(args)} -> method')

    def fn_getItem(self, *args):
        logger.debug(f'patch -> v8_storage.py -> Storage.getItem{tuple(args)} -> method')

    def fn_key(self, *args):
        logger.debug(f'patch -> v8_storage.py -> Storage.key{tuple(args)} -> method')

    def fn_removeItem(self, *args):
        logger.debug(f'patch -> v8_storage.py -> Storage.removeItem{tuple(args)} -> method')

    def fn_setItem(self, *args):
        logger.debug(f'patch -> v8_storage.py -> Storage.setItem{tuple(args)} -> method')
