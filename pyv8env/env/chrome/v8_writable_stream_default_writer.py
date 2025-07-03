from .flags import *


@construct_111001
class WritableStreamDefaultWriter:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("closed", "get_closed", None, 0, 1, 0, 1, 0, 0, 1),
        ("desiredSize", "get_desiredSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("ready", "get_ready", None, 0, 1, 0, 1, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 1, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("releaseLock", "fn_releaseLock", 0, 0, 1, 0, 0, 0, 0),
        ("write", "fn_write", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_closed(self):
        val = self._attr.get('closed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_writable_stream_default_writer.py -> WritableStreamDefaultWriter.closed -> get attr')

    def get_desiredSize(self):
        val = self._attr.get('desiredSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_writable_stream_default_writer.py -> WritableStreamDefaultWriter.desiredSize -> get attr')

    def get_ready(self):
        val = self._attr.get('ready')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_writable_stream_default_writer.py -> WritableStreamDefaultWriter.ready -> get attr')

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_writable_stream_default_writer.py -> WritableStreamDefaultWriter.abort{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_writable_stream_default_writer.py -> WritableStreamDefaultWriter.close{tuple(args)} -> method')

    def fn_releaseLock(self, *args):
        logger.debug(f'patch -> v8_writable_stream_default_writer.py -> WritableStreamDefaultWriter.releaseLock{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_writable_stream_default_writer.py -> WritableStreamDefaultWriter.write{tuple(args)} -> method')
