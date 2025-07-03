from .flags import *


@construct_100001
class SmartCardContext:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("connect", "fn_connect", 2, 0, 1, 0, 1, 0, 0),
        ("getStatusChange", "fn_getStatusChange", 1, 0, 1, 0, 1, 0, 0),
        ("listReaders", "fn_listReaders", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_connect(self, *args):
        logger.debug(f'patch -> v8_smart_card_context.py -> SmartCardContext.connect{tuple(args)} -> method')

    def fn_getStatusChange(self, *args):
        logger.debug(f'patch -> v8_smart_card_context.py -> SmartCardContext.getStatusChange{tuple(args)} -> method')

    def fn_listReaders(self, *args):
        logger.debug(f'patch -> v8_smart_card_context.py -> SmartCardContext.listReaders{tuple(args)} -> method')
