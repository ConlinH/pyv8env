from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_112001
class BackgroundFetchEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BackgroundFetchEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("registration", "get_registration", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_registration(self):
        val = self._attr.get('registration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_event.py -> BackgroundFetchEvent.registration -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_event.py -> BackgroundFetchEvent.isTrusted -> get attr')
