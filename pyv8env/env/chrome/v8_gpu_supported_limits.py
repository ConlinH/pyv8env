from .flags import *


@construct_100001
class GPUSupportedLimits:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("maxTextureDimension1D", "get_maxTextureDimension1D", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxTextureDimension2D", "get_maxTextureDimension2D", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxTextureDimension3D", "get_maxTextureDimension3D", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxTextureArrayLayers", "get_maxTextureArrayLayers", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxBindGroups", "get_maxBindGroups", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxBindGroupsPlusVertexBuffers", "get_maxBindGroupsPlusVertexBuffers", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxBindingsPerBindGroup", "get_maxBindingsPerBindGroup", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxDynamicUniformBuffersPerPipelineLayout", "get_maxDynamicUniformBuffersPerPipelineLayout", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxDynamicStorageBuffersPerPipelineLayout", "get_maxDynamicStorageBuffersPerPipelineLayout", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxSampledTexturesPerShaderStage", "get_maxSampledTexturesPerShaderStage", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxSamplersPerShaderStage", "get_maxSamplersPerShaderStage", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxStorageBuffersPerShaderStage", "get_maxStorageBuffersPerShaderStage", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxStorageTexturesPerShaderStage", "get_maxStorageTexturesPerShaderStage", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxUniformBuffersPerShaderStage", "get_maxUniformBuffersPerShaderStage", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxUniformBufferBindingSize", "get_maxUniformBufferBindingSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxStorageBufferBindingSize", "get_maxStorageBufferBindingSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("minUniformBufferOffsetAlignment", "get_minUniformBufferOffsetAlignment", None, 0, 1, 0, 0, 0, 0, 1),
        ("minStorageBufferOffsetAlignment", "get_minStorageBufferOffsetAlignment", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxVertexBuffers", "get_maxVertexBuffers", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxBufferSize", "get_maxBufferSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxVertexAttributes", "get_maxVertexAttributes", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxVertexBufferArrayStride", "get_maxVertexBufferArrayStride", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxInterStageShaderComponents", "get_maxInterStageShaderComponents", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxInterStageShaderVariables", "get_maxInterStageShaderVariables", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxColorAttachments", "get_maxColorAttachments", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxColorAttachmentBytesPerSample", "get_maxColorAttachmentBytesPerSample", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxComputeWorkgroupStorageSize", "get_maxComputeWorkgroupStorageSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxComputeInvocationsPerWorkgroup", "get_maxComputeInvocationsPerWorkgroup", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxComputeWorkgroupSizeX", "get_maxComputeWorkgroupSizeX", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxComputeWorkgroupSizeY", "get_maxComputeWorkgroupSizeY", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxComputeWorkgroupSizeZ", "get_maxComputeWorkgroupSizeZ", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxComputeWorkgroupsPerDimension", "get_maxComputeWorkgroupsPerDimension", None, 0, 1, 0, 0, 0, 0, 1),
        ("minSubgroupSize", "get_minSubgroupSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxSubgroupSize", "get_maxSubgroupSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_maxTextureDimension1D(self):
        val = self._attr.get('maxTextureDimension1D')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxTextureDimension1D -> get attr')

    def get_maxTextureDimension2D(self):
        val = self._attr.get('maxTextureDimension2D')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxTextureDimension2D -> get attr')

    def get_maxTextureDimension3D(self):
        val = self._attr.get('maxTextureDimension3D')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxTextureDimension3D -> get attr')

    def get_maxTextureArrayLayers(self):
        val = self._attr.get('maxTextureArrayLayers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxTextureArrayLayers -> get attr')

    def get_maxBindGroups(self):
        val = self._attr.get('maxBindGroups')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxBindGroups -> get attr')

    def get_maxBindGroupsPlusVertexBuffers(self):
        val = self._attr.get('maxBindGroupsPlusVertexBuffers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxBindGroupsPlusVertexBuffers -> get attr')

    def get_maxBindingsPerBindGroup(self):
        val = self._attr.get('maxBindingsPerBindGroup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxBindingsPerBindGroup -> get attr')

    def get_maxDynamicUniformBuffersPerPipelineLayout(self):
        val = self._attr.get('maxDynamicUniformBuffersPerPipelineLayout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxDynamicUniformBuffersPerPipelineLayout -> get attr')

    def get_maxDynamicStorageBuffersPerPipelineLayout(self):
        val = self._attr.get('maxDynamicStorageBuffersPerPipelineLayout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxDynamicStorageBuffersPerPipelineLayout -> get attr')

    def get_maxSampledTexturesPerShaderStage(self):
        val = self._attr.get('maxSampledTexturesPerShaderStage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxSampledTexturesPerShaderStage -> get attr')

    def get_maxSamplersPerShaderStage(self):
        val = self._attr.get('maxSamplersPerShaderStage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxSamplersPerShaderStage -> get attr')

    def get_maxStorageBuffersPerShaderStage(self):
        val = self._attr.get('maxStorageBuffersPerShaderStage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxStorageBuffersPerShaderStage -> get attr')

    def get_maxStorageTexturesPerShaderStage(self):
        val = self._attr.get('maxStorageTexturesPerShaderStage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxStorageTexturesPerShaderStage -> get attr')

    def get_maxUniformBuffersPerShaderStage(self):
        val = self._attr.get('maxUniformBuffersPerShaderStage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxUniformBuffersPerShaderStage -> get attr')

    def get_maxUniformBufferBindingSize(self):
        val = self._attr.get('maxUniformBufferBindingSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxUniformBufferBindingSize -> get attr')

    def get_maxStorageBufferBindingSize(self):
        val = self._attr.get('maxStorageBufferBindingSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxStorageBufferBindingSize -> get attr')

    def get_minUniformBufferOffsetAlignment(self):
        val = self._attr.get('minUniformBufferOffsetAlignment')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.minUniformBufferOffsetAlignment -> get attr')

    def get_minStorageBufferOffsetAlignment(self):
        val = self._attr.get('minStorageBufferOffsetAlignment')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.minStorageBufferOffsetAlignment -> get attr')

    def get_maxVertexBuffers(self):
        val = self._attr.get('maxVertexBuffers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxVertexBuffers -> get attr')

    def get_maxBufferSize(self):
        val = self._attr.get('maxBufferSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxBufferSize -> get attr')

    def get_maxVertexAttributes(self):
        val = self._attr.get('maxVertexAttributes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxVertexAttributes -> get attr')

    def get_maxVertexBufferArrayStride(self):
        val = self._attr.get('maxVertexBufferArrayStride')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxVertexBufferArrayStride -> get attr')

    def get_maxInterStageShaderComponents(self):
        val = self._attr.get('maxInterStageShaderComponents')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxInterStageShaderComponents -> get attr')

    def get_maxInterStageShaderVariables(self):
        val = self._attr.get('maxInterStageShaderVariables')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxInterStageShaderVariables -> get attr')

    def get_maxColorAttachments(self):
        val = self._attr.get('maxColorAttachments')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxColorAttachments -> get attr')

    def get_maxColorAttachmentBytesPerSample(self):
        val = self._attr.get('maxColorAttachmentBytesPerSample')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxColorAttachmentBytesPerSample -> get attr')

    def get_maxComputeWorkgroupStorageSize(self):
        val = self._attr.get('maxComputeWorkgroupStorageSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxComputeWorkgroupStorageSize -> get attr')

    def get_maxComputeInvocationsPerWorkgroup(self):
        val = self._attr.get('maxComputeInvocationsPerWorkgroup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxComputeInvocationsPerWorkgroup -> get attr')

    def get_maxComputeWorkgroupSizeX(self):
        val = self._attr.get('maxComputeWorkgroupSizeX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxComputeWorkgroupSizeX -> get attr')

    def get_maxComputeWorkgroupSizeY(self):
        val = self._attr.get('maxComputeWorkgroupSizeY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxComputeWorkgroupSizeY -> get attr')

    def get_maxComputeWorkgroupSizeZ(self):
        val = self._attr.get('maxComputeWorkgroupSizeZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxComputeWorkgroupSizeZ -> get attr')

    def get_maxComputeWorkgroupsPerDimension(self):
        val = self._attr.get('maxComputeWorkgroupsPerDimension')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxComputeWorkgroupsPerDimension -> get attr')

    def get_minSubgroupSize(self):
        val = self._attr.get('minSubgroupSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.minSubgroupSize -> get attr')

    def get_maxSubgroupSize(self):
        val = self._attr.get('maxSubgroupSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_supported_limits.py -> GPUSupportedLimits.maxSubgroupSize -> get attr')
