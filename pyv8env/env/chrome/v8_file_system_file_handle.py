from .flags import *
from .v8_file_system_handle import FileSystemHandle


@construct_100001
class FileSystemFileHandle(FileSystemHandle):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FileSystemFileHandle, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createWritable", "fn_createWritable", 0, 0, 1, 0, 1, 0, 0),
        ("getFile", "fn_getFile", 0, 0, 1, 0, 1, 0, 0),
        ("move", "fn_move", 1, 0, 1, 0, 1, 0, 0),
        ("createSyncAccessHandle", "fn_createSyncAccessHandle", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_createWritable(self, *args):
        logger.debug(f'patch -> v8_file_system_file_handle.py -> FileSystemFileHandle.createWritable{tuple(args)} -> method')

    def fn_getFile(self, *args):
        logger.debug(f'patch -> v8_file_system_file_handle.py -> FileSystemFileHandle.getFile{tuple(args)} -> method')

    def fn_move(self, *args):
        logger.debug(f'patch -> v8_file_system_file_handle.py -> FileSystemFileHandle.move{tuple(args)} -> method')

    def fn_createSyncAccessHandle(self, *args):
        logger.debug(f'patch -> v8_file_system_file_handle.py -> FileSystemFileHandle.createSyncAccessHandle{tuple(args)} -> method')
