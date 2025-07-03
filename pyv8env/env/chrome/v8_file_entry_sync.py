from .flags import *
from .v8_entry_sync import EntrySync


@construct_000000
class FileEntrySync(EntrySync):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FileEntrySync, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createWriter", "fn_createWriter", 0, 0, 1, 0, 0, 0, 0),
        ("file", "fn_file", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_createWriter(self, *args):
        logger.debug(f'patch -> v8_file_entry_sync.py -> FileEntrySync.createWriter{tuple(args)} -> method')

    def fn_file(self, *args):
        logger.debug(f'patch -> v8_file_entry_sync.py -> FileEntrySync.file{tuple(args)} -> method')
