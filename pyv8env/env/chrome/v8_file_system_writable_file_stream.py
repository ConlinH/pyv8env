from .flags import *
from .v8_writable_stream import WritableStream


@construct_100001
class FileSystemWritableFileStream(WritableStream):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FileSystemWritableFileStream, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("mode", "get_mode", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("seek", "fn_seek", 1, 0, 1, 0, 1, 0, 0),
        ("truncate", "fn_truncate", 1, 0, 1, 0, 1, 0, 0),
        ("write", "fn_write", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_system_writable_file_stream.py -> FileSystemWritableFileStream.mode -> get attr')

    def fn_seek(self, *args):
        logger.debug(f'patch -> v8_file_system_writable_file_stream.py -> FileSystemWritableFileStream.seek{tuple(args)} -> method')

    def fn_truncate(self, *args):
        logger.debug(f'patch -> v8_file_system_writable_file_stream.py -> FileSystemWritableFileStream.truncate{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_file_system_writable_file_stream.py -> FileSystemWritableFileStream.write{tuple(args)} -> method')
