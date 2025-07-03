from .flags import *
from .v8_midi_port import MIDIPort


@construct_100001
class MIDIInput(MIDIPort):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MIDIInput, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onmidimessage", "get_onmidimessage", "set_onmidimessage", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_onmidimessage(self):
        val = self._attr.get('onmidimessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_midi_input.py -> MIDIInput.onmidimessage -> get attr')

    def set_onmidimessage(self, val):
        self._attr['onmidimessage'] = val
