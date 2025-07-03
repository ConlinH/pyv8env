from .flags import *


@construct_100001
class BarProp:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("visible", "get_visible", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_visible(self):
        val = self._attr.get('visible')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_bar_prop.py -> BarProp.visible -> get attr')
