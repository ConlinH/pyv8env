from .flags import *


@construct_100001
class GPUComputePipeline:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getBindGroupLayout", "fn_getBindGroupLayout", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compute_pipeline.py -> GPUComputePipeline.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_getBindGroupLayout(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pipeline.py -> GPUComputePipeline.getBindGroupLayout{tuple(args)} -> method')
