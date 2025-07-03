from .flags import *
from .v8_xr_sub_image import XRSubImage


@construct_100001
class XRWebGLSubImage(XRSubImage):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRWebGLSubImage, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("colorTexture", "get_colorTexture", None, 0, 1, 0, 0, 0, 0, 1),
        ("depthStencilTexture", "get_depthStencilTexture", None, 0, 1, 0, 0, 0, 0, 1),
        ("motionVectorTexture", "get_motionVectorTexture", None, 0, 1, 0, 0, 0, 0, 1),
        ("imageIndex", "get_imageIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("colorTextureWidth", "get_colorTextureWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("colorTextureHeight", "get_colorTextureHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("depthStencilTextureWidth", "get_depthStencilTextureWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("depthStencilTextureHeight", "get_depthStencilTextureHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("motionVectorTextureWidth", "get_motionVectorTextureWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("motionVectorTextureHeight", "get_motionVectorTextureHeight", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_colorTexture(self):
        val = self._attr.get('colorTexture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.colorTexture -> get attr')

    def get_depthStencilTexture(self):
        val = self._attr.get('depthStencilTexture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.depthStencilTexture -> get attr')

    def get_motionVectorTexture(self):
        val = self._attr.get('motionVectorTexture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.motionVectorTexture -> get attr')

    def get_imageIndex(self):
        val = self._attr.get('imageIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.imageIndex -> get attr')

    def get_colorTextureWidth(self):
        val = self._attr.get('colorTextureWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.colorTextureWidth -> get attr')

    def get_colorTextureHeight(self):
        val = self._attr.get('colorTextureHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.colorTextureHeight -> get attr')

    def get_depthStencilTextureWidth(self):
        val = self._attr.get('depthStencilTextureWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.depthStencilTextureWidth -> get attr')

    def get_depthStencilTextureHeight(self):
        val = self._attr.get('depthStencilTextureHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.depthStencilTextureHeight -> get attr')

    def get_motionVectorTextureWidth(self):
        val = self._attr.get('motionVectorTextureWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.motionVectorTextureWidth -> get attr')

    def get_motionVectorTextureHeight(self):
        val = self._attr.get('motionVectorTextureHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_sub_image.py -> XRWebGLSubImage.motionVectorTextureHeight -> get attr')
