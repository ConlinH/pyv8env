from .flags import *


@construct_110001
class FileReaderSync:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("readAsArrayBuffer", "fn_readAsArrayBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("readAsBinaryString", "fn_readAsBinaryString", 1, 0, 1, 0, 0, 0, 0),
        ("readAsDataURL", "fn_readAsDataURL", 1, 0, 1, 0, 0, 0, 0),
        ("readAsText", "fn_readAsText", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_readAsArrayBuffer(self, *args):
        logger.debug(f'patch -> v8_file_reader_sync.py -> FileReaderSync.readAsArrayBuffer{tuple(args)} -> method')

    def fn_readAsBinaryString(self, *args):
        logger.debug(f'patch -> v8_file_reader_sync.py -> FileReaderSync.readAsBinaryString{tuple(args)} -> method')

    def fn_readAsDataURL(self, *args):
        logger.debug(f'patch -> v8_file_reader_sync.py -> FileReaderSync.readAsDataURL{tuple(args)} -> method')

    def fn_readAsText(self, *args):
        logger.debug(f'patch -> v8_file_reader_sync.py -> FileReaderSync.readAsText{tuple(args)} -> method')
