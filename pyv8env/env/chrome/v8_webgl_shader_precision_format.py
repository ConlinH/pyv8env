from .flags import *


@construct_100001
class WebGLShaderPrecisionFormat:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rangeMin", "get_rangeMin", None, 0, 1, 0, 0, 0, 0, 1),
        ("rangeMax", "get_rangeMax", None, 0, 1, 0, 0, 0, 0, 1),
        ("precision", "get_precision", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_rangeMin(self):
        val = self._attr.get('rangeMin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_shader_precision_format.py -> WebGLShaderPrecisionFormat.rangeMin -> get attr')

    def get_rangeMax(self):
        val = self._attr.get('rangeMax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_shader_precision_format.py -> WebGLShaderPrecisionFormat.rangeMax -> get attr')

    def get_precision(self):
        val = self._attr.get('precision')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_shader_precision_format.py -> WebGLShaderPrecisionFormat.precision -> get attr')
