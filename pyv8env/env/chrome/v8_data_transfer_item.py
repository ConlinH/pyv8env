from .flags import *


@construct_100001
class DataTransferItem:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("kind", "get_kind", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getAsFile", "fn_getAsFile", 0, 0, 1, 0, 0, 0, 0),
        ("getAsString", "fn_getAsString", 1, 0, 1, 0, 0, 0, 0),
        ("webkitGetAsEntry", "fn_webkitGetAsEntry", 0, 0, 1, 0, 0, 0, 0),
        ("getAsFileSystemHandle", "fn_getAsFileSystemHandle", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer_item.py -> DataTransferItem.kind -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer_item.py -> DataTransferItem.type -> get attr')

    def fn_getAsFile(self, *args):
        logger.debug(f'patch -> v8_data_transfer_item.py -> DataTransferItem.getAsFile{tuple(args)} -> method')

    def fn_getAsString(self, *args):
        logger.debug(f'patch -> v8_data_transfer_item.py -> DataTransferItem.getAsString{tuple(args)} -> method')

    def fn_webkitGetAsEntry(self, *args):
        logger.debug(f'patch -> v8_data_transfer_item.py -> DataTransferItem.webkitGetAsEntry{tuple(args)} -> method')

    def fn_getAsFileSystemHandle(self, *args):
        logger.debug(f'patch -> v8_data_transfer_item.py -> DataTransferItem.getAsFileSystemHandle{tuple(args)} -> method')
