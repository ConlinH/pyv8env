from .flags import *


@construct_110001
class AbortController:
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
        ("abort", "fn_abort", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_signal(self):
        val = self._attr.get('signal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abort_controller.py -> AbortController.signal -> get attr')

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_abort_controller.py -> AbortController.abort{tuple(args)} -> method')
