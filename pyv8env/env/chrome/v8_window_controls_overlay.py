from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class WindowControlsOverlay(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WindowControlsOverlay, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("visible", "get_visible", None, 0, 1, 0, 0, 0, 0, 1),
        ("ongeometrychange", "get_ongeometrychange", "set_ongeometrychange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getTitlebarAreaRect", "fn_getTitlebarAreaRect", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_visible(self):
        val = self._attr.get('visible')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_window_controls_overlay.py -> WindowControlsOverlay.visible -> get attr')

    def get_ongeometrychange(self):
        val = self._attr.get('ongeometrychange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_window_controls_overlay.py -> WindowControlsOverlay.ongeometrychange -> get attr')

    def set_ongeometrychange(self, val):
        self._attr['ongeometrychange'] = val

    def fn_getTitlebarAreaRect(self, *args):
        logger.debug(f'patch -> v8_window_controls_overlay.py -> WindowControlsOverlay.getTitlebarAreaRect{tuple(args)} -> method')
