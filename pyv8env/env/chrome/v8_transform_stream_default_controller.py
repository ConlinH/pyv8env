from .flags import *


@construct_100001
class TransformStreamDefaultController:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("desiredSize", "get_desiredSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("enqueue", "fn_enqueue", 0, 0, 1, 0, 0, 0, 0),
        ("error", "fn_error", 0, 0, 1, 0, 0, 0, 0),
        ("terminate", "fn_terminate", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_desiredSize(self):
        val = self._attr.get('desiredSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_transform_stream_default_controller.py -> TransformStreamDefaultController.desiredSize -> get attr')

    def fn_enqueue(self, *args):
        logger.debug(f'patch -> v8_transform_stream_default_controller.py -> TransformStreamDefaultController.enqueue{tuple(args)} -> method')

    def fn_error(self, *args):
        logger.debug(f'patch -> v8_transform_stream_default_controller.py -> TransformStreamDefaultController.error{tuple(args)} -> method')

    def fn_terminate(self, *args):
        logger.debug(f'patch -> v8_transform_stream_default_controller.py -> TransformStreamDefaultController.terminate{tuple(args)} -> method')
