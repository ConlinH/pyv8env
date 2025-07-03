from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_message_event import MessageEvent as V8MessageEvent


@impl_warp
class MessageEvent(V8MessageEvent):
    pass
