from .flags import *


@construct_100001
class XRPose:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("transform", "get_transform", None, 0, 1, 0, 0, 0, 0, 1),
        ("emulatedPosition", "get_emulatedPosition", None, 0, 1, 0, 0, 0, 0, 1),
        ("linearVelocity", "get_linearVelocity", None, 0, 1, 0, 0, 0, 0, 1),
        ("angularVelocity", "get_angularVelocity", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_transform(self):
        val = self._attr.get('transform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_pose.py -> XRPose.transform -> get attr')

    def get_emulatedPosition(self):
        val = self._attr.get('emulatedPosition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_pose.py -> XRPose.emulatedPosition -> get attr')

    def get_linearVelocity(self):
        val = self._attr.get('linearVelocity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_pose.py -> XRPose.linearVelocity -> get attr')

    def get_angularVelocity(self):
        val = self._attr.get('angularVelocity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_pose.py -> XRPose.angularVelocity -> get attr')
