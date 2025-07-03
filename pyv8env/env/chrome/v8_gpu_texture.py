from .flags import *


@construct_100001
class GPUTexture:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("depthOrArrayLayers", "get_depthOrArrayLayers", None, 0, 1, 0, 0, 0, 0, 1),
        ("mipLevelCount", "get_mipLevelCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("sampleCount", "get_sampleCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("dimension", "get_dimension", None, 0, 1, 0, 0, 0, 0, 1),
        ("format", "get_format", None, 0, 1, 0, 0, 0, 0, 1),
        ("usage", "get_usage", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createView", "fn_createView", 0, 0, 1, 0, 0, 0, 0),
        ("destroy", "fn_destroy", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.height -> get attr')

    def get_depthOrArrayLayers(self):
        val = self._attr.get('depthOrArrayLayers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.depthOrArrayLayers -> get attr')

    def get_mipLevelCount(self):
        val = self._attr.get('mipLevelCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.mipLevelCount -> get attr')

    def get_sampleCount(self):
        val = self._attr.get('sampleCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.sampleCount -> get attr')

    def get_dimension(self):
        val = self._attr.get('dimension')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.dimension -> get attr')

    def get_format(self):
        val = self._attr.get('format')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.format -> get attr')

    def get_usage(self):
        val = self._attr.get('usage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.usage -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_createView(self, *args):
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.createView{tuple(args)} -> method')

    def fn_destroy(self, *args):
        logger.debug(f'patch -> v8_gpu_texture.py -> GPUTexture.destroy{tuple(args)} -> method')
