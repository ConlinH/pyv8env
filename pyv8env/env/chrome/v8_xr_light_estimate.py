from .flags import *


@construct_100001
class XRLightEstimate:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("sphericalHarmonicsCoefficients", "get_sphericalHarmonicsCoefficients", None, 0, 1, 0, 0, 0, 0, 1),
        ("primaryLightDirection", "get_primaryLightDirection", None, 0, 1, 0, 0, 0, 0, 1),
        ("primaryLightIntensity", "get_primaryLightIntensity", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_sphericalHarmonicsCoefficients(self):
        val = self._attr.get('sphericalHarmonicsCoefficients')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_light_estimate.py -> XRLightEstimate.sphericalHarmonicsCoefficients -> get attr')

    def get_primaryLightDirection(self):
        val = self._attr.get('primaryLightDirection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_light_estimate.py -> XRLightEstimate.primaryLightDirection -> get attr')

    def get_primaryLightIntensity(self):
        val = self._attr.get('primaryLightIntensity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_light_estimate.py -> XRLightEstimate.primaryLightIntensity -> get attr')
