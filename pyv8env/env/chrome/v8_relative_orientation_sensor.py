from .flags import *
from .v8_orientation_sensor import OrientationSensor


@construct_110001
class RelativeOrientationSensor(OrientationSensor):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(RelativeOrientationSensor, self).__init__(*args, **kw)
