from .flags import *


@construct_100001
class GPUComputePassEncoder:
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
        ("insertDebugMarker", "fn_insertDebugMarker", 1, 0, 1, 0, 0, 0, 0),
        ("pushDebugGroup", "fn_pushDebugGroup", 1, 0, 1, 0, 0, 0, 0),
        ("dispatchWorkgroups", "fn_dispatchWorkgroups", 1, 0, 1, 0, 0, 0, 0),
        ("dispatchWorkgroupsIndirect", "fn_dispatchWorkgroupsIndirect", 2, 0, 1, 0, 0, 0, 0),
        ("end", "fn_end", 0, 0, 1, 0, 0, 0, 0),
        ("popDebugGroup", "fn_popDebugGroup", 0, 0, 1, 0, 0, 0, 0),
        ("setBindGroup", "fn_setBindGroup", 2, 0, 1, 0, 0, 0, 0),
        ("setPipeline", "fn_setPipeline", 1, 0, 1, 0, 0, 0, 0),
        ("writeTimestamp", "fn_writeTimestamp", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_insertDebugMarker(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.insertDebugMarker{tuple(args)} -> method')

    def fn_pushDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.pushDebugGroup{tuple(args)} -> method')

    def fn_dispatchWorkgroups(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.dispatchWorkgroups{tuple(args)} -> method')

    def fn_dispatchWorkgroupsIndirect(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.dispatchWorkgroupsIndirect{tuple(args)} -> method')

    def fn_end(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.end{tuple(args)} -> method')

    def fn_popDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.popDebugGroup{tuple(args)} -> method')

    def fn_setBindGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.setBindGroup{tuple(args)} -> method')

    def fn_setPipeline(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.setPipeline{tuple(args)} -> method')

    def fn_writeTimestamp(self, *args):
        logger.debug(f'patch -> v8_gpu_compute_pass_encoder.py -> GPUComputePassEncoder.writeTimestamp{tuple(args)} -> method')
