from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class MIDIPort(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MIDIPort, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("connection", "get_connection", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("manufacturer", "get_manufacturer", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("version", "get_version", None, 0, 1, 0, 0, 0, 0, 1),
        ("onstatechange", "get_onstatechange", "set_onstatechange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("open", "fn_open", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_connection(self):
        val = self._attr.get('connection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.connection -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.id -> get attr')

    def get_manufacturer(self):
        val = self._attr.get('manufacturer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.manufacturer -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.name -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.state -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.type -> get attr')

    def get_version(self):
        val = self._attr.get('version')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.version -> get attr')

    def get_onstatechange(self):
        val = self._attr.get('onstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.onstatechange -> get attr')

    def set_onstatechange(self, val):
        self._attr['onstatechange'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.close{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_midi_port.py -> MIDIPort.open{tuple(args)} -> method')
