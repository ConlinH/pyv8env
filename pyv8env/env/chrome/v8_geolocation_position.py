from .flags import *


@construct_100001
class GeolocationPosition:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("coords", "get_coords", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_coords(self):
        val = self._attr.get('coords')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_position.py -> GeolocationPosition.coords -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_position.py -> GeolocationPosition.timestamp -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_geolocation_position.py -> GeolocationPosition.toJSON{tuple(args)} -> method')
