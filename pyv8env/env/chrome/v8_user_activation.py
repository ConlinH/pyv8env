from .flags import *


@construct_100001
class UserActivation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("hasBeenActive", "get_hasBeenActive", None, 0, 1, 0, 0, 0, 0, 1),
        ("isActive", "get_isActive", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_hasBeenActive(self):
        val = self._attr.get('hasBeenActive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_user_activation.py -> UserActivation.hasBeenActive -> get attr')

    def get_isActive(self):
        val = self._attr.get('isActive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_user_activation.py -> UserActivation.isActive -> get attr')
