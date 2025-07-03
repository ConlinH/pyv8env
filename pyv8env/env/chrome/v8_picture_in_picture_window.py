from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class PictureInPictureWindow(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PictureInPictureWindow, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("onresize", "get_onresize", "set_onresize", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_picture_in_picture_window.py -> PictureInPictureWindow.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_picture_in_picture_window.py -> PictureInPictureWindow.height -> get attr')

    def get_onresize(self):
        val = self._attr.get('onresize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_picture_in_picture_window.py -> PictureInPictureWindow.onresize -> get attr')

    def set_onresize(self, val):
        self._attr['onresize'] = val
