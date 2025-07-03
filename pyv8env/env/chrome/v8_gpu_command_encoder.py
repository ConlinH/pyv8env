from .flags import *


@construct_100001
class GPUCommandEncoder:
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
        ("beginComputePass", "fn_beginComputePass", 0, 0, 1, 0, 0, 0, 0),
        ("beginRenderPass", "fn_beginRenderPass", 1, 0, 1, 0, 0, 0, 0),
        ("copyBufferToTexture", "fn_copyBufferToTexture", 3, 0, 1, 0, 0, 0, 0),
        ("copyTextureToBuffer", "fn_copyTextureToBuffer", 3, 0, 1, 0, 0, 0, 0),
        ("copyTextureToTexture", "fn_copyTextureToTexture", 3, 0, 1, 0, 0, 0, 0),
        ("finish", "fn_finish", 0, 0, 1, 0, 0, 0, 0),
        ("insertDebugMarker", "fn_insertDebugMarker", 1, 0, 1, 0, 0, 0, 0),
        ("pushDebugGroup", "fn_pushDebugGroup", 1, 0, 1, 0, 0, 0, 0),
        ("clearBuffer", "fn_clearBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("copyBufferToBuffer", "fn_copyBufferToBuffer", 5, 0, 1, 0, 0, 0, 0),
        ("popDebugGroup", "fn_popDebugGroup", 0, 0, 1, 0, 0, 0, 0),
        ("resolveQuerySet", "fn_resolveQuerySet", 5, 0, 1, 0, 0, 0, 0),
        ("writeTimestamp", "fn_writeTimestamp", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_beginComputePass(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.beginComputePass{tuple(args)} -> method')

    def fn_beginRenderPass(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.beginRenderPass{tuple(args)} -> method')

    def fn_copyBufferToTexture(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.copyBufferToTexture{tuple(args)} -> method')

    def fn_copyTextureToBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.copyTextureToBuffer{tuple(args)} -> method')

    def fn_copyTextureToTexture(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.copyTextureToTexture{tuple(args)} -> method')

    def fn_finish(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.finish{tuple(args)} -> method')

    def fn_insertDebugMarker(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.insertDebugMarker{tuple(args)} -> method')

    def fn_pushDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.pushDebugGroup{tuple(args)} -> method')

    def fn_clearBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.clearBuffer{tuple(args)} -> method')

    def fn_copyBufferToBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.copyBufferToBuffer{tuple(args)} -> method')

    def fn_popDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.popDebugGroup{tuple(args)} -> method')

    def fn_resolveQuerySet(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.resolveQuerySet{tuple(args)} -> method')

    def fn_writeTimestamp(self, *args):
        logger.debug(f'patch -> v8_gpu_command_encoder.py -> GPUCommandEncoder.writeTimestamp{tuple(args)} -> method')
