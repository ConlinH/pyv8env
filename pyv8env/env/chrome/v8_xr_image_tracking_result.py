from .flags import *


@construct_100001
class XRImageTrackingResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("imageSpace", "get_imageSpace", None, 0, 1, 0, 0, 0, 0, 1),
        ("index", "get_index", None, 0, 1, 0, 0, 0, 0, 1),
        ("trackingState", "get_trackingState", None, 0, 1, 0, 0, 0, 0, 1),
        ("measuredWidthInMeters", "get_measuredWidthInMeters", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_imageSpace(self):
        val = self._attr.get('imageSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_image_tracking_result.py -> XRImageTrackingResult.imageSpace -> get attr')

    def get_index(self):
        val = self._attr.get('index')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_image_tracking_result.py -> XRImageTrackingResult.index -> get attr')

    def get_trackingState(self):
        val = self._attr.get('trackingState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_image_tracking_result.py -> XRImageTrackingResult.trackingState -> get attr')

    def get_measuredWidthInMeters(self):
        val = self._attr.get('measuredWidthInMeters')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_image_tracking_result.py -> XRImageTrackingResult.measuredWidthInMeters -> get attr')
