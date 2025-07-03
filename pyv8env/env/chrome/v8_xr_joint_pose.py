from .flags import *
from .v8_xr_pose import XRPose


@construct_100001
class XRJointPose(XRPose):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRJointPose, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("radius", "get_radius", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_radius(self):
        val = self._attr.get('radius')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_joint_pose.py -> XRJointPose.radius -> get attr')
