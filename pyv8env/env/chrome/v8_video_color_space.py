from .flags import *


@construct_110001
class VideoColorSpace:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("primaries", "get_primaries", None, 0, 1, 0, 0, 0, 0, 1),
        ("transfer", "get_transfer", None, 0, 1, 0, 0, 0, 0, 1),
        ("matrix", "get_matrix", None, 0, 1, 0, 0, 0, 0, 1),
        ("fullRange", "get_fullRange", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_primaries(self):
        val = self._attr.get('primaries')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_color_space.py -> VideoColorSpace.primaries -> get attr')

    def get_transfer(self):
        val = self._attr.get('transfer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_color_space.py -> VideoColorSpace.transfer -> get attr')

    def get_matrix(self):
        val = self._attr.get('matrix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_color_space.py -> VideoColorSpace.matrix -> get attr')

    def get_fullRange(self):
        val = self._attr.get('fullRange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_color_space.py -> VideoColorSpace.fullRange -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_video_color_space.py -> VideoColorSpace.toJSON{tuple(args)} -> method')
