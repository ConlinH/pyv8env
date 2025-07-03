from .flags import *


@construct_100001
class XRInputSource:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("handedness", "get_handedness", None, 0, 1, 0, 0, 0, 0, 1),
        ("targetRayMode", "get_targetRayMode", None, 0, 1, 0, 0, 0, 0, 1),
        ("targetRaySpace", "get_targetRaySpace", None, 0, 1, 0, 0, 0, 0, 1),
        ("gripSpace", "get_gripSpace", None, 0, 1, 0, 0, 0, 0, 1),
        ("gamepad", "get_gamepad", None, 0, 1, 0, 0, 0, 0, 1),
        ("profiles", "get_profiles", None, 0, 1, 0, 0, 0, 0, 1),
        ("hand", "get_hand", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_handedness(self):
        val = self._attr.get('handedness')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source.py -> XRInputSource.handedness -> get attr')

    def get_targetRayMode(self):
        val = self._attr.get('targetRayMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source.py -> XRInputSource.targetRayMode -> get attr')

    def get_targetRaySpace(self):
        val = self._attr.get('targetRaySpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source.py -> XRInputSource.targetRaySpace -> get attr')

    def get_gripSpace(self):
        val = self._attr.get('gripSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source.py -> XRInputSource.gripSpace -> get attr')

    def get_gamepad(self):
        val = self._attr.get('gamepad')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source.py -> XRInputSource.gamepad -> get attr')

    def get_profiles(self):
        val = self._attr.get('profiles')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source.py -> XRInputSource.profiles -> get attr')

    def get_hand(self):
        val = self._attr.get('hand')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source.py -> XRInputSource.hand -> get attr')
