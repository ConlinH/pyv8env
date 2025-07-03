from .flags import *


@construct_100001
class WebPrintingManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPrinters", "fn_getPrinters", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_getPrinters(self, *args):
        logger.debug(f'patch -> v8_web_printing_manager.py -> WebPrintingManager.getPrinters{tuple(args)} -> method')
