from .flags import *
from .v8_event import Event


@construct_111001
class MIDIConnectionEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MIDIConnectionEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("port", "get_port", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_port(self):
        val = self._attr.get('port')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_connection_event.py -> MIDIConnectionEvent.port -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_connection_event.py -> MIDIConnectionEvent.isTrusted -> get attr')
