from .flags import *


@construct_100001
class XRPlane:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("planeSpace", "get_planeSpace", None, 0, 1, 0, 0, 0, 0, 1),
        ("polygon", "get_polygon", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientation", "get_orientation", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastChangedTime", "get_lastChangedTime", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_planeSpace(self):
        val = self._attr.get('planeSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_plane.py -> XRPlane.planeSpace -> get attr')

    def get_polygon(self):
        val = self._attr.get('polygon')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_plane.py -> XRPlane.polygon -> get attr')

    def get_orientation(self):
        val = self._attr.get('orientation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_plane.py -> XRPlane.orientation -> get attr')

    def get_lastChangedTime(self):
        val = self._attr.get('lastChangedTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_plane.py -> XRPlane.lastChangedTime -> get attr')
