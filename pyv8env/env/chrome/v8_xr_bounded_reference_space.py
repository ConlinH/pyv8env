from .flags import *
from .v8_xr_reference_space import XRReferenceSpace


@construct_100001
class XRBoundedReferenceSpace(XRReferenceSpace):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRBoundedReferenceSpace, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("boundsGeometry", "get_boundsGeometry", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_boundsGeometry(self):
        val = self._attr.get('boundsGeometry')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_bounded_reference_space.py -> XRBoundedReferenceSpace.boundsGeometry -> get attr')
