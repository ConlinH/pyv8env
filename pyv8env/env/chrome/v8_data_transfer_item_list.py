from .flags import *


@construct_100101
class DataTransferItemList:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_data_transfer_item_list.py -> DataTransferItemList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_data_transfer_item_list.py -> DataTransferItemList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_data_transfer_item_list.py -> DataTransferItemList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_data_transfer_item_list.py -> DataTransferItemList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_data_transfer_item_list.py -> DataTransferItemList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_data_transfer_item_list.py -> DataTransferItemList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer_item_list.py -> DataTransferItemList.length -> get attr')

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_data_transfer_item_list.py -> DataTransferItemList.add{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_data_transfer_item_list.py -> DataTransferItemList.clear{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_data_transfer_item_list.py -> DataTransferItemList.remove{tuple(args)} -> method')
