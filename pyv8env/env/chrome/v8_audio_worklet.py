from .flags import *
from .v8_worklet import Worklet


@construct_100001
class AudioWorklet(Worklet):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioWorklet, self).__init__(*args, **kw)
