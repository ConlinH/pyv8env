from .flags import *
from .v8_xr_layer import XRLayer


@construct_100001
class XRCompositionLayer(XRLayer):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRCompositionLayer, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("layout", "get_layout", None, 0, 1, 0, 0, 0, 0, 1),
        ("blendTextureSourceAlpha", "get_blendTextureSourceAlpha", "set_blendTextureSourceAlpha", 0, 1, 0, 0, 0, 0, 1),
        ("chromaticAberrationCorrection", "get_chromaticAberrationCorrection", "set_chromaticAberrationCorrection", 0, 1, 0, 0, 0, 0, 1),
        ("forceMonoPresentation", "get_forceMonoPresentation", "set_forceMonoPresentation", 0, 1, 0, 0, 0, 0, 1),
        ("opacity", "get_opacity", "set_opacity", 0, 1, 0, 0, 0, 0, 1),
        ("mipLevels", "get_mipLevels", None, 0, 1, 0, 0, 0, 0, 1),
        ("needsRedraw", "get_needsRedraw", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("destroy", "fn_destroy", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_layout(self):
        val = self._attr.get('layout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.layout -> get attr')

    def get_blendTextureSourceAlpha(self):
        val = self._attr.get('blendTextureSourceAlpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.blendTextureSourceAlpha -> get attr')

    def set_blendTextureSourceAlpha(self, val):
        self._attr['blendTextureSourceAlpha'] = val

    def get_chromaticAberrationCorrection(self):
        val = self._attr.get('chromaticAberrationCorrection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.chromaticAberrationCorrection -> get attr')

    def set_chromaticAberrationCorrection(self, val):
        self._attr['chromaticAberrationCorrection'] = val

    def get_forceMonoPresentation(self):
        val = self._attr.get('forceMonoPresentation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.forceMonoPresentation -> get attr')

    def set_forceMonoPresentation(self, val):
        self._attr['forceMonoPresentation'] = val

    def get_opacity(self):
        val = self._attr.get('opacity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.opacity -> get attr')

    def set_opacity(self, val):
        self._attr['opacity'] = val

    def get_mipLevels(self):
        val = self._attr.get('mipLevels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.mipLevels -> get attr')

    def get_needsRedraw(self):
        val = self._attr.get('needsRedraw')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.needsRedraw -> get attr')

    def fn_destroy(self, *args):
        logger.debug(f'patch -> v8_xr_composition_layer.py -> XRCompositionLayer.destroy{tuple(args)} -> method')
