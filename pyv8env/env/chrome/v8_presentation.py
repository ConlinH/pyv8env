from .flags import *


@construct_100001
class Presentation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("defaultRequest", "get_defaultRequest", "set_defaultRequest", 0, 1, 0, 0, 0, 0, 1),
        ("receiver", "get_receiver", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_defaultRequest(self):
        val = self._attr.get('defaultRequest')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation.py -> Presentation.defaultRequest -> get attr')

    def set_defaultRequest(self, val):
        self._attr['defaultRequest'] = val

    def get_receiver(self):
        val = self._attr.get('receiver')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation.py -> Presentation.receiver -> get attr')
