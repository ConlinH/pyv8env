from .flags import *
from .v8_entry import Entry


@construct_000000
class FileEntry(Entry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FileEntry, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createWriter", "fn_createWriter", 1, 0, 1, 0, 0, 0, 0),
        ("file", "fn_file", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_createWriter(self, *args):
        logger.debug(f'patch -> v8_file_entry.py -> FileEntry.createWriter{tuple(args)} -> method')

    def fn_file(self, *args):
        logger.debug(f'patch -> v8_file_entry.py -> FileEntry.file{tuple(args)} -> method')
