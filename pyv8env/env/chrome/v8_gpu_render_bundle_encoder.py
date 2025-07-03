from .flags import *


@construct_100001
class GPURenderBundleEncoder:
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
        ("finish", "fn_finish", 0, 0, 1, 0, 0, 0, 0),
        ("insertDebugMarker", "fn_insertDebugMarker", 1, 0, 1, 0, 0, 0, 0),
        ("pushDebugGroup", "fn_pushDebugGroup", 1, 0, 1, 0, 0, 0, 0),
        ("setIndexBuffer", "fn_setIndexBuffer", 2, 0, 1, 0, 0, 0, 0),
        ("draw", "fn_draw", 1, 0, 1, 0, 0, 0, 0),
        ("drawIndexed", "fn_drawIndexed", 1, 0, 1, 0, 0, 0, 0),
        ("drawIndexedIndirect", "fn_drawIndexedIndirect", 2, 0, 1, 0, 0, 0, 0),
        ("drawIndirect", "fn_drawIndirect", 2, 0, 1, 0, 0, 0, 0),
        ("popDebugGroup", "fn_popDebugGroup", 0, 0, 1, 0, 0, 0, 0),
        ("setBindGroup", "fn_setBindGroup", 2, 0, 1, 0, 0, 0, 0),
        ("setPipeline", "fn_setPipeline", 1, 0, 1, 0, 0, 0, 0),
        ("setVertexBuffer", "fn_setVertexBuffer", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_finish(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.finish{tuple(args)} -> method')

    def fn_insertDebugMarker(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.insertDebugMarker{tuple(args)} -> method')

    def fn_pushDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.pushDebugGroup{tuple(args)} -> method')

    def fn_setIndexBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.setIndexBuffer{tuple(args)} -> method')

    def fn_draw(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.draw{tuple(args)} -> method')

    def fn_drawIndexed(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.drawIndexed{tuple(args)} -> method')

    def fn_drawIndexedIndirect(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.drawIndexedIndirect{tuple(args)} -> method')

    def fn_drawIndirect(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.drawIndirect{tuple(args)} -> method')

    def fn_popDebugGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.popDebugGroup{tuple(args)} -> method')

    def fn_setBindGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.setBindGroup{tuple(args)} -> method')

    def fn_setPipeline(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.setPipeline{tuple(args)} -> method')

    def fn_setVertexBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_render_bundle_encoder.py -> GPURenderBundleEncoder.setVertexBuffer{tuple(args)} -> method')
