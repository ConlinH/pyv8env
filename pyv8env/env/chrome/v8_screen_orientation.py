from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class ScreenOrientation(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ScreenOrientation, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("angle", "get_angle", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("lock", "fn_lock", 1, 0, 1, 0, 1, 0, 0),
        ("unlock", "fn_unlock", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_angle(self):
        val = self._attr.get('angle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_orientation.py -> ScreenOrientation.angle -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_orientation.py -> ScreenOrientation.type -> get attr')

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_orientation.py -> ScreenOrientation.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def fn_lock(self, *args):
        logger.debug(f'patch -> v8_screen_orientation.py -> ScreenOrientation.lock{tuple(args)} -> method')

    def fn_unlock(self, *args):
        logger.debug(f'patch -> v8_screen_orientation.py -> ScreenOrientation.unlock{tuple(args)} -> method')
