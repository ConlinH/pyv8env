from .flags import *


@construct_100001
class GPU:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("wgslLanguageFeatures", "get_wgslLanguageFeatures", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPreferredCanvasFormat", "fn_getPreferredCanvasFormat", 0, 0, 1, 0, 0, 0, 0),
        ("requestAdapter", "fn_requestAdapter", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_wgslLanguageFeatures(self):
        val = self._attr.get('wgslLanguageFeatures')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu.py -> GPU.wgslLanguageFeatures -> get attr')

    def fn_getPreferredCanvasFormat(self, *args):
        logger.debug(f'patch -> v8_gpu.py -> GPU.getPreferredCanvasFormat{tuple(args)} -> method')

    def fn_requestAdapter(self, *args):
        logger.debug(f'patch -> v8_gpu.py -> GPU.requestAdapter{tuple(args)} -> method')
