from .flags import *


@construct_100001
class NavigationActivation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("entry", "get_entry", None, 0, 1, 0, 0, 0, 0, 1),
        ("from", "get_from", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigationType", "get_navigationType", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_entry(self):
        val = self._attr.get('entry')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_activation.py -> NavigationActivation.entry -> get attr')

    def get_from(self):
        val = self._attr.get('from')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_activation.py -> NavigationActivation.from -> get attr')

    def get_navigationType(self):
        val = self._attr.get('navigationType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_activation.py -> NavigationActivation.navigationType -> get attr')
