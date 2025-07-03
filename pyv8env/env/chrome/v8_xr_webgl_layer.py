from .flags import *
from .v8_xr_layer import XRLayer


@construct_112001
class XRWebGLLayer(XRLayer):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRWebGLLayer, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("antialias", "get_antialias", None, 0, 1, 0, 0, 0, 0, 1),
        ("ignoreDepthValues", "get_ignoreDepthValues", None, 0, 1, 0, 0, 0, 0, 1),
        ("framebufferWidth", "get_framebufferWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("framebufferHeight", "get_framebufferHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("framebuffer", "get_framebuffer", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getViewport", "fn_getViewport", 1, 0, 1, 0, 0, 0, 0),
        ("getNativeFramebufferScaleFactor", "fn_getNativeFramebufferScaleFactor", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_antialias(self):
        val = self._attr.get('antialias')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_layer.py -> XRWebGLLayer.antialias -> get attr')

    def get_ignoreDepthValues(self):
        val = self._attr.get('ignoreDepthValues')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_layer.py -> XRWebGLLayer.ignoreDepthValues -> get attr')

    def get_framebufferWidth(self):
        val = self._attr.get('framebufferWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_layer.py -> XRWebGLLayer.framebufferWidth -> get attr')

    def get_framebufferHeight(self):
        val = self._attr.get('framebufferHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_layer.py -> XRWebGLLayer.framebufferHeight -> get attr')

    def get_framebuffer(self):
        val = self._attr.get('framebuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_layer.py -> XRWebGLLayer.framebuffer -> get attr')

    def fn_getViewport(self, *args):
        logger.debug(f'patch -> v8_xr_webgl_layer.py -> XRWebGLLayer.getViewport{tuple(args)} -> method')

    @classmethod
    def fn_getNativeFramebufferScaleFactor(cls, *args):
        logger.debug(f'patch -> v8_xr_webgl_layer.py -> XRWebGLLayer.getNativeFramebufferScaleFactor{tuple(args)} -> method')
