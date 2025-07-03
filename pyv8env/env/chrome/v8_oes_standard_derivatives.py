from .flags import *


@construct_000000
class OESStandardDerivatives:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    FRAGMENT_SHADER_DERIVATIVE_HINT_OES = 35723
