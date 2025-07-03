from pyv8env import Null
from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_device_motion_event_acceleration import DeviceMotionEventAcceleration as V8DeviceMotionEventAcceleration


@impl_warp
class DeviceMotionEventAcceleration(V8DeviceMotionEventAcceleration):
    def __init__(self, *args, **kw):
        kw.setdefault("x", Null)
        kw.setdefault("y", Null)
        kw.setdefault("z", Null)
        self._attr = dict(kw)
