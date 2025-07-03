from .flags import *


@construct_100001
class MojoHandle:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("discardData", "fn_discardData", 1, 0, 1, 0, 0, 0, 0),
        ("duplicateBufferHandle", "fn_duplicateBufferHandle", 0, 0, 1, 0, 0, 0, 0),
        ("mapBuffer", "fn_mapBuffer", 2, 0, 1, 0, 0, 0, 0),
        ("queryData", "fn_queryData", 0, 0, 1, 0, 0, 0, 0),
        ("readData", "fn_readData", 1, 0, 1, 0, 0, 0, 0),
        ("readMessage", "fn_readMessage", 0, 0, 1, 0, 0, 0, 0),
        ("watch", "fn_watch", 2, 0, 1, 0, 0, 0, 0),
        ("writeData", "fn_writeData", 1, 0, 1, 0, 0, 0, 0),
        ("writeMessage", "fn_writeMessage", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.close{tuple(args)} -> method')

    def fn_discardData(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.discardData{tuple(args)} -> method')

    def fn_duplicateBufferHandle(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.duplicateBufferHandle{tuple(args)} -> method')

    def fn_mapBuffer(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.mapBuffer{tuple(args)} -> method')

    def fn_queryData(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.queryData{tuple(args)} -> method')

    def fn_readData(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.readData{tuple(args)} -> method')

    def fn_readMessage(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.readMessage{tuple(args)} -> method')

    def fn_watch(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.watch{tuple(args)} -> method')

    def fn_writeData(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.writeData{tuple(args)} -> method')

    def fn_writeMessage(self, *args):
        logger.debug(f'patch -> v8_mojo_handle.py -> MojoHandle.writeMessage{tuple(args)} -> method')
