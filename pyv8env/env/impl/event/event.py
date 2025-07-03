from pyv8env import Null

from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_event import Event as V8Event
from pyv8env.env.impl.error import V8TypeError


@impl_warp
class Event(V8Event):

    def fn_stopPropagation(self, *args):
        self._attr["cancelBubble"] = True

    def __init__(self, *args, **kw):
        if len(args) == 0:
            raise V8TypeError("Failed to construct 'Event': 1 argument required, but only 0 present.")

        self._attr = {
            "isTrusted": False,
            "type": str(args[0]),
            # "target": Null,
            # "currentTarget": Null,
            "eventPhase": 2,
            "bubbles": False,
            "cancelable": False,
            "defaultPrevented": False,
            # "composed": False,
            # "timeStamp": 1229632.1000000015,
            # "srcElement": Null,
            # "returnValue": True,
            "cancelBubble": False,
        }
        self._attr.update(kw)
