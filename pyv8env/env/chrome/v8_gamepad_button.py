from .flags import *


@construct_100001
class GamepadButton:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("pressed", "get_pressed", None, 0, 1, 0, 0, 0, 0, 1),
        ("touched", "get_touched", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_pressed(self):
        val = self._attr.get('pressed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_button.py -> GamepadButton.pressed -> get attr')

    def get_touched(self):
        val = self._attr.get('touched')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_button.py -> GamepadButton.touched -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_button.py -> GamepadButton.value -> get attr')
