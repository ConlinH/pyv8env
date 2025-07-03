from .flags import *
from .v8_event import Event


@construct_111001
class PopStateEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PopStateEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),
        ("hasUAVisualTransition", "get_hasUAVisualTransition", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pop_state_event.py -> PopStateEvent.state -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pop_state_event.py -> PopStateEvent.isTrusted -> get attr')

    def get_hasUAVisualTransition(self):
        val = self._attr.get('hasUAVisualTransition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pop_state_event.py -> PopStateEvent.hasUAVisualTransition -> get attr')
