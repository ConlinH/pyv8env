from .flags import *


@construct_110001
class HandwritingStroke:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addPoint", "fn_addPoint", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("getPoints", "fn_getPoints", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_addPoint(self, *args):
        logger.debug(f'patch -> v8_handwriting_stroke.py -> HandwritingStroke.addPoint{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_handwriting_stroke.py -> HandwritingStroke.clear{tuple(args)} -> method')

    def fn_getPoints(self, *args):
        logger.debug(f'patch -> v8_handwriting_stroke.py -> HandwritingStroke.getPoints{tuple(args)} -> method')
