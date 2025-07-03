from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_input_event import InputEvent as V8InputEvent


@impl_warp
class InputEvent(V8InputEvent):
    pass
