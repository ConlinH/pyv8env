from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Clipboard(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Clipboard, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("read", "fn_read", 0, 0, 1, 0, 1, 0, 0),
        ("readText", "fn_readText", 0, 0, 1, 0, 1, 0, 0),
        ("write", "fn_write", 1, 0, 1, 0, 1, 0, 0),
        ("writeText", "fn_writeText", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_read(self, *args):
        logger.debug(f'patch -> v8_clipboard.py -> Clipboard.read{tuple(args)} -> method')

    def fn_readText(self, *args):
        logger.debug(f'patch -> v8_clipboard.py -> Clipboard.readText{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_clipboard.py -> Clipboard.write{tuple(args)} -> method')

    def fn_writeText(self, *args):
        logger.debug(f'patch -> v8_clipboard.py -> Clipboard.writeText{tuple(args)} -> method')
