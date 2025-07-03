from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class GPUDevice(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(GPUDevice, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("features", "get_features", None, 0, 1, 0, 0, 0, 0, 1),
        ("limits", "get_limits", None, 0, 1, 0, 0, 0, 0, 1),
        ("lost", "get_lost", None, 0, 1, 0, 1, 0, 0, 1),
        ("queue", "get_queue", None, 0, 1, 0, 0, 0, 0, 1),
        ("onuncapturederror", "get_onuncapturederror", "set_onuncapturederror", 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createBindGroup", "fn_createBindGroup", 1, 0, 1, 0, 0, 0, 0),
        ("createBindGroupLayout", "fn_createBindGroupLayout", 1, 0, 1, 0, 0, 0, 0),
        ("createBuffer", "fn_createBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("createCommandEncoder", "fn_createCommandEncoder", 0, 0, 1, 0, 0, 0, 0),
        ("createComputePipeline", "fn_createComputePipeline", 1, 0, 1, 0, 0, 0, 0),
        ("createComputePipelineAsync", "fn_createComputePipelineAsync", 1, 0, 1, 0, 1, 0, 0),
        ("createPipelineLayout", "fn_createPipelineLayout", 1, 0, 1, 0, 0, 0, 0),
        ("createQuerySet", "fn_createQuerySet", 1, 0, 1, 0, 0, 0, 0),
        ("createRenderBundleEncoder", "fn_createRenderBundleEncoder", 1, 0, 1, 0, 0, 0, 0),
        ("createRenderPipeline", "fn_createRenderPipeline", 1, 0, 1, 0, 0, 0, 0),
        ("createRenderPipelineAsync", "fn_createRenderPipelineAsync", 1, 0, 1, 0, 1, 0, 0),
        ("createSampler", "fn_createSampler", 0, 0, 1, 0, 0, 0, 0),
        ("createShaderModule", "fn_createShaderModule", 1, 0, 1, 0, 0, 0, 0),
        ("createTexture", "fn_createTexture", 1, 0, 1, 0, 0, 0, 0),
        ("destroy", "fn_destroy", 0, 0, 1, 0, 0, 0, 0),
        ("importExternalTexture", "fn_importExternalTexture", 1, 0, 1, 0, 0, 0, 0),
        ("popErrorScope", "fn_popErrorScope", 0, 0, 1, 0, 1, 0, 0),
        ("pushErrorScope", "fn_pushErrorScope", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_features(self):
        val = self._attr.get('features')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.features -> get attr')

    def get_limits(self):
        val = self._attr.get('limits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.limits -> get attr')

    def get_lost(self):
        val = self._attr.get('lost')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.lost -> get attr')

    def get_queue(self):
        val = self._attr.get('queue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.queue -> get attr')

    def get_onuncapturederror(self):
        val = self._attr.get('onuncapturederror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.onuncapturederror -> get attr')

    def set_onuncapturederror(self, val):
        self._attr['onuncapturederror'] = val

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_createBindGroup(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createBindGroup{tuple(args)} -> method')

    def fn_createBindGroupLayout(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createBindGroupLayout{tuple(args)} -> method')

    def fn_createBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createBuffer{tuple(args)} -> method')

    def fn_createCommandEncoder(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createCommandEncoder{tuple(args)} -> method')

    def fn_createComputePipeline(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createComputePipeline{tuple(args)} -> method')

    def fn_createComputePipelineAsync(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createComputePipelineAsync{tuple(args)} -> method')

    def fn_createPipelineLayout(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createPipelineLayout{tuple(args)} -> method')

    def fn_createQuerySet(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createQuerySet{tuple(args)} -> method')

    def fn_createRenderBundleEncoder(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createRenderBundleEncoder{tuple(args)} -> method')

    def fn_createRenderPipeline(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createRenderPipeline{tuple(args)} -> method')

    def fn_createRenderPipelineAsync(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createRenderPipelineAsync{tuple(args)} -> method')

    def fn_createSampler(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createSampler{tuple(args)} -> method')

    def fn_createShaderModule(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createShaderModule{tuple(args)} -> method')

    def fn_createTexture(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.createTexture{tuple(args)} -> method')

    def fn_destroy(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.destroy{tuple(args)} -> method')

    def fn_importExternalTexture(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.importExternalTexture{tuple(args)} -> method')

    def fn_popErrorScope(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.popErrorScope{tuple(args)} -> method')

    def fn_pushErrorScope(self, *args):
        logger.debug(f'patch -> v8_gpu_device.py -> GPUDevice.pushErrorScope{tuple(args)} -> method')
