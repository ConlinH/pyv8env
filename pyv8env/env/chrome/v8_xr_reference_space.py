from .flags import *
from .v8_xr_space import XRSpace


@construct_100001
class XRReferenceSpace(XRSpace):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRReferenceSpace, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onreset", "get_onreset", "set_onreset", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getOffsetReferenceSpace", "fn_getOffsetReferenceSpace", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_onreset(self):
        val = self._attr.get('onreset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_reference_space.py -> XRReferenceSpace.onreset -> get attr')

    def set_onreset(self, val):
        self._attr['onreset'] = val

    def fn_getOffsetReferenceSpace(self, *args):
        logger.debug(f'patch -> v8_xr_reference_space.py -> XRReferenceSpace.getOffsetReferenceSpace{tuple(args)} -> method')
