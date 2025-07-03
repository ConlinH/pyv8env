from .flags import *


@construct_110001
class ReadableStream:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("locked", "get_locked", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancel", "fn_cancel", 0, 0, 1, 0, 1, 0, 0),
        ("getReader", "fn_getReader", 0, 0, 1, 0, 0, 0, 0),
        ("pipeThrough", "fn_pipeThrough", 1, 0, 1, 0, 0, 0, 0),
        ("pipeTo", "fn_pipeTo", 1, 0, 1, 0, 1, 0, 0),
        ("tee", "fn_tee", 0, 0, 1, 0, 0, 0, 0),
        ("values", "fn_values", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_locked(self):
        val = self._attr.get('locked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_readable_stream.py -> ReadableStream.locked -> get attr')

    def fn_cancel(self, *args):
        logger.debug(f'patch -> v8_readable_stream.py -> ReadableStream.cancel{tuple(args)} -> method')

    def fn_getReader(self, *args):
        logger.debug(f'patch -> v8_readable_stream.py -> ReadableStream.getReader{tuple(args)} -> method')

    def fn_pipeThrough(self, *args):
        logger.debug(f'patch -> v8_readable_stream.py -> ReadableStream.pipeThrough{tuple(args)} -> method')

    def fn_pipeTo(self, *args):
        logger.debug(f'patch -> v8_readable_stream.py -> ReadableStream.pipeTo{tuple(args)} -> method')

    def fn_tee(self, *args):
        logger.debug(f'patch -> v8_readable_stream.py -> ReadableStream.tee{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_readable_stream.py -> ReadableStream.values{tuple(args)} -> method')
