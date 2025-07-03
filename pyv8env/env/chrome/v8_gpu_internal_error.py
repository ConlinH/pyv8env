from .flags import *
from .v8_gpu_error import GPUError


@construct_111001
class GPUInternalError(GPUError):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(GPUInternalError, self).__init__(*args, **kw)
