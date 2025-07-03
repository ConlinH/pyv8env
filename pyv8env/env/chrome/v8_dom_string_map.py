from .flags import *


@construct_100001
class DOMStringMap:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_name_set__')
            
    def __v8_name_query__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_name_query__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_name_del__')
            
    def __v8_name_enum__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_name_enum__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_index_del__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_dom_string_map.py -> DOMStringMap.__v8_index_desc__')
            