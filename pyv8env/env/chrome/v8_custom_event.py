from .flags import *
from .v8_event import Event


@construct_111001
class CustomEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CustomEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("detail", "get_detail", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("initCustomEvent", "fn_initCustomEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_detail(self):
        val = self._attr.get('detail')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_custom_event.py -> CustomEvent.detail -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_custom_event.py -> CustomEvent.isTrusted -> get attr')

    def fn_initCustomEvent(self, *args):
        logger.debug(f'patch -> v8_custom_event.py -> CustomEvent.initCustomEvent{tuple(args)} -> method')
