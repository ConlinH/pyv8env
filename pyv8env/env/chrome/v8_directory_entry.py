from .flags import *
from .v8_entry import Entry


@construct_000000
class DirectoryEntry(Entry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DirectoryEntry, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createReader", "fn_createReader", 0, 0, 1, 0, 0, 0, 0),
        ("getDirectory", "fn_getDirectory", 1, 0, 1, 0, 0, 0, 0),
        ("getFile", "fn_getFile", 1, 0, 1, 0, 0, 0, 0),
        ("removeRecursively", "fn_removeRecursively", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_createReader(self, *args):
        logger.debug(f'patch -> v8_directory_entry.py -> DirectoryEntry.createReader{tuple(args)} -> method')

    def fn_getDirectory(self, *args):
        logger.debug(f'patch -> v8_directory_entry.py -> DirectoryEntry.getDirectory{tuple(args)} -> method')

    def fn_getFile(self, *args):
        logger.debug(f'patch -> v8_directory_entry.py -> DirectoryEntry.getFile{tuple(args)} -> method')

    def fn_removeRecursively(self, *args):
        logger.debug(f'patch -> v8_directory_entry.py -> DirectoryEntry.removeRecursively{tuple(args)} -> method')
