from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_focus_event import FocusEvent as V8FocusEvent


@impl_warp
class FocusEvent(V8FocusEvent):
    pass
