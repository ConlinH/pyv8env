from .flags import *


@construct_100001
class GPUAdapter:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("features", "get_features", None, 0, 1, 0, 0, 0, 0, 1),
        ("limits", "get_limits", None, 0, 1, 0, 0, 0, 0, 1),
        ("isFallbackAdapter", "get_isFallbackAdapter", None, 0, 1, 0, 0, 0, 0, 1),
        ("info", "get_info", None, 0, 1, 0, 0, 0, 0, 1),
        ("isCompatibilityMode", "get_isCompatibilityMode", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("requestAdapterInfo", "fn_requestAdapterInfo", 0, 0, 1, 0, 1, 0, 0),
        ("requestDevice", "fn_requestDevice", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_features(self):
        val = self._attr.get('features')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter.py -> GPUAdapter.features -> get attr')

    def get_limits(self):
        val = self._attr.get('limits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter.py -> GPUAdapter.limits -> get attr')

    def get_isFallbackAdapter(self):
        val = self._attr.get('isFallbackAdapter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter.py -> GPUAdapter.isFallbackAdapter -> get attr')

    def get_info(self):
        val = self._attr.get('info')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter.py -> GPUAdapter.info -> get attr')

    def get_isCompatibilityMode(self):
        val = self._attr.get('isCompatibilityMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_adapter.py -> GPUAdapter.isCompatibilityMode -> get attr')

    def fn_requestAdapterInfo(self, *args):
        logger.debug(f'patch -> v8_gpu_adapter.py -> GPUAdapter.requestAdapterInfo{tuple(args)} -> method')

    def fn_requestDevice(self, *args):
        logger.debug(f'patch -> v8_gpu_adapter.py -> GPUAdapter.requestDevice{tuple(args)} -> method')
