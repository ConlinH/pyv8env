from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Sensor(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Sensor, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("activated", "get_activated", None, 0, 1, 0, 0, 0, 0, 1),
        ("hasReading", "get_hasReading", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onreading", "get_onreading", "set_onreading", 0, 1, 0, 0, 0, 0, 1),
        ("onactivate", "get_onactivate", "set_onactivate", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_activated(self):
        val = self._attr.get('activated')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sensor.py -> Sensor.activated -> get attr')

    def get_hasReading(self):
        val = self._attr.get('hasReading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sensor.py -> Sensor.hasReading -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sensor.py -> Sensor.timestamp -> get attr')

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sensor.py -> Sensor.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onreading(self):
        val = self._attr.get('onreading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sensor.py -> Sensor.onreading -> get attr')

    def set_onreading(self, val):
        self._attr['onreading'] = val

    def get_onactivate(self):
        val = self._attr.get('onactivate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_sensor.py -> Sensor.onactivate -> get attr')

    def set_onactivate(self, val):
        self._attr['onactivate'] = val

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_sensor.py -> Sensor.start{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_sensor.py -> Sensor.stop{tuple(args)} -> method')
