from .flags import *
from .v8_entry_sync import EntrySync


@construct_000000
class DirectoryEntrySync(EntrySync):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DirectoryEntrySync, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createReader", "fn_createReader", 0, 0, 1, 0, 0, 0, 0),
        ("getDirectory", "fn_getDirectory", 2, 0, 1, 0, 0, 0, 0),
        ("getFile", "fn_getFile", 2, 0, 1, 0, 0, 0, 0),
        ("removeRecursively", "fn_removeRecursively", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_createReader(self, *args):
        logger.debug(f'patch -> v8_directory_entry_sync.py -> DirectoryEntrySync.createReader{tuple(args)} -> method')

    def fn_getDirectory(self, *args):
        logger.debug(f'patch -> v8_directory_entry_sync.py -> DirectoryEntrySync.getDirectory{tuple(args)} -> method')

    def fn_getFile(self, *args):
        logger.debug(f'patch -> v8_directory_entry_sync.py -> DirectoryEntrySync.getFile{tuple(args)} -> method')

    def fn_removeRecursively(self, *args):
        logger.debug(f'patch -> v8_directory_entry_sync.py -> DirectoryEntrySync.removeRecursively{tuple(args)} -> method')
