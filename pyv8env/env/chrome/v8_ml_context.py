from .flags import *


@construct_100001
class MLContext:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("compute", "fn_compute", 3, 0, 1, 0, 1, 0, 0),
        ("createBuffer", "fn_createBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("dispatch", "fn_dispatch", 3, 0, 1, 0, 0, 0, 0),
        ("readBuffer", "fn_readBuffer", 1, 0, 1, 0, 1, 0, 0),
        ("writeBuffer", "fn_writeBuffer", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_compute(self, *args):
        logger.debug(f'patch -> v8_ml_context.py -> MLContext.compute{tuple(args)} -> method')

    def fn_createBuffer(self, *args):
        logger.debug(f'patch -> v8_ml_context.py -> MLContext.createBuffer{tuple(args)} -> method')

    def fn_dispatch(self, *args):
        logger.debug(f'patch -> v8_ml_context.py -> MLContext.dispatch{tuple(args)} -> method')

    def fn_readBuffer(self, *args):
        logger.debug(f'patch -> v8_ml_context.py -> MLContext.readBuffer{tuple(args)} -> method')

    def fn_writeBuffer(self, *args):
        logger.debug(f'patch -> v8_ml_context.py -> MLContext.writeBuffer{tuple(args)} -> method')
