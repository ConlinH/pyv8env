from .flags import *


@construct_110001
class WritableStream:
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
        ("abort", "fn_abort", 0, 0, 1, 0, 1, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("getWriter", "fn_getWriter", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_locked(self):
        val = self._attr.get('locked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_writable_stream.py -> WritableStream.locked -> get attr')

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_writable_stream.py -> WritableStream.abort{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_writable_stream.py -> WritableStream.close{tuple(args)} -> method')

    def fn_getWriter(self, *args):
        logger.debug(f'patch -> v8_writable_stream.py -> WritableStream.getWriter{tuple(args)} -> method')
