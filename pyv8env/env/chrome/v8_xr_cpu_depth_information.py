from .flags import *
from .v8_xr_depth_information import XRDepthInformation


@construct_100001
class XRCPUDepthInformation(XRDepthInformation):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRCPUDepthInformation, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getDepthInMeters", "fn_getDepthInMeters", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_cpu_depth_information.py -> XRCPUDepthInformation.data -> get attr')

    def fn_getDepthInMeters(self, *args):
        logger.debug(f'patch -> v8_xr_cpu_depth_information.py -> XRCPUDepthInformation.getDepthInMeters{tuple(args)} -> method')
