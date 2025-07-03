from .flags import *


@construct_111001
class ImageDecoder:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("complete", "get_complete", None, 0, 1, 0, 0, 0, 0, 1),
        ("completed", "get_completed", None, 0, 1, 0, 1, 0, 0, 1),
        ("tracks", "get_tracks", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("decode", "fn_decode", 0, 0, 1, 0, 1, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 0, 0, 0),
        ("isTypeSupported", "fn_isTypeSupported", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.type -> get attr')

    def get_complete(self):
        val = self._attr.get('complete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.complete -> get attr')

    def get_completed(self):
        val = self._attr.get('completed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.completed -> get attr')

    def get_tracks(self):
        val = self._attr.get('tracks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.tracks -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.close{tuple(args)} -> method')

    def fn_decode(self, *args):
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.decode{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.reset{tuple(args)} -> method')

    @classmethod
    def fn_isTypeSupported(cls, *args):
        logger.debug(f'patch -> v8_image_decoder.py -> ImageDecoder.isTypeSupported{tuple(args)} -> method')
