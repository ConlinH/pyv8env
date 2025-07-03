from .flags import *
from .v8_sensor import Sensor


@construct_110001
class Magnetometer(Sensor):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Magnetometer, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("z", "get_z", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_magnetometer.py -> Magnetometer.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_magnetometer.py -> Magnetometer.y -> get attr')

    def get_z(self):
        val = self._attr.get('z')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_magnetometer.py -> Magnetometer.z -> get attr')
