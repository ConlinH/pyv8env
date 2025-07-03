from .flags import *


@construct_110001
class BarcodeDetector:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("detect", "fn_detect", 1, 0, 1, 0, 1, 0, 0),
        ("getSupportedFormats", "fn_getSupportedFormats", 0, 0, 2, 0, 1, 1, 0),

    )

    def fn_detect(self, *args):
        logger.debug(f'patch -> v8_barcode_detector.py -> BarcodeDetector.detect{tuple(args)} -> method')

    @classmethod
    def fn_getSupportedFormats(cls, *args):
        logger.debug(f'patch -> v8_barcode_detector.py -> BarcodeDetector.getSupportedFormats{tuple(args)} -> method')
