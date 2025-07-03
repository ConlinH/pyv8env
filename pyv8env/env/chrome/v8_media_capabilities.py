from .flags import *


@construct_100001
class MediaCapabilities:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("decodingInfo", "fn_decodingInfo", 1, 0, 1, 0, 1, 0, 0),
        ("encodingInfo", "fn_encodingInfo", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_decodingInfo(self, *args):
        logger.debug(f'patch -> v8_media_capabilities.py -> MediaCapabilities.decodingInfo{tuple(args)} -> method')

    def fn_encodingInfo(self, *args):
        logger.debug(f'patch -> v8_media_capabilities.py -> MediaCapabilities.encodingInfo{tuple(args)} -> method')
