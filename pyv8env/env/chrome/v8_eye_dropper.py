from .flags import *


@construct_110001
class EyeDropper:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("open", "fn_open", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_eye_dropper.py -> EyeDropper.open{tuple(args)} -> method')
