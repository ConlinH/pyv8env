from .flags import *


@construct_100001
class CanvasGradient:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addColorStop", "fn_addColorStop", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_addColorStop(self, *args):
        logger.debug(f'patch -> v8_canvas_gradient.py -> CanvasGradient.addColorStop{tuple(args)} -> method')
