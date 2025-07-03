from pyv8env import Null
from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_device_motion_event_rotation_rate import DeviceMotionEventRotationRate as V8DeviceMotionEventRotationRate


@impl_warp
class DeviceMotionEventRotationRate(V8DeviceMotionEventRotationRate):
    def __init__(self, *args, **kw):
        kw.setdefault("alpha", Null)
        kw.setdefault("beta", Null)
        kw.setdefault("gamma", Null)
        self._attr = dict(kw)
