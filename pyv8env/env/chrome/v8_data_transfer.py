from .flags import *


@construct_110001
class DataTransfer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("dropEffect", "get_dropEffect", "set_dropEffect", 0, 1, 0, 0, 0, 0, 1),
        ("effectAllowed", "get_effectAllowed", "set_effectAllowed", 0, 1, 0, 0, 0, 0, 1),
        ("items", "get_items", None, 0, 1, 0, 0, 0, 0, 1),
        ("types", "get_types", None, 0, 1, 0, 0, 0, 0, 1),
        ("files", "get_files", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clearData", "fn_clearData", 0, 0, 1, 0, 0, 0, 0),
        ("getData", "fn_getData", 1, 0, 1, 0, 0, 0, 0),
        ("setData", "fn_setData", 2, 0, 1, 0, 0, 0, 0),
        ("setDragImage", "fn_setDragImage", 3, 0, 1, 0, 0, 0, 0),

    )

    def get_dropEffect(self):
        val = self._attr.get('dropEffect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.dropEffect -> get attr')

    def set_dropEffect(self, val):
        self._attr['dropEffect'] = val

    def get_effectAllowed(self):
        val = self._attr.get('effectAllowed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.effectAllowed -> get attr')

    def set_effectAllowed(self, val):
        self._attr['effectAllowed'] = val

    def get_items(self):
        val = self._attr.get('items')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.items -> get attr')

    def get_types(self):
        val = self._attr.get('types')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.types -> get attr')

    def get_files(self):
        val = self._attr.get('files')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.files -> get attr')

    def fn_clearData(self, *args):
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.clearData{tuple(args)} -> method')

    def fn_getData(self, *args):
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.getData{tuple(args)} -> method')

    def fn_setData(self, *args):
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.setData{tuple(args)} -> method')

    def fn_setDragImage(self, *args):
        logger.debug(f'patch -> v8_data_transfer.py -> DataTransfer.setDragImage{tuple(args)} -> method')
