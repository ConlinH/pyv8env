from .flags import *


@construct_110001
class TextDetector:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("detect", "fn_detect", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_detect(self, *args):
        logger.debug(f'patch -> v8_text_detector.py -> TextDetector.detect{tuple(args)} -> method')
