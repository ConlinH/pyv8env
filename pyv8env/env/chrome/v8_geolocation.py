from .flags import *


@construct_100001
class Geolocation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clearWatch", "fn_clearWatch", 1, 0, 1, 0, 0, 0, 0),
        ("getCurrentPosition", "fn_getCurrentPosition", 1, 0, 1, 0, 0, 0, 0),
        ("watchPosition", "fn_watchPosition", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_clearWatch(self, *args):
        logger.debug(f'patch -> v8_geolocation.py -> Geolocation.clearWatch{tuple(args)} -> method')

    def fn_getCurrentPosition(self, *args):
        logger.debug(f'patch -> v8_geolocation.py -> Geolocation.getCurrentPosition{tuple(args)} -> method')

    def fn_watchPosition(self, *args):
        logger.debug(f'patch -> v8_geolocation.py -> Geolocation.watchPosition{tuple(args)} -> method')
