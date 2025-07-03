from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_pointer_event import PointerEvent as V8PointerEvent
from pyv8env.env.impl.error import V8TypeError


@impl_warp
class PointerEvent(V8PointerEvent):
    def __init__(self, *args, **kw):
        if len(args) == 0:
            raise V8TypeError("Failed to construct 'MouseEvent': 1 argument required, but only 0 present.")

        for k, v in {
            "pointerId": 0,
            "width": 1,
            "height": 1,
            "pressure": 0,
            "tiltX": 0,
            "tiltY": 0,
            "azimuthAngle": 0,
            "altitudeAngle": 1.5707963267948966,
            "tangentialPressure": 0,
            "twist": 0,
            "pointerType": "",
            "isPrimary": False,
        }.items():
            kw.setdefault(k, v)
        super(PointerEvent, self).__init__(*args, **kw)
