from .flags import *
from .v8_gamepad_event import GamepadEvent


@construct_111001
class GamepadAxisEvent(GamepadEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(GamepadAxisEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("axis", "get_axis", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_axis(self):
        val = self._attr.get('axis')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_axis_event.py -> GamepadAxisEvent.axis -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_axis_event.py -> GamepadAxisEvent.value -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_axis_event.py -> GamepadAxisEvent.isTrusted -> get attr')
