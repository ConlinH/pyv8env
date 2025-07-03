from .flags import *


@construct_100001
class GeolocationPositionError:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    PERMISSION_DENIED = 1
    POSITION_UNAVAILABLE = 2
    TIMEOUT = 3

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("code", "get_code", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_code(self):
        val = self._attr.get('code')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_position_error.py -> GeolocationPositionError.code -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_position_error.py -> GeolocationPositionError.message -> get attr')
