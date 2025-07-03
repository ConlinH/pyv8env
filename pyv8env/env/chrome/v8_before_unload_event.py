from .flags import *
from .v8_event import Event


@construct_100001
class BeforeUnloadEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BeforeUnloadEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("returnValue", "get_returnValue", "set_returnValue", 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_returnValue(self):
        val = self._attr.get('returnValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_before_unload_event.py -> BeforeUnloadEvent.returnValue -> get attr')

    def set_returnValue(self, val):
        self._attr['returnValue'] = val

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_before_unload_event.py -> BeforeUnloadEvent.isTrusted -> get attr')
