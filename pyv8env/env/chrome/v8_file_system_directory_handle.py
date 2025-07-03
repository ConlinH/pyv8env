from .flags import *
from .v8_file_system_handle import FileSystemHandle


@construct_100001
class FileSystemDirectoryHandle(FileSystemHandle):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FileSystemDirectoryHandle, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getDirectoryHandle", "fn_getDirectoryHandle", 1, 0, 1, 0, 1, 0, 0),
        ("getFileHandle", "fn_getFileHandle", 1, 0, 1, 0, 1, 0, 0),
        ("removeEntry", "fn_removeEntry", 1, 0, 1, 0, 1, 0, 0),
        ("resolve", "fn_resolve", 1, 0, 1, 0, 1, 0, 0),
        ("entries", "fn_entries", 0, 0, 1, 0, 0, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 0, 0, 0),
        ("values", "fn_values", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_getDirectoryHandle(self, *args):
        logger.debug(f'patch -> v8_file_system_directory_handle.py -> FileSystemDirectoryHandle.getDirectoryHandle{tuple(args)} -> method')

    def fn_getFileHandle(self, *args):
        logger.debug(f'patch -> v8_file_system_directory_handle.py -> FileSystemDirectoryHandle.getFileHandle{tuple(args)} -> method')

    def fn_removeEntry(self, *args):
        logger.debug(f'patch -> v8_file_system_directory_handle.py -> FileSystemDirectoryHandle.removeEntry{tuple(args)} -> method')

    def fn_resolve(self, *args):
        logger.debug(f'patch -> v8_file_system_directory_handle.py -> FileSystemDirectoryHandle.resolve{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_file_system_directory_handle.py -> FileSystemDirectoryHandle.entries{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_file_system_directory_handle.py -> FileSystemDirectoryHandle.keys{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_file_system_directory_handle.py -> FileSystemDirectoryHandle.values{tuple(args)} -> method')
