from .flags import *


@construct_100001
class GPURenderPassEncoder:
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
        ("executeBundles", "fn_executeBundles", 1, 0, 1, 0, 0, 0, 0),
        ("insertDebugMarker", "fn_insertDebugMarker", 1, 0, 1, 0, 0, 0, 0),
        ("pushDebugGroup", "fn_pushDebugGroup", 1, 0, 1, 0, 0, 0, 0),
        ("setBlendConstant", "fn_setBlendConstant", 1, 0, 1, 0, 0, 0, 0),
        ("setIndexBuffer", "fn_setIndexBuffer", 2, 0, 1, 0, 0, 0, 0),
        ("beginOcclusionQuery", "fn_beginOcclusionQuery", 1, 0, 1, 0, 0, 0, 0),
        ("draw", "fn_draw", 1, 0, 1, 0, 0, 0, 0),
        ("drawIndexed", "fn_drawIndexed", 1, 0, 1, 0, 0, 0, 0),
        ("drawIndexedIndirect", "fn_drawIndexedIndirect", 2, 0, 1, 0, 0, 0, 0),
        ("drawIndirect", "fn_drawIndirect", 2, 0, 1, 0, 0, 0, 0),
        ("end", "fn_end", 0, 0, 1, 0, 0, 0, 0),
        ("endOcclusionQuery", "fn_endOcclusionQuery", 0, 0, 1, 0, 0, 0, 0),
        ("popDebugGroup", "fn_popDebugGroup", 0, 0, 1, 0, 0, 0, 0),
        ("setBindGroup", "fn_setBindGroup", 2, 0, 1, 0, 0, 0, 0),
        ("setPipeline", "fn_setPipeline", 1, 0, 1, 0, 0, 0, 0),
        ("setScissorRect", "fn_setScissorRect", 4, 0, 1, 0, 0, 0, 0),
        ("setStencilReference", "fn_setStencilReference", 1, 0, 1, 0, 0, 0, 0),
        ("setVertexBuffer", "fn_setVertexBuffer", 2, 0, 1, 0, 0, 0, 0),
        ("setViewport", "fn_setViewport", 6, 0, 1, 0, 0, 0, 0),
        ("writeTimestamp", "fn_writeTimestamp", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_executeBundles(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.executeBundles{tuple(args)} -> method')

    def fn_insertDebugMarker(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.insertDebugMarker{tuple(args)} -> method')

    def fn_pushDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.pushDebugGroup{tuple(args)} -> method')

    def fn_setBlendConstant(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setBlendConstant{tuple(args)} -> method')

    def fn_setIndexBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setIndexBuffer{tuple(args)} -> method')

    def fn_beginOcclusionQuery(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.beginOcclusionQuery{tuple(args)} -> method')

    def fn_draw(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.draw{tuple(args)} -> method')

    def fn_drawIndexed(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.drawIndexed{tuple(args)} -> method')

    def fn_drawIndexedIndirect(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.drawIndexedIndirect{tuple(args)} -> method')

    def fn_drawIndirect(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.drawIndirect{tuple(args)} -> method')

    def fn_end(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.end{tuple(args)} -> method')

    def fn_endOcclusionQuery(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.endOcclusionQuery{tuple(args)} -> method')

    def fn_popDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.popDebugGroup{tuple(args)} -> method')

    def fn_setBindGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setBindGroup{tuple(args)} -> method')

    def fn_setPipeline(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setPipeline{tuple(args)} -> method')

    def fn_setScissorRect(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setScissorRect{tuple(args)} -> method')

    def fn_setStencilReference(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setStencilReference{tuple(args)} -> method')

    def fn_setVertexBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setVertexBuffer{tuple(args)} -> method')

    def fn_setViewport(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.setViewport{tuple(args)} -> method')

    def fn_writeTimestamp(self, *args):
        logger.debug(f'patch -> v8_gpu_render_pass_encoder.py -> GPURenderPassEncoder.writeTimestamp{tuple(args)} -> method')
