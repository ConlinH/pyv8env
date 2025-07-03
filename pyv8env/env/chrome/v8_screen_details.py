from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class ScreenDetails(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ScreenDetails, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("screens", "get_screens", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentScreen", "get_currentScreen", None, 0, 1, 0, 0, 0, 0, 1),
        ("onscreenschange", "get_onscreenschange", "set_onscreenschange", 0, 1, 0, 0, 0, 0, 1),
        ("oncurrentscreenchange", "get_oncurrentscreenchange", "set_oncurrentscreenchange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_screens(self):
        val = self._attr.get('screens')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_details.py -> ScreenDetails.screens -> get attr')

    def get_currentScreen(self):
        val = self._attr.get('currentScreen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_details.py -> ScreenDetails.currentScreen -> get attr')

    def get_onscreenschange(self):
        val = self._attr.get('onscreenschange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_details.py -> ScreenDetails.onscreenschange -> get attr')

    def set_onscreenschange(self, val):
        self._attr['onscreenschange'] = val

    def get_oncurrentscreenchange(self):
        val = self._attr.get('oncurrentscreenchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_details.py -> ScreenDetails.oncurrentscreenchange -> get attr')

    def set_oncurrentscreenchange(self, val):
        self._attr['oncurrentscreenchange'] = val
