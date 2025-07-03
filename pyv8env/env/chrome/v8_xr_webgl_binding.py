from .flags import *


@construct_112001
class XRWebGLBinding:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("nativeProjectionScaleFactor", "get_nativeProjectionScaleFactor", None, 0, 1, 0, 0, 0, 0, 1),
        ("usesDepthValues", "get_usesDepthValues", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createProjectionLayer", "fn_createProjectionLayer", 0, 0, 1, 0, 0, 0, 0),
        ("getViewSubImage", "fn_getViewSubImage", 2, 0, 1, 0, 0, 0, 0),
        ("getCameraImage", "fn_getCameraImage", 1, 0, 1, 0, 0, 0, 0),
        ("getDepthInformation", "fn_getDepthInformation", 1, 0, 1, 0, 0, 0, 0),
        ("getReflectionCubeMap", "fn_getReflectionCubeMap", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_nativeProjectionScaleFactor(self):
        val = self._attr.get('nativeProjectionScaleFactor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_binding.py -> XRWebGLBinding.nativeProjectionScaleFactor -> get attr')

    def get_usesDepthValues(self):
        val = self._attr.get('usesDepthValues')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_binding.py -> XRWebGLBinding.usesDepthValues -> get attr')

    def fn_createProjectionLayer(self, *args):
        logger.debug(f'patch -> v8_xr_webgl_binding.py -> XRWebGLBinding.createProjectionLayer{tuple(args)} -> method')

    def fn_getViewSubImage(self, *args):
        logger.debug(f'patch -> v8_xr_webgl_binding.py -> XRWebGLBinding.getViewSubImage{tuple(args)} -> method')

    def fn_getCameraImage(self, *args):
        logger.debug(f'patch -> v8_xr_webgl_binding.py -> XRWebGLBinding.getCameraImage{tuple(args)} -> method')

    def fn_getDepthInformation(self, *args):
        logger.debug(f'patch -> v8_xr_webgl_binding.py -> XRWebGLBinding.getDepthInformation{tuple(args)} -> method')

    def fn_getReflectionCubeMap(self, *args):
        logger.debug(f'patch -> v8_xr_webgl_binding.py -> XRWebGLBinding.getReflectionCubeMap{tuple(args)} -> method')
