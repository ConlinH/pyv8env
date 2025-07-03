from .flags import *
from .v8_event import Event


@construct_111001
class CloseEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CloseEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("wasClean", "get_wasClean", None, 0, 1, 0, 0, 0, 0, 1),
        ("code", "get_code", None, 0, 1, 0, 0, 0, 0, 1),
        ("reason", "get_reason", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_wasClean(self):
        val = self._attr.get('wasClean')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_close_event.py -> CloseEvent.wasClean -> get attr')

    def get_code(self):
        val = self._attr.get('code')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_close_event.py -> CloseEvent.code -> get attr')

    def get_reason(self):
        val = self._attr.get('reason')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_close_event.py -> CloseEvent.reason -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_close_event.py -> CloseEvent.isTrusted -> get attr')
