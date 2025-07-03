from .flags import *


@construct_100001
class Mojo:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    RESULT_OK = 0
    RESULT_CANCELLED = 1
    RESULT_UNKNOWN = 2
    RESULT_INVALID_ARGUMENT = 3
    RESULT_DEADLINE_EXCEEDED = 4
    RESULT_NOT_FOUND = 5
    RESULT_ALREADY_EXISTS = 6
    RESULT_PERMISSION_DENIED = 7
    RESULT_RESOURCE_EXHAUSTED = 8
    RESULT_FAILED_PRECONDITION = 9
    RESULT_ABORTED = 10
    RESULT_OUT_OF_RANGE = 11
    RESULT_UNIMPLEMENTED = 12
    RESULT_INTERNAL = 13
    RESULT_UNAVAILABLE = 14
    RESULT_DATA_LOSS = 15
    RESULT_BUSY = 16
    RESULT_SHOULD_WAIT = 17

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("bindInterface", "fn_bindInterface", 2, 0, 2, 0, 1, 1, 0),
        ("createDataPipe", "fn_createDataPipe", 1, 0, 2, 0, 1, 1, 0),
        ("createMessagePipe", "fn_createMessagePipe", 0, 0, 2, 0, 1, 1, 0),
        ("createSharedBuffer", "fn_createSharedBuffer", 1, 0, 2, 0, 1, 1, 0),
        ("getFileSystemAccessTransferToken", "fn_getFileSystemAccessTransferToken", 1, 0, 2, 0, 1, 1, 0),

    )

    @classmethod
    def fn_bindInterface(cls, *args):
        logger.debug(f'patch -> v8_mojo.py -> Mojo.bindInterface{tuple(args)} -> method')

    @classmethod
    def fn_createDataPipe(cls, *args):
        logger.debug(f'patch -> v8_mojo.py -> Mojo.createDataPipe{tuple(args)} -> method')

    @classmethod
    def fn_createMessagePipe(cls, *args):
        logger.debug(f'patch -> v8_mojo.py -> Mojo.createMessagePipe{tuple(args)} -> method')

    @classmethod
    def fn_createSharedBuffer(cls, *args):
        logger.debug(f'patch -> v8_mojo.py -> Mojo.createSharedBuffer{tuple(args)} -> method')

    @classmethod
    def fn_getFileSystemAccessTransferToken(cls, *args):
        logger.debug(f'patch -> v8_mojo.py -> Mojo.getFileSystemAccessTransferToken{tuple(args)} -> method')
