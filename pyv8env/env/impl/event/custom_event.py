from pyv8env import Undefined
from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_custom_event import CustomEvent as V8CustomEvent


@impl_warp
class CustomEvent(V8CustomEvent):

    def __init__(self, *args, **kw):
        super(CustomEvent, self).__init__(*args, **kw)
        if len(args) > 1:
            option = args[1]
            if isinstance(option, dict):
                self._attr['detail'] = option.get('detail', Undefined)