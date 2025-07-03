from .flags import *


@construct_100001
class FetchLaterResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("activated", "get_activated", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_activated(self):
        val = self._attr.get('activated')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_later_result.py -> FetchLaterResult.activated -> get attr')
