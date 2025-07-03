from .flags import *
from .v8_event import Event


@construct_111001
class InvokeEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(InvokeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("invoker", "get_invoker", None, 0, 1, 0, 0, 0, 0, 1),
        ("action", "get_action", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_invoker(self):
        val = self._attr.get('invoker')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_invoke_event.py -> InvokeEvent.invoker -> get attr')

    def get_action(self):
        val = self._attr.get('action')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_invoke_event.py -> InvokeEvent.action -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_invoke_event.py -> InvokeEvent.isTrusted -> get attr')
