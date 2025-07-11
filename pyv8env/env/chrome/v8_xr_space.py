from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class XRSpace(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRSpace, self).__init__(*args, **kw)
