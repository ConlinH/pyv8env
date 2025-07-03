from .flags import *


@construct_110001
class XRRay:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("origin", "get_origin", None, 0, 1, 0, 0, 0, 0, 1),
        ("direction", "get_direction", None, 0, 1, 0, 0, 0, 0, 1),
        ("matrix", "get_matrix", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_ray.py -> XRRay.origin -> get attr')

    def get_direction(self):
        val = self._attr.get('direction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_ray.py -> XRRay.direction -> get attr')

    def get_matrix(self):
        val = self._attr.get('matrix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_ray.py -> XRRay.matrix -> get attr')
