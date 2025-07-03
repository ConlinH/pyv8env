from .flags import *


@construct_000001
class HandwritingRecognizer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("finish", "fn_finish", 0, 0, 1, 0, 0, 0, 0),
        ("startDrawing", "fn_startDrawing", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_finish(self, *args):
        logger.debug(f'patch -> v8_handwriting_recognizer.py -> HandwritingRecognizer.finish{tuple(args)} -> method')

    def fn_startDrawing(self, *args):
        logger.debug(f'patch -> v8_handwriting_recognizer.py -> HandwritingRecognizer.startDrawing{tuple(args)} -> method')
