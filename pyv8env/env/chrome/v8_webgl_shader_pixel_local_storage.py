from .flags import *


@construct_000000
class WebGLShaderPixelLocalStorage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    MAX_PIXEL_LOCAL_STORAGE_PLANES_WEBGL = 38624
    MAX_COLOR_ATTACHMENTS_WITH_ACTIVE_PIXEL_LOCAL_STORAGE_WEBGL = 38625
    MAX_COMBINED_DRAW_BUFFERS_AND_PIXEL_LOCAL_STORAGE_PLANES_WEBGL = 38626
    PIXEL_LOCAL_STORAGE_ACTIVE_PLANES_WEBGL = 38627
    LOAD_OP_ZERO_WEBGL = 38628
    LOAD_OP_CLEAR_WEBGL = 38629
    LOAD_OP_LOAD_WEBGL = 38630
    STORE_OP_STORE_WEBGL = 38631
    PIXEL_LOCAL_FORMAT_WEBGL = 38632
    PIXEL_LOCAL_TEXTURE_NAME_WEBGL = 38633
    PIXEL_LOCAL_TEXTURE_LEVEL_WEBGL = 38634
    PIXEL_LOCAL_TEXTURE_LAYER_WEBGL = 38635
    PIXEL_LOCAL_CLEAR_VALUE_FLOAT_WEBGL = 38636
    PIXEL_LOCAL_CLEAR_VALUE_INT_WEBGL = 38637
    PIXEL_LOCAL_CLEAR_VALUE_UNSIGNED_INT_WEBGL = 38638

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("beginPixelLocalStorageWEBGL", "fn_beginPixelLocalStorageWEBGL", 1, 0, 1, 0, 0, 0, 0),
        ("endPixelLocalStorageWEBGL", "fn_endPixelLocalStorageWEBGL", 1, 0, 1, 0, 0, 0, 0),
        ("framebufferPixelLocalClearValuefvWEBGL", "fn_framebufferPixelLocalClearValuefvWEBGL", 2, 0, 1, 0, 0, 0, 0),
        ("framebufferPixelLocalClearValueivWEBGL", "fn_framebufferPixelLocalClearValueivWEBGL", 2, 0, 1, 0, 0, 0, 0),
        ("framebufferPixelLocalClearValueuivWEBGL", "fn_framebufferPixelLocalClearValueuivWEBGL", 2, 0, 1, 0, 0, 0, 0),
        ("framebufferTexturePixelLocalStorageWEBGL", "fn_framebufferTexturePixelLocalStorageWEBGL", 4, 0, 1, 0, 0, 0, 0),
        ("getFramebufferPixelLocalStorageParameterWEBGL", "fn_getFramebufferPixelLocalStorageParameterWEBGL", 2, 0, 1, 0, 0, 0, 0),
        ("isCoherent", "fn_isCoherent", 0, 0, 1, 0, 0, 0, 0),
        ("pixelLocalStorageBarrierWEBGL", "fn_pixelLocalStorageBarrierWEBGL", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_beginPixelLocalStorageWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.beginPixelLocalStorageWEBGL{tuple(args)} -> method')

    def fn_endPixelLocalStorageWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.endPixelLocalStorageWEBGL{tuple(args)} -> method')

    def fn_framebufferPixelLocalClearValuefvWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.framebufferPixelLocalClearValuefvWEBGL{tuple(args)} -> method')

    def fn_framebufferPixelLocalClearValueivWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.framebufferPixelLocalClearValueivWEBGL{tuple(args)} -> method')

    def fn_framebufferPixelLocalClearValueuivWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.framebufferPixelLocalClearValueuivWEBGL{tuple(args)} -> method')

    def fn_framebufferTexturePixelLocalStorageWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.framebufferTexturePixelLocalStorageWEBGL{tuple(args)} -> method')

    def fn_getFramebufferPixelLocalStorageParameterWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.getFramebufferPixelLocalStorageParameterWEBGL{tuple(args)} -> method')

    def fn_isCoherent(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.isCoherent{tuple(args)} -> method')

    def fn_pixelLocalStorageBarrierWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_shader_pixel_local_storage.py -> WebGLShaderPixelLocalStorage.pixelLocalStorageBarrierWEBGL{tuple(args)} -> method')
