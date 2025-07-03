from .flags import *
from .v8_node_list import NodeList


@construct_100101
class RadioNodeList(NodeList):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RadioNodeList, self).__init__(*args, **kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_radio_node_list.py -> RadioNodeList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_radio_node_list.py -> RadioNodeList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_radio_node_list.py -> RadioNodeList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_radio_node_list.py -> RadioNodeList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_radio_node_list.py -> RadioNodeList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_radio_node_list.py -> RadioNodeList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_radio_node_list.py -> RadioNodeList.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val
