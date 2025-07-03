from .flags import *


@construct_100001
class GeolocationCoordinates:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("latitude", "get_latitude", None, 0, 1, 0, 0, 0, 0, 1),
        ("longitude", "get_longitude", None, 0, 1, 0, 0, 0, 0, 1),
        ("altitude", "get_altitude", None, 0, 1, 0, 0, 0, 0, 1),
        ("accuracy", "get_accuracy", None, 0, 1, 0, 0, 0, 0, 1),
        ("altitudeAccuracy", "get_altitudeAccuracy", None, 0, 1, 0, 0, 0, 0, 1),
        ("heading", "get_heading", None, 0, 1, 0, 0, 0, 0, 1),
        ("speed", "get_speed", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_latitude(self):
        val = self._attr.get('latitude')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.latitude -> get attr')

    def get_longitude(self):
        val = self._attr.get('longitude')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.longitude -> get attr')

    def get_altitude(self):
        val = self._attr.get('altitude')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.altitude -> get attr')

    def get_accuracy(self):
        val = self._attr.get('accuracy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.accuracy -> get attr')

    def get_altitudeAccuracy(self):
        val = self._attr.get('altitudeAccuracy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.altitudeAccuracy -> get attr')

    def get_heading(self):
        val = self._attr.get('heading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.heading -> get attr')

    def get_speed(self):
        val = self._attr.get('speed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.speed -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_geolocation_coordinates.py -> GeolocationCoordinates.toJSON{tuple(args)} -> method')
