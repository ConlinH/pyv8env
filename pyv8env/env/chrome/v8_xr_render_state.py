from .flags import *


@construct_100001
class XRRenderState:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("depthNear", "get_depthNear", None, 0, 1, 0, 0, 0, 0, 1),
        ("depthFar", "get_depthFar", None, 0, 1, 0, 0, 0, 0, 1),
        ("inlineVerticalFieldOfView", "get_inlineVerticalFieldOfView", None, 0, 1, 0, 0, 0, 0, 1),
        ("baseLayer", "get_baseLayer", None, 0, 1, 0, 0, 0, 0, 1),
        ("layers", "get_layers", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_depthNear(self):
        val = self._attr.get('depthNear')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_render_state.py -> XRRenderState.depthNear -> get attr')

    def get_depthFar(self):
        val = self._attr.get('depthFar')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_render_state.py -> XRRenderState.depthFar -> get attr')

    def get_inlineVerticalFieldOfView(self):
        val = self._attr.get('inlineVerticalFieldOfView')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_render_state.py -> XRRenderState.inlineVerticalFieldOfView -> get attr')

    def get_baseLayer(self):
        val = self._attr.get('baseLayer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_render_state.py -> XRRenderState.baseLayer -> get attr')

    def get_layers(self):
        val = self._attr.get('layers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_render_state.py -> XRRenderState.layers -> get attr')
