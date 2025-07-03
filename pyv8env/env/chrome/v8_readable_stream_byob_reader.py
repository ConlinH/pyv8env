from .flags import *


@construct_111001
class ReadableStreamBYOBReader:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("closed", "get_closed", None, 0, 1, 0, 1, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("read", "fn_read", 1, 0, 1, 0, 1, 0, 0),
        ("releaseLock", "fn_releaseLock", 0, 0, 1, 0, 0, 0, 0),
        ("cancel", "fn_cancel", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_closed(self):
        val = self._attr.get('closed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_readable_stream_byob_reader.py -> ReadableStreamBYOBReader.closed -> get attr')

    def fn_read(self, *args):
        logger.debug(f'patch -> v8_readable_stream_byob_reader.py -> ReadableStreamBYOBReader.read{tuple(args)} -> method')

    def fn_releaseLock(self, *args):
        logger.debug(f'patch -> v8_readable_stream_byob_reader.py -> ReadableStreamBYOBReader.releaseLock{tuple(args)} -> method')

    def fn_cancel(self, *args):
        logger.debug(f'patch -> v8_readable_stream_byob_reader.py -> ReadableStreamBYOBReader.cancel{tuple(args)} -> method')
