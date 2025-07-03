from .flags import *


@construct_100001
class GamepadTouch:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("touchId", "get_touchId", None, 0, 1, 0, 0, 0, 0, 1),
        ("surfaceId", "get_surfaceId", None, 0, 1, 0, 0, 0, 0, 1),
        ("position", "get_position", None, 0, 1, 0, 0, 0, 0, 1),
        ("surfaceDimensions", "get_surfaceDimensions", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_touchId(self):
        val = self._attr.get('touchId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_touch.py -> GamepadTouch.touchId -> get attr')

    def get_surfaceId(self):
        val = self._attr.get('surfaceId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_touch.py -> GamepadTouch.surfaceId -> get attr')

    def get_position(self):
        val = self._attr.get('position')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_touch.py -> GamepadTouch.position -> get attr')

    def get_surfaceDimensions(self):
        val = self._attr.get('surfaceDimensions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_touch.py -> GamepadTouch.surfaceDimensions -> get attr')
