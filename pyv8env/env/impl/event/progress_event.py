from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_progress_event import ProgressEvent as V8ProgressEvent


@impl_warp
class ProgressEvent(V8ProgressEvent):
    pass
