from .flags import *


@construct_100001
class XRDepthInformation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("normDepthBufferFromNormView", "get_normDepthBufferFromNormView", None, 0, 1, 0, 0, 0, 0, 1),
        ("rawValueToMeters", "get_rawValueToMeters", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_depth_information.py -> XRDepthInformation.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_depth_information.py -> XRDepthInformation.height -> get attr')

    def get_normDepthBufferFromNormView(self):
        val = self._attr.get('normDepthBufferFromNormView')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_depth_information.py -> XRDepthInformation.normDepthBufferFromNormView -> get attr')

    def get_rawValueToMeters(self):
        val = self._attr.get('rawValueToMeters')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_depth_information.py -> XRDepthInformation.rawValueToMeters -> get attr')
