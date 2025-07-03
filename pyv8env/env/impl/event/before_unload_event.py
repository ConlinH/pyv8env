from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_before_unload_event import BeforeUnloadEvent as V8BeforeUnloadEvent


@impl_warp
class BeforeUnloadEvent(V8BeforeUnloadEvent):
    def __init__(self, *args, **kw):
        kw.setdefault("returnValue", "")
        super(BeforeUnloadEvent, self).__init__(*args, **kw)

