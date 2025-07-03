from .flags import *


@construct_000000
class UnderlyingSinkBase:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 1, 0, 1, 0, 1, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("start", "fn_start", 1, 0, 1, 0, 1, 0, 0),
        ("write", "fn_write", 2, 0, 1, 0, 1, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_underlying_sink_base.py -> UnderlyingSinkBase.type -> get attr')

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_underlying_sink_base.py -> UnderlyingSinkBase.abort{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_underlying_sink_base.py -> UnderlyingSinkBase.close{tuple(args)} -> method')

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_underlying_sink_base.py -> UnderlyingSinkBase.start{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_underlying_sink_base.py -> UnderlyingSinkBase.write{tuple(args)} -> method')
