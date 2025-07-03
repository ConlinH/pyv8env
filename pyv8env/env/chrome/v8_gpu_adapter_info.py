from .flags import *


@construct_100001
class GPUAdapterInfo:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("vendor", "get_vendor", None, 0, 1, 0, 0, 0, 0, 1),
        ("architecture", "get_architecture", None, 0, 1, 0, 0, 0, 0, 1),
        ("device", "get_device", None, 0, 1, 0, 0, 0, 0, 1),
        ("description", "get_description", None, 0, 1, 0, 0, 0, 0, 1),
        ("driver", "get_driver", None, 0, 1, 0, 0, 0, 0, 1),
        ("backend", "get_backend", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("memoryHeaps", "get_memoryHeaps", None, 0, 1, 0, 0, 0, 0, 1),
        ("d3dShaderModel", "get_d3dShaderModel", None, 0, 1, 0, 0, 0, 0, 1),
        ("vkDriverVersion", "get_vkDriverVersion", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_vendor(self):
        val = self._attr.get('vendor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.vendor -> get attr')

    def get_architecture(self):
        val = self._attr.get('architecture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.architecture -> get attr')

    def get_device(self):
        val = self._attr.get('device')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.device -> get attr')

    def get_description(self):
        val = self._attr.get('description')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.description -> get attr')

    def get_driver(self):
        val = self._attr.get('driver')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.driver -> get attr')

    def get_backend(self):
        val = self._attr.get('backend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.backend -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.type -> get attr')

    def get_memoryHeaps(self):
        val = self._attr.get('memoryHeaps')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.memoryHeaps -> get attr')

    def get_d3dShaderModel(self):
        val = self._attr.get('d3dShaderModel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.d3dShaderModel -> get attr')

    def get_vkDriverVersion(self):
        val = self._attr.get('vkDriverVersion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter_info.py -> GPUAdapterInfo.vkDriverVersion -> get attr')
