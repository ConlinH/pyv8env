from .flags import *


@construct_000000
class KHRParallelShaderCompile:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COMPLETION_STATUS_KHR = 37297
