from .flags import *


@construct_000000
class FileWriterSync:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("position", "get_position", None, 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("seek", "fn_seek", 1, 0, 1, 0, 0, 0, 0),
        ("truncate", "fn_truncate", 1, 0, 1, 0, 0, 0, 0),
        ("write", "fn_write", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_position(self):
        val = self._attr.get('position')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer_sync.py -> FileWriterSync.position -> get attr')

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer_sync.py -> FileWriterSync.length -> get attr')

    def fn_seek(self, *args):
        logger.debug(f'patch -> v8_file_writer_sync.py -> FileWriterSync.seek{tuple(args)} -> method')

    def fn_truncate(self, *args):
        logger.debug(f'patch -> v8_file_writer_sync.py -> FileWriterSync.truncate{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_file_writer_sync.py -> FileWriterSync.write{tuple(args)} -> method')
