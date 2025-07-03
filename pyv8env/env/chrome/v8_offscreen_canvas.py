from .flags import *
from .v8_event_target import EventTarget


@construct_112001
class OffscreenCanvas(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(OffscreenCanvas, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("oncontextlost", "get_oncontextlost", "set_oncontextlost", 0, 1, 0, 0, 0, 0, 1),
        ("oncontextrestored", "get_oncontextrestored", "set_oncontextrestored", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("convertToBlob", "fn_convertToBlob", 0, 0, 1, 0, 1, 0, 0),
        ("getContext", "fn_getContext", 1, 0, 1, 0, 0, 0, 0),
        ("transferToImageBitmap", "fn_transferToImageBitmap", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_offscreen_canvas.py -> OffscreenCanvas.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_offscreen_canvas.py -> OffscreenCanvas.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_oncontextlost(self):
        val = self._attr.get('oncontextlost')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_offscreen_canvas.py -> OffscreenCanvas.oncontextlost -> get attr')

    def set_oncontextlost(self, val):
        self._attr['oncontextlost'] = val

    def get_oncontextrestored(self):
        val = self._attr.get('oncontextrestored')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_offscreen_canvas.py -> OffscreenCanvas.oncontextrestored -> get attr')

    def set_oncontextrestored(self, val):
        self._attr['oncontextrestored'] = val

    def fn_convertToBlob(self, *args):
        logger.debug(f'patch -> v8_offscreen_canvas.py -> OffscreenCanvas.convertToBlob{tuple(args)} -> method')

    def fn_getContext(self, *args):
        logger.debug(f'patch -> v8_offscreen_canvas.py -> OffscreenCanvas.getContext{tuple(args)} -> method')

    def fn_transferToImageBitmap(self, *args):
        logger.debug(f'patch -> v8_offscreen_canvas.py -> OffscreenCanvas.transferToImageBitmap{tuple(args)} -> method')
