from .flags import *


@construct_000031
class ShadowRealmGlobalScope:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
