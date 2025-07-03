from .flags import *
from .v8_event import Event


@construct_111001
class ToggleEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ToggleEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oldState", "get_oldState", None, 0, 1, 0, 0, 0, 0, 1),
        ("newState", "get_newState", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_oldState(self):
        val = self._attr.get('oldState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_toggle_event.py -> ToggleEvent.oldState -> get attr')

    def get_newState(self):
        val = self._attr.get('newState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_toggle_event.py -> ToggleEvent.newState -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_toggle_event.py -> ToggleEvent.isTrusted -> get attr')
