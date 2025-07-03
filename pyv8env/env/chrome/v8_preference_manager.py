from .flags import *


@construct_100001
class PreferenceManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("colorScheme", "get_colorScheme", None, 0, 1, 0, 0, 0, 0, 1),
        ("contrast", "get_contrast", None, 0, 1, 0, 0, 0, 0, 1),
        ("reducedMotion", "get_reducedMotion", None, 0, 1, 0, 0, 0, 0, 1),
        ("reducedTransparency", "get_reducedTransparency", None, 0, 1, 0, 0, 0, 0, 1),
        ("reducedData", "get_reducedData", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_colorScheme(self):
        val = self._attr.get('colorScheme')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_manager.py -> PreferenceManager.colorScheme -> get attr')

    def get_contrast(self):
        val = self._attr.get('contrast')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_manager.py -> PreferenceManager.contrast -> get attr')

    def get_reducedMotion(self):
        val = self._attr.get('reducedMotion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_manager.py -> PreferenceManager.reducedMotion -> get attr')

    def get_reducedTransparency(self):
        val = self._attr.get('reducedTransparency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_manager.py -> PreferenceManager.reducedTransparency -> get attr')

    def get_reducedData(self):
        val = self._attr.get('reducedData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_manager.py -> PreferenceManager.reducedData -> get attr')
