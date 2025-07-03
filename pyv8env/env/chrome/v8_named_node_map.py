from .flags import *


@construct_100101
class NamedNodeMap:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_name_set__')
            
    def __v8_name_query__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_name_query__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_name_del__')
            
    def __v8_name_enum__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_name_enum__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_named_node_map.py -> NamedNodeMap.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getNamedItem", "fn_getNamedItem", 1, 0, 1, 0, 0, 0, 1),
        ("getNamedItemNS", "fn_getNamedItemNS", 2, 0, 1, 0, 0, 0, 0),
        ("item", "fn_item", 1, 0, 1, 0, 0, 0, 1),
        ("removeNamedItem", "fn_removeNamedItem", 1, 0, 1, 0, 0, 0, 0),
        ("removeNamedItemNS", "fn_removeNamedItemNS", 2, 0, 1, 0, 0, 0, 0),
        ("setNamedItem", "fn_setNamedItem", 1, 0, 1, 0, 0, 0, 0),
        ("setNamedItemNS", "fn_setNamedItemNS", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.length -> get attr')

    def fn_getNamedItem(self, *args):
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.getNamedItem{tuple(args)} -> method')

    def fn_getNamedItemNS(self, *args):
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.getNamedItemNS{tuple(args)} -> method')

    def fn_item(self, *args):
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.item{tuple(args)} -> method')

    def fn_removeNamedItem(self, *args):
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.removeNamedItem{tuple(args)} -> method')

    def fn_removeNamedItemNS(self, *args):
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.removeNamedItemNS{tuple(args)} -> method')

    def fn_setNamedItem(self, *args):
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.setNamedItem{tuple(args)} -> method')

    def fn_setNamedItemNS(self, *args):
        logger.debug(f'patch -> v8_named_node_map.py -> NamedNodeMap.setNamedItemNS{tuple(args)} -> method')
