from .flags import *


@construct_111001
class FencedFrameConfig:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setSharedStorageContext", "fn_setSharedStorageContext", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fenced_frame_config.py -> FencedFrameConfig.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fenced_frame_config.py -> FencedFrameConfig.height -> get attr')

    def fn_setSharedStorageContext(self, *args):
        logger.debug(f'patch -> v8_fenced_frame_config.py -> FencedFrameConfig.setSharedStorageContext{tuple(args)} -> method')
