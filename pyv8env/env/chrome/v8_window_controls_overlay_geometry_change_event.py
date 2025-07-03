from .flags import *
from .v8_event import Event


@construct_112001
class WindowControlsOverlayGeometryChangeEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WindowControlsOverlayGeometryChangeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("titlebarAreaRect", "get_titlebarAreaRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("visible", "get_visible", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_titlebarAreaRect(self):
        val = self._attr.get('titlebarAreaRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_window_controls_overlay_geometry_change_event.py -> WindowControlsOverlayGeometryChangeEvent.titlebarAreaRect -> get attr')

    def get_visible(self):
        val = self._attr.get('visible')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_window_controls_overlay_geometry_change_event.py -> WindowControlsOverlayGeometryChangeEvent.visible -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_window_controls_overlay_geometry_change_event.py -> WindowControlsOverlayGeometryChangeEvent.isTrusted -> get attr')
