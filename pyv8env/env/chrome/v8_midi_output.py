from .flags import *
from .v8_midi_port import MIDIPort


@construct_100001
class MIDIOutput(MIDIPort):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MIDIOutput, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("send", "fn_send", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_send(self, *args):
        logger.debug(f'patch -> v8_midi_output.py -> MIDIOutput.send{tuple(args)} -> method')
