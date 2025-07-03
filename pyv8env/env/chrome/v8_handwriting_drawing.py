from .flags import *


@construct_000001
class HandwritingDrawing:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addStroke", "fn_addStroke", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("getPrediction", "fn_getPrediction", 0, 0, 1, 0, 1, 0, 0),
        ("getStrokes", "fn_getStrokes", 0, 0, 1, 0, 0, 0, 0),
        ("removeStroke", "fn_removeStroke", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_addStroke(self, *args):
        logger.debug(f'patch -> v8_handwriting_drawing.py -> HandwritingDrawing.addStroke{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_handwriting_drawing.py -> HandwritingDrawing.clear{tuple(args)} -> method')

    def fn_getPrediction(self, *args):
        logger.debug(f'patch -> v8_handwriting_drawing.py -> HandwritingDrawing.getPrediction{tuple(args)} -> method')

    def fn_getStrokes(self, *args):
        logger.debug(f'patch -> v8_handwriting_drawing.py -> HandwritingDrawing.getStrokes{tuple(args)} -> method')

    def fn_removeStroke(self, *args):
        logger.debug(f'patch -> v8_handwriting_drawing.py -> HandwritingDrawing.removeStroke{tuple(args)} -> method')
