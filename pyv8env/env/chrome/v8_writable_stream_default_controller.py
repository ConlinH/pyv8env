from .flags import *


@construct_100001
class WritableStreamDefaultController:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("signal", "get_signal", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("error", "fn_error", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_signal(self):
        val = self._attr.get('signal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_writable_stream_default_controller.py -> WritableStreamDefaultController.signal -> get attr')

    def fn_error(self, *args):
        logger.debug(f'patch -> v8_writable_stream_default_controller.py -> WritableStreamDefaultController.error{tuple(args)} -> method')
