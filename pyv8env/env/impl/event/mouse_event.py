from pyv8env import Null
from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_mouse_event import MouseEvent as V8MouseEvent
from pyv8env.env.impl.error import V8TypeError


@impl_warp
class MouseEvent(V8MouseEvent):

    def __init__(self, *args, **kw):
        if len(args) == 0:
            raise V8TypeError("Failed to construct 'MouseEvent': 1 argument required, but only 0 present.")

        # for k, v in {
        #     "screenX": 0,
        #     "screenY": 0,
        #     "clientX": 0,
        #     "clientY": 0,
        #     "ctrlKey": False,
        #     "shiftKey": False,
        #     "altKey": False,
        #     "metaKey": False,
        #     "button": 0,
        #     "buttons": 0,
        #     "relatedTarget": Null,
        #     "pageX": 0,
        #     "pageY": 0,
        #     "x": 0,
        #     "y": 0,
        #     "offsetX": 0,
        #     "offsetY": 0,
        #     "movementX": 0,
        #     "movementY": 0,
        #     "fromElement": Null,
        #     "toElement": Null,
        #     "layerX": 0,
        #     "layerY": 0,
        # }.items():
        #     kw.setdefault(k, v)
        super(MouseEvent, self).__init__(*args, **kw)
