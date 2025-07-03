from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_111001
class PushEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PushEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_event.py -> PushEvent.data -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_push_event.py -> PushEvent.isTrusted -> get attr')
