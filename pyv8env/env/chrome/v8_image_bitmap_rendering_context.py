from .flags import *


@construct_100001
class ImageBitmapRenderingContext:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("canvas", "get_canvas", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("transferFromImageBitmap", "fn_transferFromImageBitmap", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_canvas(self):
        val = self._attr.get('canvas')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_bitmap_rendering_context.py -> ImageBitmapRenderingContext.canvas -> get attr')

    def fn_transferFromImageBitmap(self, *args):
        logger.debug(f'patch -> v8_image_bitmap_rendering_context.py -> ImageBitmapRenderingContext.transferFromImageBitmap{tuple(args)} -> method')
