from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class MIDIAccess(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MIDIAccess, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("inputs", "get_inputs", None, 0, 1, 0, 0, 0, 0, 1),
        ("outputs", "get_outputs", None, 0, 1, 0, 0, 0, 0, 1),
        ("sysexEnabled", "get_sysexEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("onstatechange", "get_onstatechange", "set_onstatechange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_inputs(self):
        val = self._attr.get('inputs')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_access.py -> MIDIAccess.inputs -> get attr')

    def get_outputs(self):
        val = self._attr.get('outputs')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_access.py -> MIDIAccess.outputs -> get attr')

    def get_sysexEnabled(self):
        val = self._attr.get('sysexEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_access.py -> MIDIAccess.sysexEnabled -> get attr')

    def get_onstatechange(self):
        val = self._attr.get('onstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_access.py -> MIDIAccess.onstatechange -> get attr')

    def set_onstatechange(self, val):
        self._attr['onstatechange'] = val
