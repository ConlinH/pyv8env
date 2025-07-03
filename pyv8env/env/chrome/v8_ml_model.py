from .flags import *


@construct_000001
class MLModel:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("compute", "fn_compute", 1, 0, 1, 0, 1, 0, 0),
        ("inputs", "fn_inputs", 0, 0, 1, 0, 0, 0, 0),
        ("outputs", "fn_outputs", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_compute(self, *args):
        logger.debug(f'patch -> v8_ml_model.py -> MLModel.compute{tuple(args)} -> method')

    def fn_inputs(self, *args):
        logger.debug(f'patch -> v8_ml_model.py -> MLModel.inputs{tuple(args)} -> method')

    def fn_outputs(self, *args):
        logger.debug(f'patch -> v8_ml_model.py -> MLModel.outputs{tuple(args)} -> method')
