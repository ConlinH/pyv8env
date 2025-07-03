from .flags import *


@construct_111001
class ImageCapture:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("track", "get_track", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPhotoCapabilities", "fn_getPhotoCapabilities", 0, 0, 1, 0, 1, 0, 0),
        ("getPhotoSettings", "fn_getPhotoSettings", 0, 0, 1, 0, 1, 0, 0),
        ("grabFrame", "fn_grabFrame", 0, 0, 1, 0, 1, 0, 0),
        ("takePhoto", "fn_takePhoto", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_track(self):
        val = self._attr.get('track')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_capture.py -> ImageCapture.track -> get attr')

    def fn_getPhotoCapabilities(self, *args):
        logger.debug(f'patch -> v8_image_capture.py -> ImageCapture.getPhotoCapabilities{tuple(args)} -> method')

    def fn_getPhotoSettings(self, *args):
        logger.debug(f'patch -> v8_image_capture.py -> ImageCapture.getPhotoSettings{tuple(args)} -> method')

    def fn_grabFrame(self, *args):
        logger.debug(f'patch -> v8_image_capture.py -> ImageCapture.grabFrame{tuple(args)} -> method')

    def fn_takePhoto(self, *args):
        logger.debug(f'patch -> v8_image_capture.py -> ImageCapture.takePhoto{tuple(args)} -> method')
