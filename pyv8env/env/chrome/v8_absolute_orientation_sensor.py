from .flags import *
from .v8_orientation_sensor import OrientationSensor


@construct_110001
class AbsoluteOrientationSensor(OrientationSensor):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AbsoluteOrientationSensor, self).__init__(*args, **kw)
