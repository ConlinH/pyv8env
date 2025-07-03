from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_touch_event import TouchEvent as V8TouchEvent
from pyv8env.env.impl.error import V8TypeError
from .touch_list import TouchList


@impl_warp
class TouchEvent(V8TouchEvent):
    def __init__(self, *args, **kw):
        if len(args) == 0:
            raise V8TypeError("Failed to construct 'MouseEvent': 1 argument required, but only 0 present.")

        for k, v in {
            "touches": TouchList(),
            "targetTouches": TouchList(),
            "changedTouches": TouchList(),
            "altKey": False,
            "metaKey": False,
            "ctrlKey": False,
            "shiftKey": False,
        }.items():
            kw.setdefault(k, v)
        super(TouchEvent, self).__init__(*args, **kw)
