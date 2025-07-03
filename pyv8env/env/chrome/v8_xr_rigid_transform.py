from .flags import *


@construct_110001
class XRRigidTransform:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("position", "get_position", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientation", "get_orientation", None, 0, 1, 0, 0, 0, 0, 1),
        ("matrix", "get_matrix", None, 0, 1, 0, 0, 0, 0, 1),
        ("inverse", "get_inverse", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_position(self):
        val = self._attr.get('position')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_rigid_transform.py -> XRRigidTransform.position -> get attr')

    def get_orientation(self):
        val = self._attr.get('orientation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_rigid_transform.py -> XRRigidTransform.orientation -> get attr')

    def get_matrix(self):
        val = self._attr.get('matrix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_rigid_transform.py -> XRRigidTransform.matrix -> get attr')

    def get_inverse(self):
        val = self._attr.get('inverse')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_rigid_transform.py -> XRRigidTransform.inverse -> get attr')
