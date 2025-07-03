from .flags import *
from .v8_sensor import Sensor


@construct_100001
class OrientationSensor(Sensor):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(OrientationSensor, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("quaternion", "get_quaternion", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("populateMatrix", "fn_populateMatrix", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_quaternion(self):
        val = self._attr.get('quaternion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_orientation_sensor.py -> OrientationSensor.quaternion -> get attr')

    def fn_populateMatrix(self, *args):
        logger.debug(f'patch -> v8_orientation_sensor.py -> OrientationSensor.populateMatrix{tuple(args)} -> method')
