from .flags import *


@construct_100001
class Ink:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("requestPresenter", "fn_requestPresenter", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_requestPresenter(self, *args):
        logger.debug(f'patch -> v8_ink.py -> Ink.requestPresenter{tuple(args)} -> method')
