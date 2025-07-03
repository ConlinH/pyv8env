from .flags import *
from .v8_xr_depth_information import XRDepthInformation


@construct_100001
class XRWebGLDepthInformation(XRDepthInformation):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRWebGLDepthInformation, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("texture", "get_texture", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_texture(self):
        val = self._attr.get('texture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_webgl_depth_information.py -> XRWebGLDepthInformation.texture -> get attr')
