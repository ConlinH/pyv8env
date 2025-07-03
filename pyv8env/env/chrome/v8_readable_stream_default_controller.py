from .flags import *


@construct_100001
class ReadableStreamDefaultController:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("desiredSize", "get_desiredSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("enqueue", "fn_enqueue", 0, 0, 1, 0, 0, 0, 0),
        ("error", "fn_error", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_desiredSize(self):
        val = self._attr.get('desiredSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_readable_stream_default_controller.py -> ReadableStreamDefaultController.desiredSize -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_readable_stream_default_controller.py -> ReadableStreamDefaultController.close{tuple(args)} -> method')

    def fn_enqueue(self, *args):
        logger.debug(f'patch -> v8_readable_stream_default_controller.py -> ReadableStreamDefaultController.enqueue{tuple(args)} -> method')

    def fn_error(self, *args):
        logger.debug(f'patch -> v8_readable_stream_default_controller.py -> ReadableStreamDefaultController.error{tuple(args)} -> method')
