from .flags import *


@construct_100001
class FileSystemChangeRecord:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("root", "get_root", None, 0, 1, 0, 0, 0, 0, 1),
        ("changedHandle", "get_changedHandle", None, 0, 1, 0, 0, 0, 0, 1),
        ("relativePathComponents", "get_relativePathComponents", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("relativePathMovedFrom", "get_relativePathMovedFrom", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_root(self):
        val = self._attr.get('root')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_change_record.py -> FileSystemChangeRecord.root -> get attr')

    def get_changedHandle(self):
        val = self._attr.get('changedHandle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_change_record.py -> FileSystemChangeRecord.changedHandle -> get attr')

    def get_relativePathComponents(self):
        val = self._attr.get('relativePathComponents')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_change_record.py -> FileSystemChangeRecord.relativePathComponents -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_change_record.py -> FileSystemChangeRecord.type -> get attr')

    def get_relativePathMovedFrom(self):
        val = self._attr.get('relativePathMovedFrom')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_change_record.py -> FileSystemChangeRecord.relativePathMovedFrom -> get attr')
