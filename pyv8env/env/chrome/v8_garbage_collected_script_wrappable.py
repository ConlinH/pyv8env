from .flags import *


@construct_000001
class GarbageCollectedScriptWrappable:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toString", "fn_toString", 0, 0, 1, 2, 0, 0, 0),

    )

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_garbage_collected_script_wrappable.py -> GarbageCollectedScriptWrappable.toString{tuple(args)} -> method')
