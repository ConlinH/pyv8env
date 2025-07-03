from .flags import *


@construct_100001
class Gamepad:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("index", "get_index", None, 0, 1, 0, 0, 0, 0, 1),
        ("connected", "get_connected", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("mapping", "get_mapping", None, 0, 1, 0, 0, 0, 0, 1),
        ("axes", "get_axes", None, 0, 1, 0, 0, 0, 0, 1),
        ("buttons", "get_buttons", None, 0, 1, 0, 0, 0, 0, 1),
        ("vibrationActuator", "get_vibrationActuator", None, 0, 1, 0, 0, 0, 0, 1),
        ("touchEvents", "get_touchEvents", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.id -> get attr')

    def get_index(self):
        val = self._attr.get('index')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.index -> get attr')

    def get_connected(self):
        val = self._attr.get('connected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.connected -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.timestamp -> get attr')

    def get_mapping(self):
        val = self._attr.get('mapping')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.mapping -> get attr')

    def get_axes(self):
        val = self._attr.get('axes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.axes -> get attr')

    def get_buttons(self):
        val = self._attr.get('buttons')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.buttons -> get attr')

    def get_vibrationActuator(self):
        val = self._attr.get('vibrationActuator')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.vibrationActuator -> get attr')

    def get_touchEvents(self):
        val = self._attr.get('touchEvents')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gamepad.py -> Gamepad.touchEvents -> get attr')
