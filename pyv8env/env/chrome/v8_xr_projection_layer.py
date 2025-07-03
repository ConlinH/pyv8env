from .flags import *
from .v8_xr_composition_layer import XRCompositionLayer


@construct_100001
class XRProjectionLayer(XRCompositionLayer):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRProjectionLayer, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("textureWidth", "get_textureWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("textureHeight", "get_textureHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("textureArrayLength", "get_textureArrayLength", None, 0, 1, 0, 0, 0, 0, 1),
        ("ignoreDepthValues", "get_ignoreDepthValues", None, 0, 1, 0, 0, 0, 0, 1),
        ("fixedFoveation", "get_fixedFoveation", "set_fixedFoveation", 0, 1, 0, 0, 0, 0, 1),
        ("deltaPose", "get_deltaPose", "set_deltaPose", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_textureWidth(self):
        val = self._attr.get('textureWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_projection_layer.py -> XRProjectionLayer.textureWidth -> get attr')

    def get_textureHeight(self):
        val = self._attr.get('textureHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_projection_layer.py -> XRProjectionLayer.textureHeight -> get attr')

    def get_textureArrayLength(self):
        val = self._attr.get('textureArrayLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_projection_layer.py -> XRProjectionLayer.textureArrayLength -> get attr')

    def get_ignoreDepthValues(self):
        val = self._attr.get('ignoreDepthValues')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_projection_layer.py -> XRProjectionLayer.ignoreDepthValues -> get attr')

    def get_fixedFoveation(self):
        val = self._attr.get('fixedFoveation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_projection_layer.py -> XRProjectionLayer.fixedFoveation -> get attr')

    def set_fixedFoveation(self, val):
        self._attr['fixedFoveation'] = val

    def get_deltaPose(self):
        val = self._attr.get('deltaPose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_projection_layer.py -> XRProjectionLayer.deltaPose -> get attr')

    def set_deltaPose(self, val):
        self._attr['deltaPose'] = val
