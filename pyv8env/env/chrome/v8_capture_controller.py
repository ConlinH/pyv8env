from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class CaptureController(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CaptureController, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oncapturedmousechange", "get_oncapturedmousechange", "set_oncapturedmousechange", 0, 1, 0, 0, 0, 0, 1),
        ("oncapturedzoomlevelchange", "get_oncapturedzoomlevelchange", "set_oncapturedzoomlevelchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setFocusBehavior", "fn_setFocusBehavior", 1, 0, 1, 0, 0, 0, 0),
        ("getZoomLevel", "fn_getZoomLevel", 0, 0, 1, 0, 0, 0, 0),
        ("sendWheel", "fn_sendWheel", 1, 0, 1, 0, 1, 0, 0),
        ("setZoomLevel", "fn_setZoomLevel", 1, 0, 1, 0, 1, 0, 0),
        ("getSupportedZoomLevels", "fn_getSupportedZoomLevels", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_oncapturedmousechange(self):
        val = self._attr.get('oncapturedmousechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_capture_controller.py -> CaptureController.oncapturedmousechange -> get attr')

    def set_oncapturedmousechange(self, val):
        self._attr['oncapturedmousechange'] = val

    def get_oncapturedzoomlevelchange(self):
        val = self._attr.get('oncapturedzoomlevelchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_capture_controller.py -> CaptureController.oncapturedzoomlevelchange -> get attr')

    def set_oncapturedzoomlevelchange(self, val):
        self._attr['oncapturedzoomlevelchange'] = val

    def fn_setFocusBehavior(self, *args):
        logger.debug(f'patch -> v8_capture_controller.py -> CaptureController.setFocusBehavior{tuple(args)} -> method')

    def fn_getZoomLevel(self, *args):
        logger.debug(f'patch -> v8_capture_controller.py -> CaptureController.getZoomLevel{tuple(args)} -> method')

    def fn_sendWheel(self, *args):
        logger.debug(f'patch -> v8_capture_controller.py -> CaptureController.sendWheel{tuple(args)} -> method')

    def fn_setZoomLevel(self, *args):
        logger.debug(f'patch -> v8_capture_controller.py -> CaptureController.setZoomLevel{tuple(args)} -> method')

    @classmethod
    def fn_getSupportedZoomLevels(cls, *args):
        logger.debug(f'patch -> v8_capture_controller.py -> CaptureController.getSupportedZoomLevels{tuple(args)} -> method')
