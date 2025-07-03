from .flags import *


@construct_100001
class GamepadHapticActuator:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("effects", "get_effects", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("playEffect", "fn_playEffect", 2, 0, 1, 0, 1, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_haptic_actuator.py -> GamepadHapticActuator.type -> get attr')

    def get_effects(self):
        val = self._attr.get('effects')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad_haptic_actuator.py -> GamepadHapticActuator.effects -> get attr')

    def fn_playEffect(self, *args):
        logger.debug(f'patch -> v8_gamepad_haptic_actuator.py -> GamepadHapticActuator.playEffect{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_gamepad_haptic_actuator.py -> GamepadHapticActuator.reset{tuple(args)} -> method')
