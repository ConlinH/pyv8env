from .flags import *


@construct_000000
class EXTClipControl:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    LOWER_LEFT_EXT = 36001
    UPPER_LEFT_EXT = 36002
    NEGATIVE_ONE_TO_ONE_EXT = 37726
    ZERO_TO_ONE_EXT = 37727
    CLIP_ORIGIN_EXT = 37724
    CLIP_DEPTH_MODE_EXT = 37725

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clipControlEXT", "fn_clipControlEXT", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_clipControlEXT(self, *args):
        logger.debug(f'patch -> v8_ext_clip_control.py -> EXTClipControl.clipControlEXT{tuple(args)} -> method')
