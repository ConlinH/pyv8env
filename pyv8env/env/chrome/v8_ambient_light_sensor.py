from .flags import *
from .v8_sensor import Sensor


@construct_110001
class AmbientLightSensor(Sensor):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AmbientLightSensor, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("illuminance", "get_illuminance", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_illuminance(self):
        val = self._attr.get('illuminance')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ambient_light_sensor.py -> AmbientLightSensor.illuminance -> get attr')
