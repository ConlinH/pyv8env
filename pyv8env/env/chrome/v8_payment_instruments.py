from .flags import *


@construct_100001
class PaymentInstruments:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clear", "fn_clear", 0, 0, 1, 0, 1, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 1, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 1, 0, 0),
        ("has", "fn_has", 1, 0, 1, 0, 1, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 1, 0, 0),
        ("set", "fn_set", 2, 0, 1, 0, 1, 0, 0),

    )

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_payment_instruments.py -> PaymentInstruments.clear{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_payment_instruments.py -> PaymentInstruments.delete{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_payment_instruments.py -> PaymentInstruments.get{tuple(args)} -> method')

    def fn_has(self, *args):
        logger.debug(f'patch -> v8_payment_instruments.py -> PaymentInstruments.has{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_payment_instruments.py -> PaymentInstruments.keys{tuple(args)} -> method')

    def fn_set(self, *args):
        logger.debug(f'patch -> v8_payment_instruments.py -> PaymentInstruments.set{tuple(args)} -> method')
