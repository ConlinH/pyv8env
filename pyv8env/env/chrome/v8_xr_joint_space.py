from .flags import *
from .v8_xr_space import XRSpace


@construct_100001
class XRJointSpace(XRSpace):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRJointSpace, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("jointName", "get_jointName", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_jointName(self):
        val = self._attr.get('jointName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_joint_space.py -> XRJointSpace.jointName -> get attr')
