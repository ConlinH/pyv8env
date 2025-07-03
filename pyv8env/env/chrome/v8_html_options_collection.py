from .flags import *
from .v8_html_collection import HTMLCollection


@construct_100101
class HTMLOptionsCollection(HTMLCollection):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLOptionsCollection, self).__init__(*args, **kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_name_set__')
            
    def __v8_name_query__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_name_query__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_name_del__')
            
    def __v8_name_enum__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_name_enum__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_html_options_collection.py -> HTMLOptionsCollection.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", "set_length", 0, 1, 0, 0, 0, 0, 1),
        ("selectedIndex", "get_selectedIndex", "set_selectedIndex", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_options_collection.py -> HTMLOptionsCollection.length -> get attr')

    def set_length(self, val):
        self._attr['length'] = val

    def get_selectedIndex(self):
        val = self._attr.get('selectedIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_options_collection.py -> HTMLOptionsCollection.selectedIndex -> get attr')

    def set_selectedIndex(self, val):
        self._attr['selectedIndex'] = val

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_html_options_collection.py -> HTMLOptionsCollection.add{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_html_options_collection.py -> HTMLOptionsCollection.remove{tuple(args)} -> method')
