from .flags import *
from .v8_event import Event


@construct_112001
class PromiseRejectionEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PromiseRejectionEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("promise", "get_promise", None, 0, 1, 0, 1, 0, 0, 1),
        ("reason", "get_reason", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_promise(self):
        val = self._attr.get('promise')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_promise_rejection_event.py -> PromiseRejectionEvent.promise -> get attr')

    def get_reason(self):
        val = self._attr.get('reason')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_promise_rejection_event.py -> PromiseRejectionEvent.reason -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_promise_rejection_event.py -> PromiseRejectionEvent.isTrusted -> get attr')
