from .flags import *


@construct_100001
class WebPrinter:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cachedAttributes", "fn_cachedAttributes", 0, 0, 1, 0, 0, 0, 0),
        ("fetchAttributes", "fn_fetchAttributes", 0, 0, 1, 0, 1, 0, 0),
        ("printJob", "fn_printJob", 3, 0, 1, 0, 1, 0, 0),

    )

    def fn_cachedAttributes(self, *args):
        logger.debug(f'patch -> v8_web_printer.py -> WebPrinter.cachedAttributes{tuple(args)} -> method')

    def fn_fetchAttributes(self, *args):
        logger.debug(f'patch -> v8_web_printer.py -> WebPrinter.fetchAttributes{tuple(args)} -> method')

    def fn_printJob(self, *args):
        logger.debug(f'patch -> v8_web_printer.py -> WebPrinter.printJob{tuple(args)} -> method')
