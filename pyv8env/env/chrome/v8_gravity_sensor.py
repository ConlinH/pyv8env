from .flags import *
from .v8_accelerometer import Accelerometer


@construct_110001
class GravitySensor(Accelerometer):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(GravitySensor, self).__init__(*args, **kw)
