from pyv8env import Null
from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_device_orientation_event import DeviceOrientationEvent as V8DeviceOrientationEvent


@impl_warp
class DeviceOrientationEvent(V8DeviceOrientationEvent):

    def __init__(self, *args, **kw):
        kw.setdefault("alpha", Null)
        kw.setdefault("beta", Null)
        kw.setdefault("gamma", Null)
        kw.setdefault("eventPhase", 0)
        super(DeviceOrientationEvent, self).__init__(*args, **kw)

